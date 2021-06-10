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
        driver = f.open_79_included_in_consolidation_page(driver, pth.destination_1)
        if f.driver_off(driver):
            raise
    except:
        return

    try:
        full_screen_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[1]/div/button/span[2]')))

        full_screen_button.click()

        full_screen_form_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[1]/h4/span')))

        if full_screen_form_heading.text != 'Полноэкранный режим':
            raise
    except:
        f.close_driver(driver)
        with allure.step('step 8: '):
            assert 0, 'fail step 8'

    try:
        driver = f._79_included_in_consolidation_full_screen_enter_number(driver, pth.incorrect_79_block_num)
        if f.driver_off(driver):
            raise

        element_warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/span')))

        if element_warning.text != 'Parameter HostName can not be empty':
            raise

        element_block = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[2]/div')))

        if element_block.get_attribute('style') != 'background-color: rgb(194, 48, 48);':
            raise
    except:
        f.close_driver(driver)
        with allure.step('step 9: '):
            assert 0, 'fail step 9'

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

"""
Тест-кейс 15: Работа блока событий 79 в полноэкранном режиме
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Производство»-> «Регистрация событий» -> 
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
    Шаг 8: Нажать кнопку «Полноэкранный режим»
        Результат: Открывается окно с одним полем ввода
    Шаг 9: В поле «Ввод данных» ввести текст «99-9999-9999/999» и нажать Enter
        Результат: Система вернула ошибку «Parameter HostName can not be empty»
"""
