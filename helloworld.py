import requests
url = "http://hangang.dkserver.wo.tc/"
res = requests.get(url)

print(res.status_code)
print(res.text)