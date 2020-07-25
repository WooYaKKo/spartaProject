import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# **[**💻코드 ** 웹 스크래핑 02] ** 영화 제목을 가져오며 ** select / select_one**의 사용법을 익히기

# 태그 안의 텍스트를 찍고 싶을 땐 → 태그.text
# 태그 안의 속성을 찍고 싶을 땐 → 태그['속성']

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')
print(movies)
# print(movies)
# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    img_tag = movie.select_one('td.ac > img')
    a_tag = movie.select_one('td.title > div > a')
    td_tag = movie.select_one('td.point')
    # if a_tag is not None:
    #     print(a_tag.text)
    # if td_tag is not None:
    #     print(td_tag.text)

    if a_tag is not None and td_tag is not None:
        value = img_tag['alt'] + " " + a_tag.text + " " + td_tag.text
        value_width = img_tag['width'] + " " + a_tag.text + " " + td_tag.text
        # print(value)
        # print(value_width)
