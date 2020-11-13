import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from functions import ok
from functions import not_ok
from functions import step


def test_():
    f.test_num(1)

    tok = f.get_token()
    if tok == -1:
        return

    step(1)
    try:
        r = f.get_courier_by_id(tok, '359afb0c-b870-4610-9233-524db1d5a029')

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
        if r['result']['firstName'] != 'Евгений ' or r['result']['lastName'] != '(СТД) Бурлаченко':
            raise
    except:
        not_ok()
        return
    else:
        ok()


if __name__ == "__main__":
    test_()

