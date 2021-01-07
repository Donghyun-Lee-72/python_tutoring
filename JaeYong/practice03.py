if __name__ == "__main__":
    # Q1
    #shirt
    #need 가 안나오는 이유는, 윗줄이 else if 조건문에서 돌아갔기 때문이다.

    # Q2
    ''' for loop 으로 풀었을 때.
    
    add = 0
    for i in range(1, 1000):
        if i % 3 == 0:
            add = add + i
    print(add)
    '''
    add = 0
    i = 1
    while 0 < i < 1001:
        i += 1
        if i % 3 != 0:
            continue
        add = add + i
    print(add)

    # Q3
    a = '*'
    i = 0
    while i < 6:
        i += 1
        print(a * i + "\n")

    # Q4
    for a in range(101):
        print(str(a) + "\n")

    # Q5
    a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for grade in a:
        total = total + grade
    print(str(total/len(a)) + "\n")

    # Q6
    print([n*2 for n in range(1, 6) if n % 2 == 1])
