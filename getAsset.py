import requests
import sys, json

if __name__ == '__main__':
    slug = sys.argv[1]
    headers = {"Accept": "application/json"}
    url = 'https://api.opensea.io/api/v1/collection/{}/stats'.format(slug)
    res = requests.get(url, headers)
    print(f'slug: {slug}, floor_price: {json.loads(res.text)['stats']['floor_price']}')

# url = "https://api.opensea.io/api/v1/asset/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/6987"

# response = requests.request("GET", url)

# print(response.text)