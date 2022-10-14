from bs4 import BeautifulSoup

fp = open('day04/fruits-vegetables.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

# 아보카도 출력하기
print(soup.select_one('#ve-list > li:nth-of-type(4)').string)
print(soup.select('#ve-list > li[data-lo="us"]')[1].string)
print(soup.select('#ve-list > li.black')[1].string)
print(soup.select('ul#ve-list > li')[3].string)

cond = {
    'data-lo': 'us',
    'class': 'black'
}

print(soup.find("li", cond).string)
print(soup.find(id="ve-list").find("li", cond).string)
