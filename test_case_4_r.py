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
        assert not f.check_group_existence(tok, pth.random_name), 'group already exists'

    with allure.step('step 2: '):
        r = f.create_group(tok, pth.random_name)
        assert r.status_code == 200, 'create_group fail'

    with allure.step('step 3: '):
        assert f.check_group_existence(tok, pth.random_name), 'group not created'

    with allure.step('step 4: '):
        group_id = f.check_group_existence(tok, pth.random_name)
        r = f.delete_group(tok, group_id)
        assert r.status_code == 200, 'delete_group fail'

    with allure.step('step 5: '):
        assert not f.check_group_existence(tok, pth.random_name), 'group not deleted'


if __name__ == "__main__":
    test_()

"""
Тест-кейс 4: Добавление и удаление группы пользователей
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