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
    f.test_num(1)

    driver = login.log_in()

    time.sleep(wt)
    if f.driver_off(driver):
        return
    f.close_driver(driver)


if __name__ == "__main__":
    test_()

