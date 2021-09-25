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

#usage LastfmInfo(params, url).get_lastfm_info('artist') or LastfmInfo(params, url).get_lastfm_info('album')
class LastfmInfo:
    def __init__(self, params,url):
        self.params = params
        self.url = url

    def __str__(self):
        return f'{self.params["user"]} - {self.params["api_key"]}'

    def get_lastfm_info(self, metadata):
        try:
            r = requests.get(url=self.url, params=self.params)
            return r.json()['recenttracks']['track'][0][metadata]['#text']
        except Exception as e:
            print(e)
            return None
