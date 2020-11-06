import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import paths as pth


def ok():
    with open(pth.logfile, 'a') as logfile:
        logfile.write('ok\n')


def not_ok():
    with open(pth.logfile, 'a') as logfile:
        logfile.write('not ok\n')


def step(n):
    with open(pth.logfile, 'a') as logfile:
        s = '\t Step ' + str(n) + ': '
        logfile.write(s)


def test_num(n):
    with open(pth.logfile, 'w') as logfile:
        s = 'Test ' + str(n) + '\n'
        logfile.write(s)


def driver_off(driver):
    return driver == 0


def close_driver(driver):
    for d in driver.window_handles:
        driver.switch_to_window(d)
        driver.close()


def click_menu_button(driver):
    try:
        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))

        menu_button.click()
    except:
        close_driver(driver)
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
        close_driver(driver)
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
        close_driver(driver)
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
        close_driver(driver)
        return 0
    else:
        return driver


def click_creating_group_button(driver):
    try:
        time.sleep(1)
        creating_group_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]')))

        creating_group_button.click()

        element_creating_group_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_creating_group_heading.text != 'Создание группы пользователей':
            raise
    except:
        close_driver(driver)
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
        close_driver(driver)
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
        close_driver(driver)
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
        close_driver(driver)
        return 0
    else:
        return driver


def open_71_arrival_without_sort_form(driver):
    try:
        driver = click_menu_button(driver)
        if driver_off(driver):
            raise

        driver = click_production_button(driver)
        if driver_off(driver):
            raise

        driver = click_event_registration_button(driver)
        if driver_off(driver):
            raise

        driver = click_71_arrival_without_sort_button(driver)
        if driver_off(driver):
            raise

        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])

        element_block_data_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_block_data_heading.text != 'Ввод данных о блоке':
            raise
    except:
        close_driver(driver)
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
        close_driver(driver)
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
        close_driver(driver)
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


def click_79_included_in_consolidation_button(driver):
    try:
        _79_included_in_consolidation_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a')))

        _79_included_in_consolidation_button.click()
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def open_79_included_in_consolidation_form(driver):
    try:
        driver = click_menu_button(driver)
        if driver_off(driver):
            raise

        driver = click_production_button(driver)
        if driver_off(driver):
            raise

        driver = click_event_registration_button(driver)
        if driver_off(driver):
            raise

        driver = click_79_included_in_consolidation_button(driver)
        if driver_off(driver):
            raise

        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])

        element_form_destination_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_form_destination_heading.text != 'Точка назначения':
            raise
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def click_79_included_in_consolidation_choose_destination_button(driver):
    try:
        choose_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button')))

        choose_button.click()
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def _79_included_in_consolidation_search_destination(driver, destination):
    try:
        element_search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search-input"]')))

        element_search.send_keys(destination)
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def _79_included_in_consolidation_add_destination(driver):
    try:
        tick_box_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/label')))

        tick_box_button.click()

        add_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]')))

        add_button.click()
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def click_79_included_in_consolidation_next_button(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button')))

        next_button.click()
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def open_79_included_in_consolidation_page(driver, destination):
    step(3)
    try:
        driver = open_79_included_in_consolidation_form(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    step(4)
    try:
        driver = click_79_included_in_consolidation_choose_destination_button(driver)
        if driver_off(driver):
            raise

        time.sleep(1)
        element_choose_destination_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h4/span')))

        if element_choose_destination_heading.text != 'Выберите точку назначения':
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    step(5)
    try:
        driver = _79_included_in_consolidation_search_destination(driver, destination)
        if driver_off(driver):
            raise

        time.sleep(1)
        element_destination_number = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]')))

        if element_destination_number.text != destination:
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    step(6)
    try:
        driver = _79_included_in_consolidation_add_destination(driver)
        if driver_off(driver):
            raise

        element_form_destination_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_form_destination_heading.text != 'Точка назначения':
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    step(7)
    time.sleep(1)
    try:
        driver = click_79_included_in_consolidation_next_button(driver)
        if driver_off(driver):
            raise

        element_79_included_in_consolidation_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/section/div[1]/h1')))

        if element_79_included_in_consolidation_page_heading.text != '79. Включен в консолидацию':
            raise

        element_79_included_in_consolidation_page_destination_number = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div')))

        if element_79_included_in_consolidation_page_destination_number.text != destination:
            raise

        element_79_included_in_consolidation_page_block_number = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div')))

        if element_79_included_in_consolidation_page_block_number.text == '':
            raise
    except:
        not_ok()
        return 0
    else:
        ok()

    return driver


def _79_included_in_consolidation_enter_number(driver, block_num):
    try:
        element_block_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))

        element_block_num.send_keys(block_num)
        element_block_num.send_keys('\n')
    except:
        close_driver(driver)
        return 0
    else:
        return driver


def _79_included_in_consolidation_full_screen_enter_number(driver, block_num):
    try:
        element_block_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[4]/div/div[2]/div/div[2]/div/div/form/input')))

        element_block_num.send_keys(block_num)
        element_block_num.send_keys('\n')
    except:
        close_driver(driver)
        return 0
    else:
        return driver