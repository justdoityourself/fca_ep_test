from test_debug_login import test_debug_login_enter_legend, test_debug_login_enter, test_debug_login_enter_legend, test_debug_login_click
from test_registration import registration_legend_click, registration_test_click, registration_test_enter, registration_legend_enter

license_dialog1 = [
    {   "method": test_debug_login_enter, "legend": test_debug_login_enter_legend },
   
]

license_dialog2 = [
    {   "method": test_debug_login_click, "legend": test_debug_login_enter_legend }
]

license_dialog3 = [
    {   "method": registration_test_click, "legend": registration_legend_click },
    
]  

license_dialog4 = [
    {   "method": registration_test_enter, "legend": registration_legend_enter }
]
