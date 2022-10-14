from bs4 import BeautifulSoup

html = """
    <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)

h1 = soup.html.body.h1
print('h1 :', h1)
print('h1 태그 제거 :', h1.string)
print('-'*50)

p1 = soup.html.body.p
print('p :', p1)
print('p 태그 제거 :', p1.string)
print('-'*50)

# p1.next_sibling → '\n' 선택됨
p2 = p1.next_sibling.next_sibling
print('p :', p2)
print('p 태그 제거 :', p2.string)
