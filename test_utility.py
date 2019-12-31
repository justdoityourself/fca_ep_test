from utility import xwait_for_then_click,wait_for_gone,wait_for,xwait_for
import xpath_objects
import time


def add_youtube_video(browser,state,video):
    xwait_for_then_click(state,browser, xpath_objects.add_video_library_overlay)
    time.sleep( 1 )

    xwait_for_then_click(state,browser, xpath_objects.add_video_youtube_link_click)
    time.sleep( 1 )
    xwait_for(state,browser, xpath_objects.add_video_dialog)
    time.sleep( 1 )

    Add_link = xwait_for(state,browser, xpath_objects.music_videoyoutube_link)

    Add_link.send_keys(video)

    time.sleep( 3 )

    xwait_for_then_click(state,browser, xpath_objects.add_video_library_ok)
    time.sleep( 1 )