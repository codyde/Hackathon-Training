import atexit
import configparser
import sys
import ssl
import re
import requests
from pyvim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__all__ = ['get_vcenter_health_status', 'get_vcenter_clusters', 'vm_count', 'vm_memory_count', 
            'get_uptime', 'count_vms_pyvmomi', 'get_vcenter_build']

config = configparser.ConfigParser()
AuthConfig = configparser.ConfigParser()


def auth_vcenter():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    username = config.get("vcenterConfig", "user")
    password = config.get("vcenterConfig", "password")
    print('Authenticating to vCenter REST API with user: {}'.format(username))
    resp = requests.post('{}/rest/com/vmware/cis/session'.format(url),
                         auth=(username, password), verify=False)
    authfile = open(".//etc//auth.ini", 'w')
    AuthConfig.add_section('auth')
    AuthConfig.set('auth', 'sid', resp.json()['value'])
    AuthConfig.write(authfile)
    authfile.close()
    if resp.status_code != 200:
        print('Error! API responded with: {}'.format(resp.status_code))
        return
    return resp.json()['value']


def get_api_data(req_url):
    AuthConfig.read(".//etc//auth.ini")
    try:
        sid = AuthConfig.get("auth", "sid")
        print("Existing SID found; using cached SID")
    except:
        print("No SID loaded; aquiring new")
        auth_vcenter()
        AuthConfig.read(".//etc//auth.ini")
        sid = AuthConfig.get("auth", "sid")
    print('Requesting Page: {}'.format(req_url))
    resp = requests.get(req_url, verify=False,
                        headers={'vmware-api-session-id': sid})
    if resp.status_code != 200:
        if resp.status_code == 401:
            print("401 received; clearing stale SID")
            AuthConfig.remove_option('auth', 'sid')
            AuthConfig.remove_section('auth')
        print('Error! API responded with: {}'.format(resp.status_code))
        auth_vcenter()
        get_api_data(req_url)
        return
    return resp

def auth_vcenter_soap():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    username = config.get("vcenterConfig", "user")
    password = config.get("vcenterConfig", "password")
    print('Authenticating to vCenter SOAP API, user: {}'.format(username))
    context = None
    if sys.version_info[:3] > (2, 7, 8):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    pattern = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
    parsed = re.search(pattern, url)
    host = parsed.group('host')
    si = SmartConnect(host=host,
                      user=username,
                      pwd=password,
                      port=443,
                      sslContext=context)
    atexit.register(Disconnect, si)
    return si


def get_vcenter_health_status():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    health = get_api_data('{}/rest/appliance/health/system'.format(url))
    j = health.json()
    return '{}'.format(j['value'])


def get_vcenter_clusters():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    cluster = get_api_data('{}/vcenter/cluster'.format(url))
    j = cluster.json()
    return '{}'.format(j['value'])


def vm_count():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    countarry = []
    for i in get_api_data('{}/rest/vcenter/vm'.format(url)).json()['value']:
        countarry.append(i['name'])
    p = len(countarry)
    return p


def vm_memory_count():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    memcount = []
    for i in get_api_data('{}/rest/vcenter/vm'.format(url)).json()['value']:
        memcount.append(i['memory_size_MiB'])
    p = sum(memcount)
    return p


def get_uptime():
    config.read(".//etc//config.ini")
    url = config.get("vcenterConfig", "url")
    resp = get_api_data('{}/rest/appliance/system/uptime'.format(url))
    k = resp.json()
    timeSeconds = k['value'] / 60 / 60
    return int(timeSeconds)


def count_vms_pyvmomi():
    si = auth_vcenter_soap()
    content = si.RetrieveContent()
    container = content.rootFolder
    viewType = [vim.VirtualMachine]
    recursive = True
    containerView = content.viewManager.CreateContainerView(
        container, viewType, recursive)
    children = containerView.view
    return len(children)


def get_vcenter_build():
    print("Retrieving vCenter Server Version and Build information ...")
    si = auth_vcenter_soap()
    return (si.content.about.apiVersion, si.content.about.build)
