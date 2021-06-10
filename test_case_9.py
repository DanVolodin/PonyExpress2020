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
        return

    try:
        driver = f._71_included_in_consolidation_enter_number(driver, pth.correct_71_block_num)
        if f.driver_off(driver):
            raise

        time.sleep(3)
        background_colour = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div')))
        background_colour = background_colour.get_attribute('style')
        if background_colour != 'background-color: rgb(124, 184, 47);':
            raise
    except:
        f.close_driver(driver)
        with allure.step('step 5: '):
            assert 0, 'fail step 5'

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 9: Проверка ввода корректного номера накладной в блок событий 71
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Производство»-> «Регистрация событий» -> 
    -> «71. Прибыл на склад (без сортировки)»
        Результат: Открылась форма «Ввод данных о блоке»
    Шаг 4: Нажать кнопку «Продолжить без курьера»
        Результат: Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
    Шаг 5: В поле ввода «Номер объекта» ввести текст «11-1111-1111» и нажать кнопку Enter
        Результат: Цвет блока изменился на rgb(124, 184, 47)
"""
