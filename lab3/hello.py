#!/usr/bin/env python3

import os
import json

env = {}

for env_key,env_value in os.environ.items():
    env[env_key] = env_value

# print("Content-Type: application/json")
# print()
# print(json.dumps((dict(env)), indent=2))

# print("Content-Type: text/html")
# print()
# print(f",p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>")


print("Content-Type: text/html")
print()
print(f",p>USER's BROWSER: {os.environ['HTTP_USER_AGENT']}</p>")