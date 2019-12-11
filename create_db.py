#!/bin/python3

import json

# https://www.abgeordnetenwatch.de/api/parliament/bundestag/constituencies.json
with open('constituencies.json', 'r') as f:
    data = f.read()
constituencies = json.loads(data)

# https://www.abgeordnetenwatch.de/api/parliament/bundestag/deputies.json
with open('deputies.json', 'r') as f:
    data = f.read()
deputies = json.loads(data)

postcodes = {}

for c in constituencies['constituencies']:
    areacodes = {x["code"]: {"uuid": c["uuid"]} for x in c["areacodes"]}
    postcodes.update(areacodes)

with open('postcodes.json', 'w+') as f:
    f.write(json.dumps(postcodes))

profile_data = {d["constituency"]["uuid"]:
        {"first_name": d["personal"]["first_name"],
         "last_name": d["personal"]["last_name"],
         "degree": d["personal"]["degree"],
         "picture_url": d["personal"]["picture"]["url"],
         "party": d["party"]}
        for d in deputies["profiles"]
        if d["constituency"] and d["constituency"]["uuid"]}

with open('profile_data.json', 'w+') as f:
    f.write(json.dumps(profile_data))
