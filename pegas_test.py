import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_login = 'ext.mgu_education'
correct_password = 'rg#P5hZm4F'
pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'

incorrect_login = 'abacaba'
incorrect_password = '0000'

random_name = 'fgnmkc123'


def ok():
    print('ok')


def not_ok():
    print('not ok')


def step(n):
    print('\t Step', n, end=': ')


def test_num(n):
    print('Test', n)


def driver_off(driver):
    return driver == 0


def pony_driver_init(driver_path):
    driver = webdriver.Safari()
    driver.get(pegas_url)
    try:
        title = WebDriverWait(driver, 10).until(
                EC.title_is('Пегас'))
    except:
        print('driver not ok')
        driver.close()
        return 0
    return driver


def log_in(driver_path):

    step(1)
    try:
        driver = pony_driver_init(driver_path)
        if driver == 0:
            return 0

        element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))

        element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    step(2)
    element_login.send_keys(correct_login)
    time.sleep(2) # иначе может вводить всё в одно поле
    element_password.send_keys(correct_password)
    enter_button.click()
    try:
        main_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/h1')))
        if main_page_heading.text != 'Главная страница':
            raise

        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))
    except:
        not_ok()
        driver.close()
        return 0
    else:
        ok()

    return driver


def click_menu_button(driver):
    try:
        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))

        menu_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_service_button(driver):
    try:
        service_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/span/a')))

        service_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_hosting_management_button(driver):
    try:
        hosting_management_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/span/a/div')))

        hosting_management_button.click()
    except:
        driver.close()
        return 0
    else:
        return driver


def click_editing_user_groups_button(driver):
    try:
        editing_user_groups_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]/a')))

        editing_user_groups_button.click()

        element_editing_user_groups_page_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section[2]/section/div/h1')))

        if element_editing_user_groups_page_heading.text != 'Редактирование групп пользователей':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def click_creating_group_button(driver):
    try:

        creating_group_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]')))

        creating_group_button.click()

        element_creating_group_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/h4/span')))

        if element_creating_group_heading.text != 'Создание группы пользователей':
            raise
    except:
        driver.close()
        return 0
    else:
        return driver


def check_group_existence(driver, name):
    try:
        element_search = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-input"]')))
        time.sleep(3)

        element_search.send_keys(name)
        time.sleep(3)

        element_group_name = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,
            '//*[@id="root"]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')))
        time.sleep(3)
        
        if element_group_name.text != name:
            raise
    except:
        driver.close()
        return False
    else:
        return True


def test_case_1(driver_path):
    test_num(1)

    driver = log_in(driver_path)

    time.sleep(10)
    if driver_off(driver):
        return
    driver.close()


def test_case_2(driver_path):
    test_num(2)

    driver = log_in(driver_path)
    if driver_off(driver):
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

    time.sleep(10)
    driver.close()


def test_case_3(driver_path):
    test_num(3)

    step(1)
    try:
        driver = pony_driver_init(driver_path)
        if driver_off(driver):
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
        driver.close()
        return
    else:
        ok()

    step(2)
    element_login.send_keys(incorrect_login)
    time.sleep(2)  # иначе может вводить всё в одно поле
    element_password.send_keys(incorrect_password)
    enter_button.click()
    try:
        warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-hnp1e7')))
        if warning.text != 'Неверный логин или пароль':
            raise
    except:
        not_ok()
        driver.close()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()


def test_case_5(driver_path):
    test_num(5)

    driver = log_in(driver_path)
    if driver_off(driver):
        return

    step(3)
    try:
        driver = click_menu_button(driver)
        if driver_off(driver):
            raise

        driver = click_service_button(driver)
        if driver_off(driver):
            raise

        driver = click_hosting_management_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(4)
    try:
        driver = click_editing_user_groups_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()


def test_case_6(driver_path):
    test_num(6)

    driver = log_in(driver_path)
    if driver_off(driver):
        return

    step(3)
    try:
        driver = click_menu_button(driver)
        if driver_off(driver):
            raise

        driver = click_service_button(driver)
        if driver_off(driver):
            raise

        driver = click_hosting_management_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(4)
    try:
        driver = click_editing_user_groups_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(5)
    try:
        driver = click_creating_group_button(driver)
        if driver_off(driver):
            raise
    except:
        not_ok()
        return
    else:
        ok()

    step(6)
    try:
        element_group_name =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input')))

        element_group_name.send_keys(random_name)

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
        if check_group_existence(driver, random_name) == False:
            raise
    except:
        not_ok()
        #driver.close()
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
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h4/span')))

        if element_deleting_group_heading.text != 'Удаление группы пользователей':
            raise

        delete_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]')))

        delete_button.click()

        if check_group_existence(driver, random_name):
            raise
    except:
        not_ok()
        #driver.close()
        return
    else:
        ok()

    time.sleep(10)
    driver.close()

if __name__ == "__main__":
    driver_path = ''
    #test_case_1(driver_path)
    #test_case_2(driver_path)
    #test_case_3(driver_path)
    #test_case_5(driver_path)
    test_case_6(driver_path)

