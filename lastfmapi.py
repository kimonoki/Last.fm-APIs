import requests


username = 'USERNAME'
apikey = 'APIKEY'
url = 'http://ws.audioscrobbler.com/2.0'

params = dict(
    method='user.getrecenttracks',
    user=username,
    limit='1',
    api_key=apikey,
    format='json'
)


def album():
    resp = requests.get(url=url, params=params)
    album = resp.json()['recenttracks']['track'][0]['album']['#text']
    return album
