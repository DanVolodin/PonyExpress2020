import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_login = 'ext.mgu_education'
correct_password = 'rg#P5hZm4F'
pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'

incorrect_login = 'abacaba'
incorrect_password = '0000'


def ok():
    print('ok')


def not_ok():
    print('not ok')


def step(n):
    print('\t Step', n, end=': ')


def test_num(n):
    print('Test', n)


def pony_driver_init(driver_path):
    driver = webdriver.Safari()
    driver.get(pegas_url)
    try:
        title = WebDriverWait(driver, 10).until(
                EC.title_is('Пегас'))
    except:
        print('driver not ok')
        driver.close()
        return 0
    return driver


def log_in(driver_path):
    step(1)
    try:
        driver = pony_driver_init(driver_path)
        if driver == 0:
            return 0

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    step(2)
    element_login.send_keys(correct_login)
    time.sleep(2) # иначе может вводить всё в одно поле
    element_password.send_keys(correct_password)
    enter_button.click()
    try:
        main_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/h1')))
        if main_page_heading.text != 'Главная страница':
            raise

        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))

    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    return driver


def test_case_1(driver_path):
    test_num(1)
    driver = log_in(driver_path)
    time.sleep(10)
    if driver == 0:
        return
    driver.close()


def test_case_2(driver_path):
    test_num(2)
    driver = log_in(driver_path)
    if driver == 0:
        return

    step(3)
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
        not_ok()
        driver.close()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()


def test_case_3(driver_path):
    test_num(3)

    step(1)
    try:
        driver = pony_driver_init(driver_path)
        if driver == 0:
            return 0

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    step(2)
    element_login.send_keys(incorrect_login)
    time.sleep(2)  # иначе может вводить всё в одно поле
    element_password.send_keys(incorrect_password)
    enter_button.click()
    try:
        incorrect_data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-hnp1e7')))
        if incorrect_data.text != 'Неверный логин или пароль':
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()


def test_case_5(driver_path):
    test_num(5)
    driver = log_in(driver_path)
    if driver == 0:
        return

    step(3)
    try:
        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))

        menu_button.click()

        service_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a')))

        service_button.click()

        hosting_management_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a/div')))
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    step(4)
    hosting_management_button.click()
    try:
        editing_user_groups_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a')))

        editing_user_groups_button.click()

        editing_user_groups_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/div/h1')))

        if editing_user_groups_page_heading.text != 'Редактирование групп пользователей':
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()


if __name__ == "__main__":
    driver_path = ''
    test_case_1(driver_path)
    test_case_2(driver_path)
    test_case_3(driver_path)
    test_case_5(driver_path)

