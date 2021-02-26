import requests
import json
import allure

import paths as pth
from paths import urls

import pegas_requests_functions as f
from pegas_requests_functions import ok
from pegas_requests_functions import not_ok
from pegas_requests_functions import step


def test_():
    tok = f.get_token()
    with allure.step('step 0: '):
        assert tok != -1, 'get_token fail'

    with allure.step('step 1: '):
        assert not f.check_group_existence(tok, pth.random_name), 'group already exists'

    r = f.create_group(tok, pth.random_name)
    with allure.step('step 2: '):
        assert r.status_code == 200, 'create_group fail'

    with allure.step('step 3: '):
        assert f.check_group_existence(tok, pth.random_name), 'group not created'

    group_id = f.check_group_existence(tok, pth.random_name)
    r = f.delete_group(tok, group_id)
    with allure.step('step 4: '):
        assert r.status_code == 200, 'delete_group fail'

    with allure.step('step 5: '):
        assert not f.check_group_existence(tok, pth.random_name), 'group not deleted'


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
    Шаг 5: Проверка, что удаленной группы пользователей нет в списке
        Результат: Получили список групп, в котором нет группы с нашим именем
"""