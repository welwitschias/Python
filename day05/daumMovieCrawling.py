from bs4 import BeautifulSoup
import requests

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 방법 1
title = soup.select(
    '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > strong > a')

grade = soup.select(
    '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span .txt_grade')

reserv = soup.select(
    '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span .txt_num')

for i in range(len(title)):
    print('제목 : ', title[i].string)
    print('평점 : ', grade[i].string)
    print('예매율 : ', reserv[i].string)
    print()

print('==============================')
# 방법 2
movieList = soup.find('ol', class_="list_movieranking")
rankcont = movieList.find_all('div', class_="thumb_cont")

for i in rankcont:
    movieTitle = i.find('a', class_="link_txt").get_text()
    movieGrade = i.find('span', class_="txt_grade").get_text()
    movieReserv = i.find('span', class_="txt_num").get_text()

    print('제목 :', movieTitle)
    print('평점 :', movieGrade)
    print('예매율 :', movieReserv)
    print()
