# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:45:24 2022

@author: Andres
"""

import requests
import json
response = requests.get("https://api.openalex.org/works?filter=institutions.id:I173911158")
print(response.status_code)
data = response.text
parse_json = json.loads(data)
active_case = parse_json['results'][25]["title"]
print("Result:\n ", active_case)