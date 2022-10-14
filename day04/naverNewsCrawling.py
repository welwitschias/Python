import urllib.request
import datetime
import json

clientId = ""
clientSecret = ""


def getRequestUrl(url):  # url에 연결하는 함수
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", clientId)
    req.add_header("X-Naver-Client-Secret", clientSecret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success " % datetime.datetime.now())
        return response.read().decode('utf-8')
    except:
        return None


def getNaverSearch(node, srcText, start, display):  # json 형태의 데이터를 받아오는 함수
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    parameters = "?query=%s&start=%s&display=%s" % (
        urllib.parse.quote(srcText), start, display)
    url = base + node + parameters
    print(url)

    responseDecode = getRequestUrl(url)
    if (responseDecode == None):
        return None
    else:  # loads() : 성공 시 json 문자열을 python 객체로 리턴
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):  # 원하는 데이터를 추출하는 함수
    title = post['title']
    description = post['description']
    original_link = post['originallink']
    link = post['link']
    pubDate = post['pubDate']

    jsonResult.append({'cnt': cnt,
                       'title': title,
                       'description': description,
                       'original_link': original_link,
                       'link': link,
                       'pubDate': pubDate})


node = 'news'
srcText = '선거'
# srcText = input('검색어를 입력하세요')
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)
# print(jsonResponse)
total = jsonResponse['total']

while((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start']+jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 10)

print('전체 검색 : %d건' % total)

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4,
                          sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)

print('가져온 데이터 : %d건' % cnt)
print('%s_naver_%s.json Saved' % (srcText, node))
