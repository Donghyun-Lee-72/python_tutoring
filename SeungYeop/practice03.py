if __name__ == "__main__":
    # Q1 answer = shirt

    # Q2
    num = 0
    answer = 0
    while num <=1000:
        if num % 3 == 0:
            answer = answer + num
        num += 1

    print(answer)

    # Q3
    a = 1
    star = ""
    while a <= 5:
        star += "*"
        print (star)
        a += 1

    # Q4
    for i in range(101): print (i)

    # Q5
    list = [70,60,55,75,95,90,80,80,85,100]
    total = 0
    for i in list:
        total = total + i
print (total / len(list))
    # Q6
for n in [1,2,3,4,5]: if n% 2 ==1: print (n*2)

pass