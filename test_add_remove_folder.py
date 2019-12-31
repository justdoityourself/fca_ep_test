from utility import xwait_for_then_click,wait_for_gone,wait_for,xwait_for
from selenium.common.exceptions import TimeoutException
import traceback
import xpath_objects
import time

report_add_remove_folder_legend = [
    "Success",
    "Library not visible",
    "Recommended not visible",
    "Search not Visible",
    "Total Practice not Visible",
    "History not Visible",
]

def add_remove_folder(browser):
    state = [0]
    try:
        xwait_for_then_click(state,browser, xpath_objects.library_overlay_button)
        time.sleep( 1 )

        i = 0
        while i < 4:
            xwait_for_then_click(state,browser, xpath_objects.add_binder)
            time.sleep( 1 )
            xwait_for_then_click(state,browser, xpath_objects.add_binder_name_click)
            time.sleep( 1 )

            Add_binder = xwait_for(state,browser, xpath_objects.add_binder_mame)

            
            Add_binder.send_keys("binder" + str(i))
            time.sleep( 1 )

            xwait_for_then_click(state,browser, xpath_objects.add_binder_click_ok)
            time.sleep( 1 )
            i += 1

        i = 0
        while i < 4:
            xwait_for_then_click(state,browser, xpath_objects.open_binder)
            time.sleep( 1 )
            xwait_for_then_click(state,browser, xpath_objects.remove_binder)
            time.sleep( 1 )

            i += 1
        time.sleep( 3 )






        
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0