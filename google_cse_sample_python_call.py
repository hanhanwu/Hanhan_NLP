import json
import urllib
from pprint import pprint

base_url = 'https://www.googleapis.com/customsearch/v1?'
query = {
    'q': 'What happened to the promised ban?',
    'format': 'json',
    'cx': '[your Custom Search Engine id]',
    'key': '[your api key]',
    'num': 10,
    'siteSearch': 'http://www.theglobeandmail.com/opinion/*'
}

url = base_url + urllib.urlencode(query)
response = urllib.urlopen(url)
data = response.read()
quote = json.loads(data)
pprint(quote)


# I just need output urls
for elem in quote['items']:
  print elem['pagemap']['metatags'][0]['og:url']
