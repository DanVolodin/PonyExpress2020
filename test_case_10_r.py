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
        block_number = r['result']['number']
        assert block_number[0:3] == 'MOW', 'invalid block_id'

    with allure.step('step 3'):
        block_id = r['result']['id']
        r = f.create_event_blocks_71_object(tok, block_id, pth.incorrect_71_block_num_1)
        assert r.status_code == 200, 'create_event_blocks_71_object fail'

    with allure.step('step 4: '):
        r = json.loads(r.text)
        object_ok = r['ok']
        fail_message = r['metadata']['message']
        assert not object_ok and \
               fail_message == f'Номер объекта не валидный: {pth.incorrect_71_block_num_1}', 'object not created'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 10: Проверка ввода некорректного номера накладной в блок событий "71. Прибыл на склад (без сортировки)"
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что полученный номер блока корректен
        Результат: number блока начинается с 'MOW'
    Шаг 3: Добавление объекта с некорректным номером "11-1111-1112"
        Результат: Код 200
    Шаг 4: Проверка статуса ответа и сообщения ошибки
        Результат: Статус r['ok'] = false и r['metadata']['message'] = 'Номер объекта не валидный: 11-1111-1112'
"""