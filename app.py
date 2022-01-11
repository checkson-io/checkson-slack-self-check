import sys
import random

if random.random() > 0.5:
    print("Check successful")
    sys.exit(0)
else:
    print("Check unsuccessful")
    sys.exit(1)
