import requests
import json
import allure
import pytest

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


def test_():
    tok = f.get_token()
    with allure.step('step 0: '):
        assert tok != -1, 'get_token fail'

    r = f.create_event_blocks_71(tok)
    with allure.step('step 1: '):
        assert r.status_code == 200, 'create_event_blocks_71 fail'

    r = json.loads(r.text)
    block_id = r['result']['number']
    with allure.step('step 2: '):
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