from utility import wait_for_then_click,wait_for_gone

report_bug_test_legend = [
    "Success",
    "Main Menu not visible",
    "Open settings menu item not visible"
]

def report_bug_test(browser):
    state = [0]
    try:
        wait_for_then_click(state,browser,"main_menu")
        wait_for_then_click(state,browser,"open_settings_menu_button")
        wait_for_then_click(state,browser,"open_bug_report_button")

        bug_comment_area = wait_for_then_click(state,browser,"bug_comment_area")
        bug_comment_area.send_keys("Report a Bug Test")

        wait_for_then_click(state,browser,"bug_report_send")
        wait_for_then_click(state,browser,"confirm_yes")

        wait_for_gone(state,browser,"bug_comment_area")
      
    except Exception as e:
        return state[0]
    
    return 0