import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


def web(browser):
    browser.fullscreen_window()
    # browser.get('https://ali.asiacommerce.net')
    browser.get('http://localhost:8080')


def login(browser):
    email = browser.find_element_by_xpath(
        "//input[@type='email']").send_keys("julioixc@gmail.com")
    password = browser.find_element_by_xpath(
        "//input[@type='password']").send_keys("123")
    browser.find_element_by_xpath("//button[@role='button']").click()


def catalog(browser):
    for i in range(20):
        card = browser.find_element_by_xpath(
            "//button[@class='ui green fluid button']")
        if(card is None):
            continue
        card.click()
    print("lanjut ke more")
    buttonMore = browser.find_element_by_xpath("//button[@pagination]").click()


browser = webdriver.Chrome("D:/mlabs/automation/chromedriver.exe")
web(browser)
login(browser)
time.sleep(20)
catalog(browser)
time.sleep(50)
browser.quit()
