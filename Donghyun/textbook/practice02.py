# Question 1
if __name__ == "__main__":
    # 코드 작성
    국어 = 80
    영어 = 75
    수학 = 55
    avg = (국어 + 영어 + 수학) / 3
    print(avg)
    pass

# Question 2
if __name__ == "__main__":
    # 코드 작성
    # num = int(input("숫자를 입력해주세요: "))
    # print("짝수" if num % 2 == 0 else "홀수")

    num = 13
    if 13 % 2 == 0:
        print("짝수")
    else:
        print("홀수")
    pass

# Question 3
if __name__ == "__main__":
    # 코드 작성
    SSN = "881120-1068234"
    print(SSN.split("-"))
    pass

# Question 4
if __name__ == "__main__":
    # 코드 작성
    SSN = "881120-1068234"
    print(SSN[7])
    pass

# Question 5
if __name__ == "__main__":
    # 코드 작성
    a = "a:b:c:d"
    a = a.replace(":", "#")
    print(a)
    pass

# Question 6
if __name__ == "__main__":
    # 코드 작성
    a = [1, 3, 5, 4, 2]
    a.sort()
    a.reverse()
    print(a)
    pass

# Question 7
if __name__ == "__main__":
    # 코드 작성
    a = ['Life', 'is', 'too', 'short']
    b = " ".join(a)
    print(b)
    pass

# Question 8
if __name__ == "__main__":
    # 코드 작성
    a = (1, 2, 3)
    a = a + (4, )
    print(a)
    pass

# Question 9
if __name__ == "__main__":
    # 코드 작성
    a = dict()

    # choice 1
    a['name'] = 'python'
    # choice 2
    a[('a', )] = 'python'
    # choice 3: this would cause an error; bcuz given key is mutable(list).
    # a[[1]] = 'python'
    # choice 4
    a[250] = 'python'
    pass

# Question 10
if __name__ == "__main__":
    # 코드 작성
    a = {'A':90, 'B':80, 'C':70}
    print(a['B'])
    print(a.pop('B'))
    print(a)
    pass

# Question 11
if __name__ == "__main__":
    # 코드 작성
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    b = set(a)
    print(b)
    pass

# Question 12
if __name__ == "__main__":
    # 코드 작성
    a = b = [1, 2, 3]
    a[1] = 4
    print(b)
    print('id(a):', id(a), ", id(b):", id(b))
    # 이유: a와 b가 같은 객체이기 때문이다. 그 증거로, a와 b의 id가 일치한다
    pass