from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class ="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# 위키북스 도서만 추출해서 출력
h1_1 = soup.find('h1').string
print('방법1 :', h1_1)

h1_2 = soup.select_one('h1').string
print('방법2 :', h1_2)

# div 태그 안에 있는 h1을 선택
h1_3 = soup.select_one('div > h1').string
print('방법3 :', h1_3)

# id가 meigen인 div 태그 안에 있는 h1을 선택
h1_4 = soup.select_one('div#meigen > h1').string
print('방법4 :', h1_4)

print('==============================')
# select : 여러 개 가져올 때, select_one : 1개만 가져올 때
li_list = soup.select('div#meigen > ul.items > li')
print(li_list)

for i in li_list:
    print(i.string)
