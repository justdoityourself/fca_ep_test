from utility import wait_for,wait_for_gone
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import traceback

registration_legend = ["Success","License Dialog is not Displayed","Email Address input missing","License Dialog failed to close"]

def registration_test_click(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        email_address = wait_for(state,browser,"email_address")
        send_email = wait_for(state,browser,"send_email")

        email_address.send_keys("test@firstchairanalytics.com")
        send_email.click()
    
        wait_for_gone(state,browser,'license_input_dialog')

    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]

    return 0












