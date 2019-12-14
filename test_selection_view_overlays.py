from utility import xwait_for_then_click,wait_for_gone,wait_for
from selenium.common.exceptions import TimeoutException
import traceback
import xpath_objects

report_selection_view_overlays_legend = [
    "Success",
    "Library not visible",
    "Recommended not visible",
    "Search not Visible",
    "Total Practice not Visible",
    "History not Visible",
]

def selection_view_overlays_toggle(browser):
    state = [0]
    try:
        xwait_for_then_click(state,browser, xpath_objects.library_overlay_button)
        xwait_for_then_click(state,browser, xpath_objects.recommended_overlay_button)
        xwait_for_then_click(state,browser, xpath_objects.search_overlay_button)
        xwait_for_then_click(state,browser, xpath_objects.total_practice_overlay_button)
        xwait_for_then_click(state,browser, xpath_objects.history_overlay_button)
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0