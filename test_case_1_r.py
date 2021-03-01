import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


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

"""
Тест-кейс 1: Проверка получения верных данных о курьер с заданным id
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Получение данных о курьере по id
        Результат: Код 200
    Шаг 2: Проверка имени(['result']['firstName']) и фамилии(['result']['lastName']) курьера
        Результат: Имя - 'Евгений ', фамилия - '(СТД) Бурлаченко'
"""