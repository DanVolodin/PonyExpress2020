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
    f.test_num(10)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_71_arrival_without_sort_page(driver)
        if f.driver_off(driver):
            raise
    except:
        return

    step(5)
    try:
        element_block_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))

        element_block_num.send_keys(pth.incorrect_71_block_num)
        element_block_num.send_keys('\n')

        element_warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/span')))

        if element_warning.text != 'Parameter HostName can not be empty':
            raise
        
        element_block = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div')))

        if element_block.get_attribute('style') != 'background-color: rgb(194, 48, 48);':
            raise
    except:
        not_ok()
        f.close_driver(driver)
        return
    else:
        ok()

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 10: Проверка ввода некорректного номера накладной в блок событий 71
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Производство» -> «Регистрация событий» -> 
    -> «71. Прибыл на склад (без сортировки)»
        Результат: Открылась форма «Ввод данных о блоке»
    Шаг 4: Нажать кнопку «Продолжить без курьера»
        Результат: Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
    Шаг 5: В поле ввода «Номер объекта» ввести текст «11-1111-1112» и нажать кнопку Enter
        Результат: Система вернула ошибку «Parameter HostName can not be empty» и цвет блока изменился
        на rgb(194, 48, 48)
"""
