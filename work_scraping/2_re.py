import re

p = re.compile("ca.e")

#정규식 사용중
def print_match(m):
 if m:
  print("m.group() :",m.group()) #일치하는 문자열을 반환한다. -> care
  print("m.string :",m.string) #입력받은 문자열을 반환한다. -> careless
  print("m.start() :",m.start()) #일치하는 문자열의 시작 index. -> 0
  print("m.end() :",m.end()) #일치하는 문자열의 끝 index. -> 4앞까지. +1됨됨
  print("m.span() :",m.span()) #일치하는 문자열의 시작, 끝 index. -> (0,4)

 else:
  print("매칭되지 않음") #일치하는 문자열을 반환한다.
  
#   함수를 만들고 파라미터 m을 보낸다
# match : 주어진 문자열의 처음부터 일치하는지 확인

# m = p.match("careless") 
# 1. p.match("careless") 
# m.group() : care
# m.string : careless
# m.start() : 0
# m.end() : 4
# m.span() : (0, 4)

# m = p.search("good care") 
# m.group() : care
# m.string : good care
# m.start() : 5
# m.end() : 9 -> 8에 +1된값값
# m.span() : (5, 9)
# print_match(m) 


lst = p.findall("good care cafe") 
print(lst)
# findall : 일치하는 모든것을 리스트 형태로 반환
# ['care', 'cafe']
