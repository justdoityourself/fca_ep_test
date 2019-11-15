from selenium import webdriver
import traceback
import time
import json

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_debug_login3(browser):
    state = 1
    try:
        license_input_dialog = WebDriverWait(browser,5).until(
        EC.visibility_of_element_located((By.ID, "license_input_dialog")))

        validation_code = browser.find_element_by_id("validation_code")

        validation_code.send_keys("DEBUG")
        validation_code.send_keys(Keys.ENTER)
    
        state = 2
        license_input_dialog = WebDriverWait(browser,5).until(
        EC.invisibility_of_element_located((By.ID, "license_input_dialog")))

    except TimeoutException:
        return state

    return 0

def test_debug_login2(browser):
    state = 1
    try:
        license_input_dialog = WebDriverWait(browser,5).until(
        EC.visibility_of_element_located((By.ID, "license_input_dialog")))

        validation_code = browser.find_element_by_id("validation_code")
        accept_license = browser.find_element_by_id("accept_license")

        validation_code.send_keys("DEBUG")
        accept_license.click()
    
        state = 2
        license_input_dialog = WebDriverWait(browser,5).until(
        EC.invisibility_of_element_located((By.ID, "license_input_dialog")))

    except TimeoutException:
        return state

    return 0

def Report_Bug_test(browser):
        kabob_menu = browser.find_element_by_id("kabob_menu")
        settings = browser.find_element_by_id("settings")
        report_bug = browser.find_element_by_id("report_bug")
        comment_area = browser.find_element_by_id("comment_area")
        report_bug_send = browser.find_element_by_id("report_bug_send")

        kabob_menu.click()
        browser.implicitly_wait(2)

        Setting.click()
        browser.implicitly_wait(2)

        Report_bug.click()
        browser.implicitly_wait(2)

        comment_area.click()
        browser.implicitly_wait(2)
        comment_area.send_keys("Report a Bug Test")

        Report_bug_send.click()
        Print("Just sent report")

#Use 2 and 3
def test_debug_login(browser):
    license_input_dialog = browser.find_element_by_id("license_input_dialog")
    if not license_input_dialog.is_displayed():
        return 1 #1 == dialog wasn't open

    validation_code = browser.find_element_by_id("validation_code")
    accept_license = browser.find_element_by_id("accept_license")

    validation_code.send_keys("DEBUG")
    accept_license.click()

    browser.implicitly_wait(2)

    if license_input_dialog.is_displayed():
        return 2 #2 == dialog didn't close

    return 0 #0 == success

def clear_data(browser):
    #clear_database_button = browser.find_element_by_id("clear_database_button")
    #clear_database_button.click()
    #browser.implicitly_wait(10)
    
    return 0

def add_youtube_video(browser):
    return 0

def orchestrate(tests)
    try:
        success = 0
        fail = 0

        with open('settings.json') as config_file:
            settings = json.load(config_file)

        print("Initializing Driver...")
        browser = webdriver.Chrome(settings['driver'])
        browser.get = (Settings['url'])

        print("Loading Page...")
        time.sleep( settings['delay'] )

        for test in tests: 
            print("Running:" + test.method.__name__ + "...")
            r = test.method(browser)

            if not r: success+=1 
            else: fail += 1

        print("Results: Success {} Fail {}".format(success,fail))
        print('Closing...') 
        time.sleep( settings['delay_end'] )   

    except Exception as e:
        print(e,traceback.format_exc())
    finally:
        browser.quit()

full_test1 = [
    {   "method": clear_data  },
    {   "method": test_debug_login2 },
    {   "method": Report_Bug_test },
    {   "method": add_youtube_video }
]

full_test2 = [
    {   "method": clear_data  },
    {   "method": test_debug_login3 }
]

orchestrate(full_test1)
orchestrate(full_test2)