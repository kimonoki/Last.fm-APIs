import requests
import argparse
import json

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



def main():
    parser = argparse.ArgumentParser(description='Fetch artist or album information from Last.fm')
    parser.add_argument('info_type', choices=['artist', 'album'], help='The type of information to fetch (artist or album)')

    args = parser.parse_args()

    lastfm_info = LastfmInfo(params, url)
    result = lastfm_info.get_lastfm_info(args.info_type)
    
    if result:
            jsonresult = {
            "items": [
                {
                    "title": result,
                    "arg": result 
                }
            ]
            }
            print(json.dumps(jsonresult))

    else:
        print("Failed to fetch the information.")

if __name__ == '__main__':
    main()