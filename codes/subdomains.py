import requests
url = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=lpu.in"
res = requests.get(url)
for x in res.json()['subdomains']:
	print(x)