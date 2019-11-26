from component_settings_dialog import settings_dialog
from component_license_dialog import license_dialog1, license_dialog2, license_dialog3, license_dialog4
from utility import delay_component60

full_mode1 = {
    "license_dialog":license_dialog1,
    "settings_dialog":settings_dialog
}

full_mode2 = {
    "license_dialog":license_dialog2,
    "settings_dialog":settings_dialog
}

full_mode3 = {
    "license_dialog":license_dialog3,
    "settings_dialog":settings_dialog
}

full_mode4 = {
    "license_dialog":license_dialog4,
    "settings_dialog":settings_dialog
}

delay = {
    "zdelay":delay_component60,
}


orchestrations = [
    full_mode1,
    #delay,
    full_mode2,
    #delay,
    full_mode3,
    delay,
    full_mode4,
    delay,
]