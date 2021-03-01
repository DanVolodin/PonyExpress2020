import requests
import json
import allure
import pytest

import paths as pth

import pegas_requests_functions as f


def test_():
    with allure.step('step 0: '):
        tok = f.get_token()
        assert tok != -1, 'get_token fail'

    with allure.step('step 1: '):
        r = f.get_polygon_with_coordinate_by_address_id(tok, pth.incorrect_adress_id)
        r = json.loads(r.text)
        ok = r['ok']
        fail_message = r['metadata']['message']
        assert not ok and \
               fail_message == f'$_ADDRESS_NOT_FOUND_$ addressId:{pth.incorrect_adress_id}', 'wrong address id'


if __name__ == "__main__":
    test_()

"""
Тест-кейс География 4: Получение координат зоны объекта по некорректному id адреса
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Запрос координат зоны по некорректному id адреса
        Результат: r['ok'] = false and r['metadata']['message'] = '$_ADDRESS_NOT_FOUND_$'
"""