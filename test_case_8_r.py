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
        r = f.create_event_blocks_71(tok)
        assert r.status_code == 200, 'create_event_blocks_71 fail'

    with allure.step('step 2: '):
        r = json.loads(r.text)
        block_id = r['result']['number']
        assert block_id[0:3] == 'MOW', 'invalid block_id'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 8: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что номер полученного блока корректен
        Результат: number блока начинается с 'MOW'
"""