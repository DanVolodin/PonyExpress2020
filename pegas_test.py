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
    print('Step 1:', end=' ')
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
        print('not ok')
        driver.close()
        return 0
    else:
        print('ok')

    print('Step 2:', end=' ')
    element_login.send_keys(correct_login)
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
        print('not ok')
        driver.close()
        return 0
    else:
        print('ok')

    return driver


def test_case_1(driver_path):
    driver = log_in(driver_path)
    time.sleep(10)
    if driver == 0:
        return
    driver.close()


#def test_case_2():


if __name__ == "__main__":
    driver_path = ''
    test_case_1(driver_path)