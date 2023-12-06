#!/usr/bin/env python3
import csv, sys
from google.auth import default
from google.auth.transport.requests import AuthorizedSession

# configure these variables before running the script
project_id = 
agent_id = 
location = 

# Setup
displayName = sys.argv[1]
url_endpoint = (
    "https://"
    + location
    + "-dialogflow.googleapis.com/v3/projects/"
    + project_id
    + "/locations/"
    + location
    + "/agents/"
    + agent_id
    + "/entityTypes"
)
if len(sys.argv) == 3:
    url_endpoint = url_endpoint + "/" + sys.argv[2]

# Read csv file
entity_json = []
with open("synonyms.csv", mode="r", encoding="utf-8-sig") as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        each_entity_value = {}
        each_entity_value["value"] = line[0]
        each_entity_value["synonyms"] = line
        entity_json.append(each_entity_value)

# Download the service account json with the required permissions to call the cx agent
credentials = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])[0]
authed_session = AuthorizedSession(credentials)
response = None
if len(sys.argv) == 2:
    response = authed_session.post(
        url_endpoint,
        json={"displayName": displayName, "entities": entity_json, "kind": "KIND_MAP"},
    )
else:
    response = authed_session.patch(
        url_endpoint,
        json={"displayName": displayName, "entities": entity_json, "kind": "KIND_MAP"},
    )
print(response.text)
