from component_settings_dialog import settings_dialog
from component_license_dialog import license_dialog1, license_dialog2, license_dialog3, license_dialog4
from component_selection_view_overlays import selection_view_overlays
from component_add_remove_video import add_video
from component_edit_timeline import edit_timeline_1
from component_edit_timeline_convert_to_markers import edit_timeline_convert_sections
from component_add_remove_folder import add_remove_folder_1
from utility import delay_component60

#test_debug_login_enter
full_mode1 = {
    "license_dialog":license_dialog3,
    "add folders":add_remove_folder_1,
    "add_video_library":add_video,
    "markers_to_section":edit_timeline_convert_sections,
    "edit_timeline":edit_timeline_1,
    #"settings_dialog":settings_dialog
   
}

#test_debug_login_click
full_mode2 = {
    "license_dialog":license_dialog2,
    "selection_view_overlays":selection_view_overlays,
    "settings_dialog":settings_dialog
}

#registration_test_click
full_mode3 = {
    "license_dialog":license_dialog3,
    "selection_view_overlays":selection_view_overlays,
    "settings_dialog":settings_dialog
}

#registration_test_enter
full_mode4 = {
    "license_dialog":license_dialog4,
    "settings_dialog":settings_dialog
}

delay = {
    "zdelay":delay_component60,
}
orchestrations = [
    full_mode1
]


orchestrations_old = [
    full_mode1,
    #delay,
    full_mode2,
    #delay,
    full_mode3,
    delay,
    full_mode4,
    delay,
]