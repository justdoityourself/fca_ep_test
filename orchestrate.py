from utility import new_test,load_settings
import traceback
import time

def orchestrate(tests):
    try:
        success = 0
        fail = 0

        settings = load_settings()
        print(settings)

        print("Initializing Driver...")
        browser = new_test(settings['driver'],settings['url'])

        print("Loading Page...")
        time.sleep( settings['delay'] )

        for test in tests: 
            print("Running:" + test['method'].__name__ + "...")
            r = test['method'](browser)

            if 'legend' in test.keys():
                print(test['legend'][r])

            if not r: success+=1 
            else: fail += 1

        print("Results: Success {} Fail {}".format(success,fail))
        print('Closing...') 
        time.sleep( settings['delay_end'] )   

    except Exception as e:
        print(e,traceback.format_exc())
    finally:
        browser.quit()

def orchestrate_many(tests, browser,settings):
    try:
        success = 0
        fail = 0

        #settings = load_settings()
        #print(settings)

        #print("Initializing Driver...")
        #browser = new_test(settings['driver'],settings['url'])

        print("Loading Page...")
        time.sleep( settings['delay'] )

        for test in tests: 
            print("Running:" + test['method'].__name__ + "...")
            r = test['method'](browser)

            if 'legend' in test.keys():
                print(test['legend'][r])

            if not r: success+=1 
            else: fail += 1

        print("Results: Success {} Fail {}".format(success,fail))
        print('Closing...') 
        time.sleep( settings['delay_end'] )   

    except Exception as e:
        print(e,traceback.format_exc())