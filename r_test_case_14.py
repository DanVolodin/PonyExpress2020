import requests
import json
import allure
import pytest

import paths as pth

import pegas_requests_functions as f


def test_():
    f.test_num(9)

    tok = f.get_token()
    if tok == -1:
        return

    step(1)
    try:
        r = f.create_event_blocks_71(tok)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    r = json.loads(r.text)
    block_id = r['result']['id']

    step(2)
    try:
        if not block_id:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(3)
    try:
        r = f.create_event_blocks_71_object(tok, block_id, pth.correct_71_block_num)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    r = json.loads(r.text)
    object_status = r['ok']

    step(4)
    try:
        if not object_status:
            raise
    except:
        not_ok()
        return
    else:
        ok()


if __name__ == "__main__":
    test_()

"""
Тест-кейс 9: Проверка ввода корректного номера накладной в блок событий "71. Прибыл на склад (без сортировки)"
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что полученный id блока непустой
        Результат: id блока непустой
    Шаг 3: Добавление объекта с корректным номером "11-1111-1111"
        Результат: Код 200
    Шаг 4: Проверка статуса ответа
        Результат: Статус r['ok'] = true
"""