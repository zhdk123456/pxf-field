#!/usr/bin/python

import json
import sys

def getValueOrEmpty(data, key):
    try:
        return data[key]
    except (KeyError):
        return ""

bytes = sys.stdin.read()

idx = bytes.index('\t')
key = bytes[0:idx].strip()
value = bytes[idx+1:]

data = json.loads(value)

created_at = getValueOrEmpty(data, "created_at")
id_str = getValueOrEmpty(data, "id_str")
text = getValueOrEmpty(data, "text")
source = getValueOrEmpty(data, "source")

try:
    user_id = data["user"]["id"]
except:
    user_id = ""

try:
    user_location = data["user"]["location"]
except:
    user_location = ""

try:
    lat = data["coordinates"]["coordinates"][0]
except:
    lat = ""

try:
    lon = data["coordinates"]["coordinates"][1]
except:
    lon = ""

print "%s|%s|%s|%s|%s|%s|%s|%s|%s" % (key, created_at, id_str, text, source, user_id, user_location, lat, lon)


