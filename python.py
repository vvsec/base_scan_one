# -*- conding:UTF-8 -*-

import requests


url = 'https://www.aqniu.com/'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

req = requests.get(url = url,headers = header)

res = req.text

res = req.status_code

print(res)