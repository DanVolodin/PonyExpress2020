import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


def test_():
    f.test_num(4)

    tok = f.get_token()
    if tok == -1:
        return

    step(1)
    try:
        group_id = f.check_group_existence(tok, pth.random_name)
        if group_id:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(2)
    try:
        r = f.create_group(tok, pth.random_name)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(3)
    try:
        group_id = f.check_group_existence(tok, pth.random_name)
        if not group_id:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(4)
    try:
        r = f.delete_group(tok, group_id)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(5)
    try:
        group_id = f.check_group_existence(tok, pth.random_name)
        if group_id:
            raise
    except:
        not_ok()
        return
    else:
        ok()


if __name__ == "__main__":
    test_()

"""
Тест-кейс 4: Добавление группы пользователей
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Проверка, что создаваемой группы пользователей нет в списке
        Результат: Получили список групп, в котором нет группы с нашим именем
    Шаг 2: Создание группы пользователей
        Результат: Код 200
    Шаг 3: Проверка, что группа пользователей появилась в списке
        Результат: Получили список групп, в котором есть группы с нашим именем
    Шаг 4: Удалили группу по ее id
        Результат: Код 200
    Шаг 1: Проверка, что удаленной группы пользователей нет в списке
        Результат: Получили список групп, в котором нет группы с нашим именем
"""