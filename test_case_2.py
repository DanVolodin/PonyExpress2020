import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import login
import paths as pth
import functions as f
from functions import ok
from functions import not_ok
from functions import step


def test_():
    f.test_num(2)

    driver = login.log_in()
    if f.driver_off(driver):
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

    time.sleep(5)
    driver.close()


if __name__ == "__main__":
    logfile = open('logfile.txt', 'w')
    test_()