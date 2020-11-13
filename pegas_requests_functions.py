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
        json.loads(r.text)
    except:
        not_ok()
        return -1
    else:
        ok()
        return json.loads(r.text)['access_token']


def get_request(token, num, api, params=None):
    if params is None:
        r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'})
    else:
        r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'}, params=params)
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


if __name__ == "__main__":
    tok = get_token()

