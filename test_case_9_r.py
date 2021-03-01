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
        r = f.create_event_blocks_71_object(tok, block_id, pth.correct_71_block_num)
        assert r.status_code == 200, 'create_event_blocks_71_object fail'

    with allure.step('step 4: '):
        r = json.loads(r.text)
        post_ok = r['ok']
        assert post_ok, 'object not created'

    with allure.step('step 5'):
        object_id = r['result']['id']
        r = f.get_event_blocks_71_object(tok, block_id, object_id)
        assert r.status_code == 200, 'get_event_blocks_71_object fail'

    with allure.step('step 6: '):
        r = json.loads(r.text)
        find_ok = r['ok']
        assert find_ok, 'object not found'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 9: Проверка ввода корректного номера накладной в блок событий "71. Прибыл на склад (без сортировки)"
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что полученный номер блока корректен
        Результат: number блока начинается с 'MOW'
    Шаг 3: Добавление объекта с корректным номером "11-1111-1111"
        Результат: Код 200
    Шаг 4: Проверка, что нет ошибки добавления
        Результат: r['ok'] = true
    Шаг 5: Зпроса объекта по id
        Результат: Код 200
    Шаг 6: Проверка, что объект найден найден в списке объектов
        Результат: r['ok'] = true
"""