from utility import wait_for
from selenium.webdriver.common.keys import Keys

test_debug_login_enter_legend = ["Success","License Dialog is not Displayed","Validation code input missing","License Dialog failed to close"]

def test_debug_login_enter(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        validation_code = wait_for(state,browser,"validation_code")

        validation_code.send_keys("DEBUG")
        validation_code.send_keys(Keys.ENTER)
    
        wait_for_gone(state,browser,'license_input_dialog')

    except Exception as e:
        return state[0]

    return 0

test_debug_login_click_legend = test_debug_login_enter_legend

def test_debug_login_click(browser):
    state = [0]
    try:
        license_input_dialog = wait_for(state,browser,"license_input_dialog")
        validation_code = wait_for(state,browser,"validation_code")
        accept_license = wait_for(state,browser,"accept_license")

        validation_code.send_keys("DEBUG")
        accept_license.click()
    
        wait_for_gone(state,browser,'license_input_dialog')

    except Exception as e:
        return state[0]

    return 0