import requests
res = requests.get("http://google.com")
res.raise_for_status() #에러가 있다면 멈춰주고 에러를 알려준다.
print("응답코드:",res.status_code)#200이면 정상

# 크기 너무크면얼마나클지 보게 len 사용
# print(len(res.text)) #18058
print(res.text) #18058