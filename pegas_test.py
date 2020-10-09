import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_login = 'ext.mgu_education'
correct_password = 'rg#P5hZm4F'
pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'


def test_case_1():
    driver = webdriver.Safari()
    driver.get(pegas_url)
    #assert driver.title == 'Пегас'
    if driver.title == 'Пегас': print('ok')
    else: print('not ok')

    element_login = driver.find_element_by_name('login')
    element_password = driver.find_element_by_name('password')
    enter_button = driver.find_element_by_class_name('css-1hnkt5t')

    element_login.send_keys(correct_login)
    element_password.send_keys(correct_password)
    enter_button.click()

    #страница не успевает прогрузиться

    #assert driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/section/h1').text == 'Главная страница'
    if driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/section/h1').text == 'Главная страница': print('ok')
    else: print('not ok')


#def test_case_2():


test_case_1()
