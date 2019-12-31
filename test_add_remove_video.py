from utility import xwait_for_then_click,wait_for_gone,wait_for,xwait_for
from selenium.common.exceptions import TimeoutException
import traceback
import xpath_objects
import time
from test_utility import add_youtube_video

report_add_video_library_legend = [
    "Success",
    "Library button not visible",
    "Library button not active",
    "Add Video not Visible",
    "Add Video link not Visible",
    "Ok not Visible",
]

def add_video_library(browser):
    state = [0]
    try:

        #xwait_for_then_click(state,browser, xpath_objects.library_overlay_button)
        #time.sleep( 1 )
        #xwait_for(state,browser, xpath_objects.library_overlay_button_active)
        #time.sleep( 1 )
       
        add_youtube_video(browser,state,"https://www.youtube.com/watch?v=VsTDGy38lcY")

        xwait_for_then_click(state,browser, xpath_objects.return_to_selection_view)
        xwait_for_then_click(state,browser, xpath_objects.edit_video_button_3)
        xwait_for_then_click(state,browser, xpath_objects.delete_video_icon)
        xwait_for_then_click(state,browser, xpath_objects.delete_video_no)


        xwait_for_then_click(state,browser, xpath_objects.edit_video_button_3)
        xwait_for_then_click(state,browser, xpath_objects.delete_video_icon)
        xwait_for_then_click(state,browser, xpath_objects.delete_video_yes)

        print ("Add Remove Complete !")
  
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0