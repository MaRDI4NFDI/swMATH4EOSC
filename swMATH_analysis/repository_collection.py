# -*- coding: utf-8 -*-
import pandas
import requests
import numpy as np
with open('index_init.txt', 'r') as f:
    l = f.read()
    ind = max(l)
    f.close()

    for i in range(int(ind),42000):

        headers = {'Accept': 'application/json'}
        try:
            r = requests.get('https://api.zbmath.org/v1/software/_search?search_string=si%3A' + str(i), headers=headers)
            if r.status_code != 200:
                raise Exception(f"Unexpected response with status code {r.status_code}: {r.text}")
            json = r.json()
            # Bugfix as the sates are lists of lists which has no canonical XML mapping
            print(json['result'][0]['id'])
            with open('table_swMATH.csv', 'a') as f:
                f.write(','.join([str(json['result'][0]['id']), str(json['result'][0]['source_code']),'\n']))
                f.close()
            with open('index_init.txt', 'a') as f:
                f.write(str(i)+'\n')
                f.close()
        except:
            continue