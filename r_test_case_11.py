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

    r = f.create_event_blocks_71(tok)
    with allure.step('step 1: '):
        assert r.status_code == 200, 'create_event_blocks_71 fail'

    r = json.loads(r.text)
    block_number = r['result']['number']
    with allure.step('step 2: '):
        assert block_number[0:3] == 'MOW', 'invalid block_id'

    block_id = r['result']['id']
    r = f.create_event_blocks_71_object(tok, block_id, pth.incorrect_71_block_num_2)
    with allure.step('step 3'):
        assert r.status_code == 200, 'create_event_blocks_71_object fail'

    r = json.loads(r.text)
    object_ok = r['ok']
    fail_message = r['metadata']['message']
    print(fail_message)
    with allure.step('step 4: '):
        assert not object_ok and \
               fail_message == '$_MARK_IS_NOT_BOUND_$', 'object not created'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 11: Проверка ввода непривязанной марки в блок событий "71. Прибыл на склад (без сортировки)"
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что полученный номер блока корректен
        Результат: number блока начинается с 'MOW'
    Шаг 3: Добавление объекта с непривязанной маркой "0012345666"
        Результат: Код 200
    Шаг 4: Проверка статуса ответа и сообщения ошибки
        Результат: Статус r['ok'] = false и r['metadata']['message'] = '$_MARK_IS_NOT_BOUND_$'
"""