import requests

URL = 'https://www.naver.com'
response = requests.get(URL)
print(response)

# 크롤링할 때 필요
html_text = response.text
# print(html_text)
print(html_text.find('<h3 class="blind">'))
print(html_text.find('급'))