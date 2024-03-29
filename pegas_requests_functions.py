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
    url = "http://srv-pnew-02-test:1001/auth/connect/token"

    try:
        r = requests.post(url, data=data, headers=headers)
        if r.status_code != 200:
            raise
    except:
        return -1
    else:
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
    params = {'id': courier_id}
    r = get_request(token, 1, f'/api/v1/couriers/get-courier-by-id/ {courier_id}', params=params)
    return r


def get_couriers(token, page_index, page_size, sort_direction=0, search=''):
    params = {'PageIndex': page_index,
              'PageSize': page_size,
              'SortDirection': sort_direction,
              'Search': search}
    r = get_request(token, 1, '/api/v1/couriers/get-couriers', params=params)
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
    data = {'displayName': group_name}
    r = post_request(token, 14, pth.url_group_post, data=data)
    return r


def delete_group(token, group_id):
    params = {'id': group_id}
    r = delete_request(token, 14, pth.url_group_delete, params=params)
    return r


def create_event_blocks_71(token):
    data = {"description": ""}
    r = post_request(token, 6, '/api/v1/event-blocks71/post-item', data=data)
    return r


def create_event_blocks_71_object(token, block_id, scanned_number):
    data = {"eventBlockId": block_id,
            "pointId": "07c5c96a-6f52-428d-9332-0004c296067e",
            "scannedNumber": scanned_number,
            "hostName": pth.random_name
            }
    r = post_request(token, 6, '/api/v1/pegasus-events71/post-item', data=data)
    return r


def get_event_blocks_71_object(token, block_id, object_id):
    params = {"id": object_id}
    r = get_request(token, 6, f'/api/v1/pegasus-events71/get-events-by-event-block-id/{block_id}', params=params)
    return r


def delete_event_blocks_71_object(token, object_id):
    params = {"id": object_id}
    r = delete_request(token, 6, f'/api/v1/pegasus-events71/delete-item/{object_id}', params=params)
    return r


def create_event_blocks_79(token, point_id):
    data = {"description": "", "destinationPointId": point_id}
    r = post_request(token, 6, '/api/v1/event-blocks79/post-item', data=data)
    return r


def create_event_blocks_79_object(token, block_id, scanned_number):
    data = {"IsRouteValidationEnabled": False,
            "eventBlockId": block_id,
            "pointId": "07c5c96a-6f52-428d-9332-0004c296067e",
            "scannedNumber": scanned_number,
            "hostname": pth.random_name
            }
    r = post_request(token, 6, '/api/v1/pegasus-events71/post-item', data=data)
    return r


def get_address_by_id(token, address_id):
    params = {"id": address_id}
    r = get_request(token, 8, f'/api/v1/addresses/get-by-id/{address_id}', params=params)
    return r


def get_polygon_by_address_id(token, address_id):
    params = {"id": address_id}
    r = get_request(token, 8, f'/api/v1/geography/get-polygon-by-address-id/{address_id}', params=params)
    return r


def get_polygon_with_coordinate_by_address_id(token, address_id):
    params = {"id": address_id}
    r = get_request(token, 8, f'/api/v1/geography/get-polygon-with-coordinates-by-address-id/{address_id}',
                    params=params)
    return r

