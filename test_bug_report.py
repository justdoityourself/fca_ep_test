from utility import wait_for_then_click,wait_for_gone,wait_for
from selenium.common.exceptions import TimeoutException
import traceback

report_bug_test_legend = [
    "Success",
    "Main Menu not visible",
    "Open settings menu button not visible",
    "Settings Dialog not Visible",
    "Bug Report dialog not Visible, Adding Comment",
    "Bug Report dialog not Visible, Clicking Send",
    "Confirmation dialog not visible, Clicking Yes",
    "Dialogs failed to close",
]

def report_bug_test(browser):
    state = [0]
    try:
        wait_for_then_click(state,browser,"main_menu")
        wait_for_then_click(state,browser,"open_settings_menu_button")
        wait_for_then_click(state,browser,"open_bug_report_button")

        bug_comment_area = wait_for(state,browser,"bug_comment_area")
        bug_comment_area.send_keys("Report a Bug Test")

        wait_for_then_click(state,browser,"bug_report_send")
        wait_for_then_click(state,browser,"confirm_yes")

        wait_for_gone(state,browser,"bug_comment_area")
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0