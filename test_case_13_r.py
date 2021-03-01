import requests
import json
import allure
import pytest

import paths as pth

import pegas_requests_functions as f


def test_():
    tok = f.get_token()
    with allure.step('step 0: '):
        assert tok != -1, 'get_token fail'

    r = f.create_event_blocks_79(tok, pth.destinationPointId_1202)
    with allure.step('step 1: '):
        assert r.status_code == 200, 'create_event_blocks_79 fail'

    r = json.loads(r.text)
    destination_point = r['result']['destinationPoint']['code']
    with allure.step('step 2: '):
        assert destination_point == '1202', 'invalid destinationPoint'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 13: Создание блока событий 79
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий 79
        Результат: Код 200
    Шаг 2: Проверка, что номер блок создан с корректным пунктом
        Результат: r['result']['destinationPoint']['code'] = '1202'
"""