import requests
import json
import paths as pth
from paths import urls


def ok():
    with open(pth.logfile, 'a') as logfile:
        logfile.write('ok\n')


def not_ok():
    with open(pth.logfile, 'a') as logfile:
        logfile.write('not ok\n')


def step(n):
    with open(pth.logfile, 'a') as logfile:
        s = '\t Step ' + str(n) + ': '
        logfile.write(s)


def test_num(n):
    with open(pth.logfile, 'w') as logfile:
        s = 'Test ' + str(n) + '\n'
        logfile.write(s)


def get_token():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': pth.correct_login,
            'password': pth.correct_password,
            'grant_type': 'password',
            'scope': 'pegasus',
            'client_id': 'pegasus-v2',
            'client_secret': 'secret'}
    url = "http://srv-pnew-01-test:1001/auth/connect/token"

    step(0)
    try:
        r = requests.post(url, data=data, headers=headers)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return -1
    else:
        ok()
        return json.loads(r.text)['access_token']


def get_request(token, num_url, api, params=None):
    headers = {'Authorization': f'Bearer {token}'}
    if params is None:
        r = requests.get(urls[num_url] + api, headers=headers)
    else:
        r = requests.get(urls[num_url] + api, headers=headers, params=params)
    return r


def post_request(token, num_url, api, data=None):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    if data is None:
        r = requests.post(urls[num_url] + api, headers=headers)
    else:
        r = requests.post(urls[num_url] + api, data=json.dumps(data), headers=headers)
    return r


def delete_request(token, num_url, api, params=None):
    headers = {'Authorization': f'Bearer {token}'}
    if params is None:
        r = requests.delete(urls[num_url] + api, headers=headers)
    else:
        r = requests.delete(urls[num_url] + api, headers=headers, params=params)
    return r


def request_configurations_get_all(token):
    r = get_request(token, 0, '/api/v1/configurations/get-all')
    return r


def get_courier_by_id(token, courier_id):
    r = get_request(token, 1, f'/api/v1/couriers/get-courier-by-id/ {courier_id}', {'id': courier_id})
    return r


def get_couriers(token, page_index, page_size, sort_direction=0, search=''):
    r = get_request(token, 1, '/api/v1/couriers/get-couriers',
                    {'PageIndex': page_index, 'PageSize': page_size, 'SortDirection': sort_direction, 'Search': search})
    return r


def get_sending_condition_parameters(token):
    r = get_request(token, 12, '/api/v1/condition-parameters/get-all')
    return r


def get_groups_list(token):
    r = get_request(token, 14, pth.url_get_groups_list)
    return r


def check_group_existence(token, group_name):
    try:
        r = get_groups_list(token)
        if r.status_code != 200:
            raise
    except:
        return False
    r = json.loads(r.text)
    for group in r['result']:
        if group['displayName'] == group_name:
            return group['id']
    return False


def create_group(token, group_name):
    r = post_request(token, 14, pth.url_group_post, {'displayName': group_name})
    return r


def delete_group(token, group_id):
    r = delete_request(token, 14, pth.url_group_delete, {'id': group_id})
    return r


if __name__ == "__main__":
    tok = get_token()
    print(check_group_existence(tok, 'Бета-тестеры'))
