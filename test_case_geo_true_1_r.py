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
        r = f.get_adress_by_id(tok, pth.correct_adress_id)
        r = json.loads(r.text)
        ok = r['ok']
        fail_message = r['metadata']
        assert ok and fail_message is None, 'wrong adress id'


if __name__ == "__main__":
    test_()

"""
Тест-кейс География 1: Получение адреса объекта по корректному id
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Запрос адреса по корректному id
        Результат: r['ok'] = true and r['metadata'] = None
"""