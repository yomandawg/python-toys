# CSV(Comma Seperated Value : 콤마로 구분된 값(들)) => excel에서 쓸 수 있다. csv 아주 간단한 엑셀같음
# CSV 간단한 행과 열들이 많을 때 쓴다!
# 엑셀 파일 자체가 무겁기 떄문에 이거 편리하게 씀

# 이중배열처럼 할 수도 있어!
# list[0][1] 이런거처럼


import csv

## csv 쓰기
# f = open('sspy1.csv', 'w', encoding='utf-8') # 조작하는 환경을 f라는 임시변수에 저장하고 한다
# sspy1 = csv.writer(f)
# sspy1.writerow(["john", "john@hphkr.kr", "010123456789", "sspy1", "CS"]) #리스트를 넣겠다라고 생각해도 무방
# f.close()


## csv 읽기
# f = open('sspy1.csv', 'r', encoding='utf-8')
# sspy1 = csv.reader(f)
# for row in sspy1:
#     for d in row:
#         print(d)
# f.close()
## [["john", "john@hphkr.kr", "010123456789", "sspy1", "CS"]]

## csv 수정
f = open('sspy1.csv', 'a', encoding='utf-8') # 조작하는 환경을 f라는 임시변수에 저장하고 한다
sspy1 = csv.writer(f)
sspy1.writerow(["yoman", "yoman@hphkr.kr", "010987654321", "ashk", "LAW"]) #리스트를 넣겠다라고 생각해도 무방
f.close()