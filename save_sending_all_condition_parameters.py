import requests
import json

import pegas_requests_functions as f


def save_sending_all_condition_parameters():
    tok = f.get_token()
    r = f.get_sending_all_condition_parameters(tok)
    r = json.loads(r.text)
    condition_parameters = list()
    for parameter in r['result']:
        condition_parameters.append(parameter['code'])
    with open('sending_all_condition_parameters.txt', 'w') as file:
        json.dump(condition_parameters, file)


if __name__ == "__main__":
    save_sending_all_condition_parameters()