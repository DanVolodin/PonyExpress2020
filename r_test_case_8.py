import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


def test_():
    f.test_num(8)

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


if __name__ == "__main__":
    test_()

"""
Тест-кейс 8: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Создание блока событий "71. Прибыл на склад (без сортировки)" без курьера
        Результат: Код 200
    Шаг 2: Проверка, что полученный id блока непустой
        Результат: id блока непустой
"""