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
    f.test_num(15)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_79_included_in_consolidation_page(driver, pth.destination_1)
        if f.driver_off(driver):
            raise
    except:
        return

    step(8)
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
        not_ok()
        return
    else:
        ok()

    step(9)
    try:
        driver = f._79_included_in_consolidation_full_screen_enter_number(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    time.sleep(wt)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

