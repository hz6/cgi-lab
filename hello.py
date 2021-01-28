#!/usr/bin/env python3

import os
import json

# printing env var as text
# print('Content-type text/plain')
# print()
# print(os.environ["QUERY_STRING"])

# printing env var as json
print('Content-type application/json')
print()
print(json.dumps(dict(os.environ), indent=4))

# printing env var as html
# print('Content-type text/html')
# print()
# print(f'<p>{os.environ}</p>')
