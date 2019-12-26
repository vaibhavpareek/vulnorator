import requests
rt = requests.get("https://tools.dnsstuff.com/#dnsReport|type=domain&&value=lpu.in")
fp = open('check.html','w')
fp.write(rt.text)
fp.close()