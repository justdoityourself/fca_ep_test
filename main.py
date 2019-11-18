from orchestrate import orchestrate
from orchestrations import orchestrations

import sys

if len(sys.argv) == 1:
    print("Run all tests:")
    for mode in orchestrations:
        for name, component in mode.items():
            print("Orchestrate: " + name)
            orchestrate(component)
else:
    #Run the specified tests
    args = sys.argv[1:]

    for name in args:
        print("Orchestrate: " + name)
        orchestrate(orchestrations[name])
