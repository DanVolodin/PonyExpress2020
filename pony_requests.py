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


def request_configurations_get_all(token):
    r = requests.get(urls[0] + '/api/v1/configurations/get-all', headers={'Authorization': f'Bearer {token}'})
    return json.loads(r.text)


if __name__ == "__main__":
    tok = get_token()
    print(request_configurations_get_all(tok))

