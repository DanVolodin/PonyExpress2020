import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


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

"""
Тест-кейс 2: Проверка получения списка пяти курьеров с именами 'Максим'
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Получение списка данных о курьерах по имени (PageSize = 5, Search = 'Максим')
        Результат: Код 200
    Шаг 2: Проверка количества курьеров в списке(['result']['count'])
        Результат: Количество - 5
    Шаг 3: Проверка имен(['firstName']) всех курьеров из списка (['result']['items'])
        Результат: Имя - 'Максим'
"""