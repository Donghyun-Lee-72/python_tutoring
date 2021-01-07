# Donghyun/practice06.py
import math

######## CODES ########
def GuGu(multiplier):
    return [x*multiplier for x in range(1, 10)]


def sum_multiples(end, *numbers):
    arr = set()
    for num in numbers:
        arr = arr.union(filter(lambda x: x % num == 0, range(end)))
    return sum(arr)


def getTotalPage(m, n):
    return math.ceil(m / n)


def getTotalPage2(m, n):
    if m % n:
        return m // n + 1
    else:
        return m / n


def writeToFile():
    import sys

    option = sys.argv[1]

    if option == '-a':
        memo = sys.argv[2]
        f = open('memo.txt', 'a')
        f.write(memo)
        f.write('\n')
        f.close()
    elif option == '-v':
        f = open('memo.txt')
        memo = f.read()
        f.close()
        print(memo)


######## RUN ########
if __name__ == "__main__":
    # print(GuGu(2))
    # print(sum_multiples(1000, 3, 5))
    # print(getTotalPage(25, 10))
    # writeToFile()
    pass

