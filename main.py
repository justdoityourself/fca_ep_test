from orchestrate import orchestrate, orchestrate_many
from orchestrations import orchestrations
from utility import new_test,load_settings

import sys

if len(sys.argv) == 1:
    print("Run all tests:")

    for mode in orchestrations:
        settings = load_settings()
        print(settings)

        print("Initializing Driver...")
        browser = new_test(settings['driver'],settings['url'])

        for name, component in mode.items():
            print("Orchestrate: " + name)
            orchestrate_many(component,browser,settings)

        browser.quit()
else:
    #Run the specified tests
    args = sys.argv[1:]

    for name in args:
        print("Orchestrate: " + name)
        orchestrate(orchestrations[name])