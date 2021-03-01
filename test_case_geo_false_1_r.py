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
        r = f.get_address_by_id(tok, pth.incorrect_adress_id)
        print(r)
        r = json.loads(r.text)
        ok = r['ok']
        fail_message = r['metadata']['message']
        assert not ok and fail_message == 'Object not found', 'wrong address id'


if __name__ == "__main__":
    test_()

"""
Тест-кейс География 2: Получение адреса объекта по некорректному id
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Запрос адреса по некорректному id
        Результат: r['ok'] = false and r['metadata']['message'] = 'Object not found'
"""