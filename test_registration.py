from utility import wait_for,wait_for_gone
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import traceback

registration_legend = ["Success","License Dialog is not Displayed","Email Address input missing","License Dialog failed to close"]

def registration_test_(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        license_email_address = wait_for(state,browser,"license_email_address")
        send_email_address = wait_for(state,browser,"send_email_address")

        license_email_address.send_keys("email from andrew")
        send_email_address.click()
    
        wait_for_gone(state,browser,'license_input_dialog')

    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]

    return 0












