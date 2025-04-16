import requests
import csv
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "코스피_시가총액1-50_05.csv"
# f =open(filename,"w",encoding="utf-8")
# encoding="utf-8-sig" 엑셀에서 열때 한글깨짐 방지
# f =open(filename,"w",encoding="utf-8-sig")
# newline="" 엔터방지
f =open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)


# 타이틀 넣기전에 컬럼먼저 넣기
# title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실"
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
print(type(title))
writer.writerow(title)


# for page in range(1,3): #(1~2페이지 1위-100위)
for page in range(1,2):
    # res = requests.get(url+page)
    res = requests.get(url+str(page))
    # 문제있으면 에러코드
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"html.parser")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows :
        columns = row.find_all("td")
        # print("@# =>len",len(columns))
        # len(columns) ==1: 의미없는 데이터는 skip
        if len(columns) ==1: 
            continue
        # data = [column.get_text() for column in columns]
        # strip() : \n, \t제거
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)