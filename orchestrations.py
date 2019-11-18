from component_settings_dialog import settings_dialog
from component_license_dialog import license_dialog1, license_dialog2

full_mode1 = {
    "license_dialog":license_dialog1,
    "settings_dialog":settings_dialog
}

full_mode2 = {
    "license_dialog":license_dialog2,
    "settings_dialog":settings_dialog
}

orchestrations = [
    full_mode1,
    full_mode2
]