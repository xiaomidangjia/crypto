
# coding: utf-8
#!/usr/bin/python
import urllib
from urllib import request
import requests
import base64



test_data_1 = {
    "type":"kong",
    "date":'2022-11-27'
    }

req_url = "http://172.23.198.69:80/crypto_pre"
r = requests.post(req_url, data=test_data_1)
print(r.content.decode('utf-8'))

#print(r)




