#06-1 내가 프로그램을 만들 수 있을까? version 1
def gugu(n):
    result =[]
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result
#06-1 RUN
if __name__ == "__main__":
    print(gugu(2))


#06-2 3과 5의 배수 합하기
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
#06-2 RUN
if __name__ == "__main__":
    print(result)


#06-3 게시판 페이징하기
import math
def page(num):
    return math.ceil(num/10)

#06-3 RUN
if __name__ == "__main__":
    print(page(15))
    print(page(25))


#06-4 간단한 메모장 만들기
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()

memo = sys.argv[2]


#06-5 탭을 4개의 공백으로 바꾸기
if __name__ == "__main__":
