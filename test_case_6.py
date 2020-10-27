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
    f.test_num(6)

    driver = login.log_in()
    if f.driver_off(driver):
        return

    step(3)
    try:
        driver = f.click_menu_button(driver)
        if f.driver_off(driver):
            raise

        driver = f.click_service_button(driver)
        if f.driver_off(driver):
            raise

        driver = f.click_hosting_management_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(4)
    try:
        driver = f.click_editing_user_groups_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(5)
    try:
        driver = f.click_creating_group_button(driver)
        if f.driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(6)
    try:
        element_group_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input')))

        element_group_name.send_keys(pth.random_name)

        saving_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]')))

        saving_button.click()

        element_editing_user_groups_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/div/h1')))

        if element_editing_user_groups_page_heading.text != 'Редактирование групп пользователей':
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    step(7)
    try:
        if not f.check_group_created(driver, pth.random_name):
            raise

        if not f.check_group_existence(driver, pth.random_name):
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    step(8)
    try:
        marker_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span')))

        marker_button.click()

        delete_group_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]')))

        delete_group_button.click()

        element_deleting_group_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h4/span')))

        if element_deleting_group_heading.text != 'Удаление группы пользователей':
            raise

        delete_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]')))

        delete_button.click()

        if f.check_group_existence(driver, pth.random_name):
            raise
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
