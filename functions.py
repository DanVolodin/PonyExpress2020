import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ok():
    with open('logfile', 'a') as logfile:
        logfile.write('ok\n')


def not_ok():
    with open('logfile', 'a') as logfile:
        logfile.write('not ok\n')


def step(n):
    with open('logfile', 'a') as logfile:
        s = '\t Step ' + str(n) + ': '
        logfile.write(s)


def test_num(n):
    with open('logfile', 'a') as logfile:
        s = 'Test ' + str(n) + '\n'
        logfile.write(s)


def driver_off(driver):
    return driver == 0


def click_menu_button(driver):
    try:
        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))

        menu_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_service_button(driver):
    try:
        service_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a')))

        service_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_hosting_management_button(driver):
    try:
        hosting_management_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a/div')))

        hosting_management_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_editing_user_groups_button(driver):
    try:
        editing_user_groups_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a')))

        editing_user_groups_button.click()

        element_editing_user_groups_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/div/h1')))

        if element_editing_user_groups_page_heading.text != 'Редактирование групп пользователей':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def click_creating_group_button(driver):
    try:
        creating_group_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]')))

        creating_group_button.click()

        element_creating_group_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_creating_group_heading.text != 'Создание группы пользователей':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def check_group_existence(driver, name):
    try:
        element_search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search-input"]')))

        element_search.send_keys(name)

        element_group_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')))

        if element_group_name.text != name:
            raise
    except:
        return False
    else:
        return True


def check_group_created(driver, name):
    try:
        element_warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/span')))

        if element_warning.text != ('UserProfileGroup already exists with "DisplayName": "' + name + '"'):
            raise
    except:
        return True
    else:
        return False


def click_production_button(driver):
    try:
        production_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/span/a')))

        production_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_event_registration_button(driver):
    try:
        event_registration_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span/a')))

        event_registration_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_71_arrival_without_sort_button(driver):
    try:
        _71_arrival_without_sort_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a')))

        _71_arrival_without_sort_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def open_71_arrival_without_sort_form(driver):
    try:
        click_menu_button(driver)
        if driver_off(driver):
            raise

        click_production_button(driver)
        if driver_off(driver):
            raise

        click_event_registration_button(driver)
        if driver_off(driver):
            raise

        click_71_arrival_without_sort_button(driver)
        if driver_off(driver):
            raise

        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])

        element_block_data_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_block_data_heading.text != 'Ввод данных о блоке':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def click_continue_without_courier_button(driver):
    try:
        continue_without_courier_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]')))

        continue_without_courier_button.click()

        page_arrival_without_sort_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[1]/h1')))

        if page_arrival_without_sort_heading.text != '71. Прибыл на склад (без сортировки)':
            raise

        element_block_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div')))

        if element_block_num.text == '':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def open_71_arrival_without_sort_page(driver):
    step(3)
    try:
        driver = open_71_arrival_without_sort_form(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    step(4)
    try:
        driver = click_continue_without_courier_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    return driver
