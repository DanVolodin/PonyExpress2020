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
    f.test_num(10)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_71_arrival_without_sort_page(driver)
        if f.driver_off(driver):
            raise
    except:
        return

    step(5)
    try:
        element_block_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))

        element_block_num.send_keys(pth.incorrect_block_num)
        element_block_num.send_keys('\n')

        element_warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/span')))

        if element_warning.text != 'Parameter HostName can not be empty':
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    time.sleep(wt)
    driver.close()


if __name__ == "__main__":
    test_()
