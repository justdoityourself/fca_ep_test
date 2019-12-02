from utility import wait_for_then_click,wait_for_gone,wait_for
from selenium.common.exceptions import TimeoutException
import traceback

report_selection_view_overlays_legend = [
    "Success",
    "Library not visible",
    "Recommended not visible",
    "Search not Visible",
    "Total Practice not Visible",
    "History not Visible",
]

def selection_view_overlay(browser):
    state = [0]
    try:
        wait_for_then_click(state,browser,"library_overlay")
        wait_for_then_click(state,browser,"recommended_overlay")
        wait_for_then_click(state,browser,"search_overlay")
        wait_for_then_click(state,browser,"total_practice_overlay")
        wait_for_then_click(state,browser,"history_overlay")
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0