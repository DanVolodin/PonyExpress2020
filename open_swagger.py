import time
from selenium import webdriver

import paths as pth


def open_page(num):
    driver = 0
    if pth.browser == 'Safari':
        driver = webdriver.Safari()
    if pth.browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=pth.driver_path)
    if pth.browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=pth.driver_path)
    driver.get(pth.urls[num] + pth.swagger_tail)
    return driver


if __name__ == "__main__":
    n = int(input())
    driver = open_page(n)