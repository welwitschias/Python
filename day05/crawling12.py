from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def hollys_store(storeList):
    for pageNo in range(1, 6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' % pageNo
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')

        tag_tbody = soup.select_one('tbody')

        for store in tag_tbody.select('tr'):
            tds = store.select('td')
            storeLocation = tds[0].string
            storeName = tds[1].string
            storeAddress = tds[3].string
            storeCallNum = tds[5].string

            storeList.append([storeLocation,
                              storeName,
                              storeAddress,
                              storeCallNum])

    return print(storeList)


result = []
hollys_store(result)

print('==============================')
hollys_dataframe = pd.DataFrame(result, columns=(
    'storeLocation', 'storeName', 'storeAddress', 'storeCallNum'))
print(hollys_dataframe)

print('==============================')
hollys_dataframe.to_csv('day05/hollys.csv', mode='w', encoding='euc-kr', index=True)
