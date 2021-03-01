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


def pony_driver_init():
    if pth.browser == 'Safari':
        driver = webdriver.Safari()
    if pth.browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=pth.driver_path)
    if pth.browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=pth.driver_path)
    driver.get(pth.pegas_url)
    try:
        title = WebDriverWait(driver, 10).until(
                EC.title_is('Пегас'))
    except:
        f.close_driver(driver)
        with allure.step('step 0: '):
            assert 0, 'fail step 0'
    else:
        return driver


def log_in():
    try:
        driver = pony_driver_init()
        if driver == 0:
            return 0

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        f.close_driver(driver)
        with allure.step('step 1: '):
            assert 0, 'fail step 1'

    element_login.send_keys(pth.correct_login)
    time.sleep(1) # иначе может вводить всё в одно поле
    element_password.send_keys(pth.correct_password)
    enter_button.click()
    try:
        main_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[1]/div/div/button/span/div')))
        if main_page_heading.text != 'ПЕГАС 2.0':
            raise

        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))
    except:
        f.close_driver(driver)
        with allure.step('step 2: '):
            assert 0, 'fail step 2'
    return driver

