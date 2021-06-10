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
    try:
        driver = login.pony_driver_init()
        if f.driver_off(driver):
            return

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        f.close_driver(driver)
        with allure.step('step 3: '):
            assert 0, 'fail step 3'

    element_login.send_keys(pth.incorrect_login)
    time.sleep(1)  # иначе может вводить всё в одно поле
    element_password.send_keys(pth.incorrect_password)
    enter_button.click()
    try:
        warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-hnp1e7')))
        if warning.text != 'Неверный логин или пароль':
            raise
    except:
        f.close_driver(driver)
        with allure.step('step 4: '):
            assert 0, 'fail step 4'

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 3: Попытка входа несуществующего пользователя в систему
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя, не заведенный в системе, в поле для логина, произвольный непустой пароль
    пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Система вернула ошибку «Неверный логин или пароль»
"""