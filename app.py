import sys
import os
import requests

URL = os.environ.get('FLAPPING_STATE_URL')

r = requests.get(URL)
r.raise_for_status()

state = r.json()['state']

if state:
    print("State is true, check successful")
    sys.exit(0)
else:
    print("State is false, check unsuccessful")
    sys.exit(1)
