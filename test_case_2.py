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
        exit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[1]/div/div/div[2]/div/button[2]')))

        exit_button.click()

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
    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 2: Выход пользователя из системы
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать кнопку выхода в верхнем правом углу окна системы
        Результат: Пользователь вышел из системы, открылась страница «Вход в систему»
"""