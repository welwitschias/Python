from bs4 import BeautifulSoup
import requests

url = requests.get("https://tv.naver.com/r")
res = url.text
soup = BeautifulSoup(res, 'html.parser')

tv_rank = soup.find_all('dt', class_="title")

for i in range(len(tv_rank)):
    print((i+1), '위 :', tv_rank[i].get_text().strip())
