import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

moviestars = soup.select('#old_content > table > tbody > tr')
# print(moviestars)

for moviestar in moviestars:
    star_ranking = moviestar.select_one('td.ac > img')
    # print(star_ranking)
    star_name = moviestar.select_one('td.title > a')

    # print(star_name)
    # if star_ranking is not None and star_name is not None:
    if star_ranking is not None and star_name is not None:
        result = star_ranking['alt'] + " " + star_name.text
        # reuslt = star_ranking['alt'], star_name.text
        print(result)
