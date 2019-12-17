from component_settings_dialog import settings_dialog
from component_license_dialog import license_dialog1, license_dialog2, license_dialog3, license_dialog4
from component_selection_view_overlays import selection_view_overlays
from utility import delay_component60

#test_debug_login_enter
full_mode1 = {
    "license_dialog":license_dialog1,
    "settings_dialog":settings_dialog
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

#registration_test_enterS
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