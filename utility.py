from selenium import webdriver
import json

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def wait_for_then_click(state,browser,id)
    state[0] += 1
    r = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.ID, id)))
    r.click()

    return r

def wait_for(state,browser,id)
    state[0] += 1
    r = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.ID, id)))

    return r

def wait_for_gone(state,browser,id)
    state[0] += 1
    r = WebDriverWait(browser,5).until(EC.invisibility_of_element_located((By.ID, id)))

    return r

def new_test(driver,url):
    browser = webdriver.Chrome(driver)
    browser.get = (url)

    return browser

def load_settings:
    with open('settings.json') as config_file:
        settings = json.load(config_file)

    return settings