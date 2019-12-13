import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.virustotal.com/vtapi/v2/domain/report'

params = {'apikey':'b391f7768eb1e671eba10424213c8a146500b9ff7cd67ad73d47335902c62e85','domain':'https://www.facebook.com'}

response = requests.get(url, params=params)
print(response.json())

