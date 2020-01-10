from utility import xwait_for_then_click,wait_for_gone,wait_for,xwait_for
from selenium.common.exceptions import TimeoutException
import traceback
import xpath_objects
import time
from test_utility import add_youtube_video, return_to_library 

report_edit_timeline_legend = [
    "Success",
    "Library button not visible",
    "Library button not active",
    "Add Video not Visible",
    "Add Video link not Visible",
    "Ok not Visible",
]

def edit_timeline(browser):
    state = [0]
    try:

        #xwait_for_then_click(state,browser, xpath_objects.library_overlay_button)
        #time.sleep( 1 )
        #xwait_for(state,browser, xpath_objects.library_overlay_button_active)
        #time.sleep( 1 )

        add_youtube_video(browser,state,"https://www.youtube.com/watch?v=VsTDGy38lcY")
       
        time.sleep( 3 )

        xwait_for_then_click(state,browser, xpath_objects.practice_view_total_area)
        time.sleep( 1 )

        xwait_for_then_click(state,browser, xpath_objects.are_you_sure_pop_yes)
        time.sleep( 20 )

        xwait_for_then_click(state,browser, xpath_objects.stop_video_click_enywhare)
        time.sleep( 3 )

        xwait_for_then_click(state,browser, xpath_objects.play_button)
        time.sleep( 20 )

        xwait_for_then_click(state,browser, xpath_objects.stop_video_click_enywhare)
        time.sleep( 3 )

        xwait_for_then_click(state,browser, xpath_objects.section2_select_checkmark)
        time.sleep( 1 )

        xwait_for_then_click(state,browser, xpath_objects.play_button)
        time.sleep( 20 )

        xwait_for_then_click(state,browser, xpath_objects.stop_video_click_enywhare)
        time.sleep( 10 )

        xwait_for_then_click(state,browser, xpath_objects.open_r_a_p_menu)
        time.sleep( 2 )

        xwait_for_then_click(state,browser, xpath_objects.repetitions_4)
        time.sleep( 2 )

        xwait_for_then_click(state,browser, xpath_objects.speed_1_25)
        time.sleep( 2 )

        xwait_for_then_click(state,browser, xpath_objects.play_button)
        time.sleep( 10 )

        xwait_for_then_click(state,browser, xpath_objects.stop_video_click_enywhare)
        time.sleep( 5 )

        return_to_library(browser,state)


        #xwait_for_then_click(state,browser, xpath_objects.return_to_selection_view)
        #xwait_for_then_click(state,browser, xpath_objects.edit_video_button_3)
        #xwait_for_then_click(state,browser, xpath_objects.delete_video_icon)
        #xwait_for_then_click(state,browser, xpath_objects.delete_video_no)


        #xwait_for_then_click(state,browser, xpath_objects.edit_video_button_3)
        #xwait_for_then_click(state,browser, xpath_objects.delete_video_icon)
        #xwait_for_then_click(state,browser, xpath_objects.delete_video_yes)

        #print ("Add Remove Complete !")""
    
      
    except TimeoutException as e:
        return state[0]
    except Exception as e:
        print(e,traceback.format_exc())
        return state[0]
    
    return 0