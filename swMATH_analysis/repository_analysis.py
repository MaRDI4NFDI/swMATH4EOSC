# -*- coding: utf-8 -*-
import pandas
import requests

def final_xml2(de, api_source):

    headers = {'Accept': 'application/json'}
    r = requests.get(api_source + de, headers=headers)
    if r.status_code != 200:
        raise Exception(f"Unexpected response with status code {r.status_code}: {r.text}")
    json = r.json()
    # Bugfix as the sates are lists of lists which has no canonical XML mapping
    if type(json['result'])==dict: