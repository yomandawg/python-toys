##open('파일명', '뭘할지', '[인코딩]') #requires two inputs 'file name', 'what you're going to do'

f = open('names.txt', 'a', encoding="utf-8")
#f.write('김영준')
#print(f.read())
f.write('\n김탁희')
f.close

##영구적(손실없이)으로 데이터 저장할때.

# .txt 파일 연다
# 1. 읽기 'r' 'read'
# 2. 쓰기 'w' 'write'
# 3. 수정 'a' 'append'
# 파일 닫는다

# .json 파일 연다 (import json) => dictionary // json 모듈 활용해서 간다
# 1. 읽기 'read'
# 2. 쓰기 'write'
# 3. 수정 'append'
# 파일 닫는다

# .csv 파일 연다 (import csv) => 2d-list
# 1. 읽기 'read'
# 2. 쓰기 'write'
# 3. 수정 'append'
# 파일 닫는다

# with 키워드 활동 -> 코드를 간결하게

# DB 열다(CONNECT) -> CRUD OP.
# 1. 읽기(CREATE)
# 2. 쓰기(READ/RETRIEVE)
# 3. 수정(UPDATE)
# 4. 삭제(DELETE/DESTROY)
#DB 닫는다(disconnect)


# dictionary -> key-value + 강력한 메소드 추가 = (object)
# 관계형 DB에서 연결해준다고 해서 ORM이라부름 // 현대 프로그램에서 매우 중요함 SQL에서 도메인을 써야지만 DB를 다룰 수 있었지만 이제 ORM에서 바로 접근 가능
# 테크면접에서 ORM많이 물어본다! => 개발 제대로하게되면 안쓸수가없다, 개발에 대해 알고 있냐!