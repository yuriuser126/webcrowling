from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# pip install pyperclip
import pyperclip
from selenium.webdriver.common.keys import Keys
import time #시간 딜레이 사용가능

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 압축파일 푼걸 사용하겠다
# browser = webdriver.Chrome()#"./chromedriver.exe"
browser = webdriver.Chrome(options=chrome_options)#"./chromedriver.exe"

# 1.네이버 이동하면서 창이 닫힘
browser.get("http://naver.com")

# 2.로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()

# 3.id 입력
id = browser.find_element(By.CSS_SELECTOR,"#id")
id.click()

# 텍스트를 복사
pyperclip.copy("syuri5458")
# 복사한 아이디를 텍스트박스에 붙여넣기
browser.find_element(By.CSS_SELECTOR,"#id").send_keys(Keys.CONTROL,"v")

# 4.pw 입력
pw = browser.find_element(By.CSS_SELECTOR,"#pw")
pw.click() #텍스트박스 클릭

# 텍스트를 복사
pyperclip.copy("Ssyuri5458.!")
# 복사한 아이디를 텍스트박스에 붙여넣기
browser.find_element(By.CSS_SELECTOR,"#pw").send_keys(Keys.CONTROL,"v")

# 4.로그인 버튼 클릭
browser.find_element(By.ID,"log.login").click()

time.sleep(3)

mail = browser.find_element(By.CLASS_NAME,"MyView-module__item_text___VTQQM")
mail.click()

# 6.html정보출력
print(browser.page_source)

# 7.브라우저 종료
browser.close()
