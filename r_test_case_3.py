import requests
import json

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


def test_():
    f.test_num(3)

    tok = f.get_token()
    if tok == -1:
        return

    step(1)
    try:
        r = f.get_sending_all_condition_parameters(tok)
        if r.status_code != 200:
            raise
    except:
        not_ok()
        return
    else:
        ok()

    r = json.loads(r.text)
    condition_parameters_1 = list()
    with open('sending_all_condition_parameters.txt', 'r') as file:
        condition_parameters_1 = json.load(file)
    condition_parameters_2 = list()
    for parameters in r['result']:
        condition_parameters_2.append(parameters['code'])

    step(2)
    try:
        if len(condition_parameters_1) != len(condition_parameters_2):
            raise
        for parameter in condition_parameters_2:
            if parameter not in condition_parameters_1:
                raise
    except:
        not_ok()
        return
    else:
        ok()


if __name__ == "__main__":
    test_()

"""
Тест-кейс 3: Проверка наличия всех параметров состояний отправления в базе
    Шаг 0: Получение токена
        Результат: Код 200
    Шаг 1: Получение списка параметров состояний отправления из базы 
        Метод: ConditionParameterViewModelIEnumerableOperationResult
        Результат: Код 200
    Шаг 2: Проверка, что список кодов(['result'][i]['code']) полученных параметров совпадает с исходным списком
        Результат: Одинаковые размеры списков, и все коды элементов полученного списка присутсвуют в исходном списке
"""