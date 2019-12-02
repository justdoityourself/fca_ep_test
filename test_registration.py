from utility import wait_for,wait_for_gone
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import traceback
from email_util import get_last_email_code

registration_legend_click = ["Success","License Dialog is not Displayed","Email Address input missing","License Dialog failed to close"]

def registration_test_click(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        email_address = wait_for(state,browser,"email_address")
        send_email = wait_for(state,browser,"send_email")

        validation_code = wait_for(state,browser,"validation_code")
        accept_license = wait_for(state,browser,"accept_license")

        email_address.send_keys("test@firstchairanalytics.com")
        send_email.click()
        email_code = get_last_email_code()

        validation_code.send_keys(email_code)
        accept_license.click()

    
        wait_for_gone(state,browser,'license_input_dialog')

    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]

    return 0
    
registration_legend_enter = registration_legend_click

def registration_test_enter(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        email_address = wait_for(state,browser,"email_address")
        send_email = wait_for(state,browser,"send_email")

        validation_code = wait_for(state,browser,"validation_code")



        email_address.send_keys("test@firstchairanalytics.com")
        send_email.send_keys(Keys.ENTER)
        email_code = get_last_email_code()

        validation_code.send_keys(email_code)
        validation_code.send_keys(Keys.ENTER)
    
        wait_for_gone(state,browser,'license_input_dialog')

    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]

    return 0








