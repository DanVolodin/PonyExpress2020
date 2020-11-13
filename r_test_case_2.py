import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from functions import ok
from functions import not_ok
from functions import step


def test_():
    f.test_num(2)

    tok = f.get_token()
    if tok == -1:
        return

    step(1)
    try:
        r = f.get_couriers(tok, 1, 5, 0, 'Максим')

        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    r = json.loads(r.text)

    step(2)
    try:
        if r['result']['count'] != 5:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(3)
    try:
        couriers_list = r['result']['items']
        for courier in couriers_list:
            if courier['firstName'] != 'Максим':
                raise
    except:
        not_ok()
        return
    else:
        ok()


if __name__ == "__main__":
    test_()