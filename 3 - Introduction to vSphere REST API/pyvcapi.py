import requests
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
