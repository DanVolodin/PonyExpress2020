import time
from selenium import webdriver

import paths as pth


def open_page(num):
    driver = webdriver.Safari()
    driver.get(pth.urls[num] + pth.swagger_tail)
    return driver


if __name__ == "__main__":
    n = int(input())
    driver = open_page(n)