from json import loads
from urllib.parse import urlencode
from urllib.request import urlopen
import time


def get_google_url(qt):
    base_url = 'https://www.googleapis.com/customsearch/v1?'
    query = {
        'q': qt,
        'format': 'json',
        'exactTerms': qt,
        'cx': '[your cse id]',
        'key': '[your google api key]',
        'siteSearch': 'http://www.theglobeandmail.com/opinion/*'
    }

    url = base_url + urlencode(query)
    response = urlopen(url)
    quote = loads(response.read().decode("utf-8"))
    if 'items' in quote.keys():
        for elem in quote['items']:
            if 'og:url' in elem['pagemap']['metatags'][0].keys():
                print(elem['pagemap']['metatags'][0]['og:url'])
            else:
                print('***** no url returned')
    else:
        print('***** no url returned')



def main():
    input_path = "[folder path]/output_quotes_1000_p2.txt"

    f = open(input_path)
    input_count = 0

    for q in f:
        time.sleep(1)
        input_count += 1
        print(input_count)
        get_google_url(q)

if __name__ == "__main__":
    main()
