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
    f.test_num(8)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    try:
        driver = f.open_71_arrival_without_sort_page(driver)
        if f.driver_off(driver):
            raise
    except:
        return

    time.sleep(5)
    f.close_driver(driver)


if __name__ == "__main__":
    test_()
