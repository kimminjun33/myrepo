import requests
import json
from secret import API_KEY

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
       "boxoffice/searchDailyBoxOfficeList.json")
params = {"key" : API_KEY, "targetDt": "20260824"}

response = requests.get(url, params=params, timeout=10)

data = response.json()
result = data['boxOfficeResult']
print(result.keys())


movies = result['dailyBoxOfficeList']

for movie in movies[:5]:
    rank = movie['rank']
    name = movie['movieNm']
    audi = int(movie['audiCnt'])
    print(f"{rank}위 {name} {audi:,}명")