import requests
import json
import paths as pth
from paths import urls


def get_token():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': pth.correct_login,
            'password': pth.correct_password,
            'grant_type': 'password',
            'scope': 'pegasus',
            'client_id': 'pegasus-v2',
            'client_secret': 'secret'}
    url = "http://srv-pnew-01-test:1001/auth/connect/token"

    r = requests.post(url, data=data, headers=headers)
    return json.loads(r.text)['access_token']


def get_request(token, num, api, params):
    if params == {}:
        r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'})
    else:
        r = requests.get(urls[num] + api, headers={'Authorization': f'Bearer {token}'}, params=params)
    return r


def request_configurations_get_all(token):
    r = get_request(token, 0, '/api/v1/configurations/get-all', {})
    return json.loads(r.text)


def get_courier_by_id(token, courier_id):
    r = get_request(token, 1, '/api/v1/couriers/get-courier-by-id/{id}', {'id': courier_id})
    return r.text


if __name__ == "__main__":
    tok = get_token()
    print(request_configurations_get_all(tok))
    print(get_courier_by_id(tok, '359afb0c-b870-4610-9233-524db1d5a029'))

