import requests
from bs4 import BeautifulSoup

url = "https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

response = requests.get(url)

# 코드 200이면 텍스트형식 출력
# 문제생기면 문제상태코드 그대로 출력
if response.status_code == 200:
    html=response.text
    # 파싱할거다 soup가 골라서 긁어올거다.
    #lxml 파싱할때 사용가능(install 해줘야함- pip install lxml)
    # 'html.parser'자리에 쓰면됨
    soup = BeautifulSoup(html,'html.parser')
    ul=soup.select_one("ul.basic1")
    titles = ul.select("li > dl > dt > a")
    # 제목에 있는 텍스트 읽어서 for문으로 몽땅가져온다
    for title in titles:
        print(title.get_text())
else:
    print(response.status_code)


