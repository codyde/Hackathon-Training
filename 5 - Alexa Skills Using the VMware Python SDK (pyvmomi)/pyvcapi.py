import atexit
import sys
import ssl
import re
import requests
from pyvim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://hlcorevc01.humblelab.com/rest'
username = 'administrator@vsphere.local'
password = 'VMware123!'


def auth_vcenter():
    print('Authenticating to vCenter REST API with user: {}'.format(username))
    resp = requests.post('{}/com/vmware/cis/session'.format(url),
                         auth=(username, password), verify=False)
    if resp.status_code != 200:
        print('Error! API responded with: {}'.format(resp.status_code))
        return
    return resp.json()['value']


def get_api_data(req_url):
    sid = auth_vcenter()
    print('Requesting Page: {}'.format(req_url))
    resp = requests.get(req_url, verify=False, headers={
                        'vmware-api-session-id': sid})
    if resp.status_code != 200:
        print('Error! API responded with: {}'.format(resp.status_code))
        return
    return resp


def get_vcenter_health_status():
    health = get_api_data('{}/appliance/health/system'.format(url))
    j = health.json()
    return '{}'.format(j['value'])


def get_vcenter_clusters():
    cluster = get_api_data('{}/vcenter/cluster'.format(url))
    j = cluster.json()
    return '{}'.format(j['value'])


def vm_count():
    countarry = []
    for i in get_api_data('{}/rest/vcenter/vm'.format(url)).json()['value']:
        countarry.append(i['name'])
    p = len(countarry)
    return p


def vm_memory_count():
    memcount = []
    for i in get_api_data('{}/rest/vcenter/vm'.format(url)).json()['value']:
        memcount.append(i['memory_size_MiB'])
    p = sum(memcount)
    return p


def get_uptime():
    resp = get_api_data('{}/rest/appliance/system/uptime'.format(url))
    k = resp.json()
    timeSeconds = k['value'] / 60 / 60
    return int(timeSeconds)


def auth_vcenter_soap():
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


def count_vms_pyvmomi():
    si = auth_vcenter_soap()
    content = si.RetrieveContent()
    container = content.rootFolder
    viewType = [vim.VirtualMachine]
    recursive = True
    containerView = content.viewManager.CreateContainerView(
        container, viewType, recursive)
    children = containerView.view
    print(children)
    return len(children)
