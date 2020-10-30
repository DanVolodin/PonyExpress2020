import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import login
import paths as pth
import functions as f
from paths import wait_time as wt
from functions import ok
from functions import not_ok
from functions import step


def test_():
    f.test_num(3)

    step(1)
    try:
        driver = login.pony_driver_init()
        if f.driver_off(driver):
            not_ok()
            return

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        not_ok()
        f.close_driver(driver)
        return
    else:
        ok()

    step(2)
    element_login.send_keys(pth.incorrect_login)
    time.sleep(1)  # иначе может вводить всё в одно поле
    element_password.send_keys(pth.incorrect_password)
    enter_button.click()
    try:
        warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-hnp1e7')))
        if warning.text != 'Неверный логин или пароль':
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
