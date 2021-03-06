import pytest
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import paths as pth
import functions as f
import login
from paths import wait_time as wt


def test_():
    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_71_arrival_without_sort_page(driver)
        if f.driver_off(driver):
            raise
    except:
        f.close_driver(driver)
        with allure.step('step 3: '):
            assert 0, 'fail step 3'

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 8: Создание блока событий 71 без курьера
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Производство»-> «Регистрация событий» -> 
    -> «71. Прибыл на склад (без сортировки)»
        Результат: Открылась форма «Ввод данных о блоке»
    Шаг 4: Нажать кнопку «Продолжить без курьера»
        Результат: Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
"""