# week10_03.py

f = open(r"c:\202444040\sonhyeji02.txt", 'r')

# readlines() : 라인을 한꺼번에 읽어서 줄단위로 리스트를 만듦
lines = f.readlines()
# print(lines) : ['math, 10|kor, 20|eng, 30\n', 'math, 40|kor, 50|eng, 60\n']
for line in lines:
    print(line.strip())
 
# readline() : 한 줄씩 읽음
#while True:
#    line = f.readline()
#    if not line:
#        break
#    print(line.strip())

# read()를 쓴 경우
# data = f.read()
# print(data)

f.close()