import requests
from bs4 import BeautifulSoup

# 함수로 뉴스데이터 스크래핑-출력
def fetch_headlines():
    url = "https://news.naver.com/section/105"#네이버 IT/과학
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text,"html.parser")
    
    # 결과를 저장할 리스트
    news_headlines = []
    
    # 헤드라인 리스트 추출
    headline_items = soup.find_all("li",class_="sa_item _SECTION_HEADLINE")

    try:
        for item in headline_items:
            title_tag = item.find("a",class_="sa_text_title") #제목
            lede_tag = item.find("div",class_="sa_text_lede") #내용
            # info_tag = item.find("div",class_="sa_text_info_left") #출처
            info_tag = item.find("div",class_="sa_text_press") #출처

            if title_tag:
                title = title_tag.get_text #제목 추출
                title = title_tag.get_text(strip=True) #제목 추출
                link = title_tag["href"]#링크 추출
            else:
                title,link = None, None

            # lede = lede_tag.get_text #내용 추출
            lede = lede_tag.get_text(strip=True) #내용 추출
            # info = info_tag.get_text #출처 추출
            info = info_tag.get_text(strip=True) #출처 추출

            news_headlines.append({
                "title":title,
                "link":link,
                "lede":lede,
                "info":info,
            })
        return news_headlines
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청중 오류 발생{e}")
        return []

headlines = fetch_headlines()  
# 있으면 출력  
if headlines:
    print("헤드라인 뉴스")
    # 반복문 두개사용시 열거형 사용
    # 뉴스 1번부터 시작
    for idx,lines in enumerate(headlines, start=1):
        print(f"{idx}:{lines['title']}-{lines['info']}") #제목-출처
        print(f"링크:{lines['link']}") #링크
        print(f"내용:{lines['lede']}\n") #내용
        # 반복하면서 엔터
else:
    print("뉴스를 가져오지 못했습니다.")


