import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import login
import paths as pth
from paths import wait_time as wt
import functions as f
from functions import ok
from functions import not_ok
from functions import step


def test_():
    f.test_num(13)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_79_included_in_consolidation_page(driver, pth.destination_1)
        if f.driver_off(driver):
            raise
    except:
        return

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 13: Создание блока событий 79
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Производство» -> «Регистрация событий» -> 
    -> «79. Включен в консолидацию»
        Результат: Открылась форма «Точка назначения»
    Шаг 4: Нажать кнопку «Выбрать»
        Результат: Открылась форма «Выберите точку назначения»
    Шаг 5: Ввести в поле ввода номер точки «1202»
        Результат: В таблице с точками отображается точка с введенным номером
    Шаг 6: Выбрать в таблице точку 1202 и нажать кнопку «Добавить»
        Результат: Открылась форма «Точка назначения» с выбранной точкой 1202
    Шаг 7: Нажать кнопку «Далее»
        Результат: Открылась форма «79. Включен в консолидацию» с номером созданного блока и точкой назначения 1202
"""
