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
        r = f.create_event_blocks_79(tok, pth.destinationPointId_1202)
        assert r.status_code == 200, 'create_event_blocks_79 fail'

    with allure.step('step 2: '):
        r = json.loads(r.text)
        block_id = r['result']['id']
        destination_point = r['result']['destinationPoint']['code']
        assert destination_point == '1202', 'invalid destinationPoint'

    with allure.step('step 3: '):
        r = f.create_event_blocks_79_object(tok, block_id, pth.incorrect_79_block_num)
        assert r.status_code == 200, 'create_event_blocks_79_object fail'

    with allure.step('step 4: '):
        r = json.loads(r.text)
        fail_message = r['metadata']['message']
        assert fail_message == 'Отсутствует введенное место накладной', 'object created'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 14: Ввод несуществующего места в блок событий 79
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий 79
        Результат: Код 200
    Шаг 2: Проверка, что номер блок создан с корректным пунктом
        Результат: r['result']['destinationPoint']['code'] = '1202'
    Шаг 3: Добавление объекта с невалидным номером
        Результат: Код 200
    Шаг 4: Проверка, что объект не добавлен
        Результат: r['metadata']['message'] = 'Отсутствует введенное место накладной'
"""