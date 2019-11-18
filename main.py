from orchestrate import orchestrate
from orchestrations import orchestrations

import sys

if let(sys.argv) == 1:
    #Run all tests
    for name, component in orchestrations:
        print("Orchestrate: " + name)
        orchestrate(component)
else:
    #Run the specified tests
    args = sys.argv[1:]

    for name in args:
        print("Orchestrate: " + name)
        orchestrate(orchestrations[name])
