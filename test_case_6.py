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
    f.test_num(6)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    step(3)
    try:
        driver = f.click_menu_button(driver)
        if f.driver_off(driver):
            raise

        driver = f.click_service_button(driver)
        if f.driver_off(driver):
            raise

        driver = f.click_hosting_management_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(4)
    try:
        driver = f.click_editing_user_groups_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(5)
    try:
        driver = f.click_creating_group_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(6)
    try:
        element_group_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input')))

        element_group_name.send_keys(pth.random_name)

        saving_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]')))

        saving_button.click()

        element_editing_user_groups_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/div/h1')))

        if element_editing_user_groups_page_heading.text != 'Редактирование групп пользователей':
            raise
    except:
        not_ok()
        f.close_driver(driver)
        return
    else:
        ok()

    step(7)
    try:
        if not f.check_group_created(driver, pth.random_name):
            raise

        if not f.check_group_existence(driver, pth.random_name):
            raise
    except:
        not_ok()
        f.close_driver(driver)
        return
    else:
        ok()

    step(8)
    try:
        marker_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span')))

        marker_button.click()

        delete_group_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]')))

        delete_group_button.click()

        element_deleting_group_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h4/span')))

        if element_deleting_group_heading.text != 'Удаление группы пользователей':
            raise

        delete_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]')))

        delete_button.click()

        if f.check_group_existence(driver, pth.random_name):
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
Тест-кейс 6: Создание и удаление группы пользователей
    Шаг 1: В браузере открыть ссылку на вход с систему
        Результат: Открылась страница «Вход в систему» с полями для ввода логина и пароля
    Шаг 2: Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти»
        Результат: Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
    Шаг 3: Нажать последовательность кнопок «Menu» ->  «Сервис» -> «Управление» разрешениями»
        Результат: В выпавшем списке доступен пункт «Группы пользователей»
    Шаг 4: Выбрать пункт «Группы пользователей»
        Результат: Открылась форма «Редактирование групп пользователей»
    Шаг 5: Нажать кнопку «Создать новую»
        Результат: Открылась форма «Создание группы пользователей»
    Шаг 6: Ввести в поле «Название группы» непустое название группы и нажать кнопку «Сохранить»
        Результат: Система вернулась в на страницу «Редактирование групп пользователей»
    Шаг 7: Проверить, что система не вернула ошибку и созданная группа есть в списке групп
        Результат: Система нашла созданную группу в поиске
    Шаг 8: Удалить созданную группу
        Результат: Система не нашла созданную группу в поиске
"""