import requests
from secret import API_KEY

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
       "boxoffice/searchDailyBoxOfficeList.json")


def get_movie_audience(date, title):
    """날짜와 영화 제목을 받아 그날의 관객 수를 문자열로 돌려준다."""
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(url, params=params, timeout=10)
    movies = response.json()['boxOfficeResult']['dailyBoxOfficeList']

    for movie in movies:
        if movie['movieNm'] == title:
            audi = int(movie['audiCnt'])
            return f"{audi:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."


print(get_movie_audience("20260824", "오디세이"))
print(get_movie_audience("20260824", "호프"))
print(get_movie_audience("20260824", "없는영화"))