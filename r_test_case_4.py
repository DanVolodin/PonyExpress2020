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
    Шаг 1: Получение списка параметров состояний отправления из базы 
        Метод: ConditionParameterViewModelIEnumerableOperationResult
        Результат: Код 200
    Шаг 2: Проверка, что список кодов(['result'][i]['code']) полученных параметров совпадает с исходным списком
        Результат: Одинаковые размеры списков, и все коды элементов полученного списка присутсвуют в исходном списке
    Шаг 3:
        Результат:
    Шаг 4:
        Результат:
"""