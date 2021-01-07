#겨울프로젝트/JaeYong/practice06.py
import sys

class Jaeyong:
    def __init__(self):
        self.result = 0

    #Question 1
    def GuGu(self):
        gugu = int(input("Enter a natural number: "))
        hold = []
        i=1
        while i < 10:
            hold.append(gugu * i)
            i += 1
        return hold


    #Question 2
    def two(self):
        num = list(map(int, input("Enter two natural numbers less than 1000: ").split()))
        hold = 0
        for i in range(1, 1000):
            if i % 3 == 0 or i % 5 == 0:
                hold += i
        return hold

    #Question 3
    def three(self):
        total_posting = int(input("Enter the total number of postings: "))
        posting_number = int(input("Enter the number of postings per a page: "))
        if total_posting % posting_number == 0:
            return total_posting // posting_number
        else:
            return total_posting // posting_number + 1

    #Question 4
    def four(self):
        #책 06-4 코드 들고옴.
        option = sys.argv[1]
        # memo = sys.argv[2]

        if option == '-a':
            memo = sys.argv[2]
            f = open("memo.txt", "a")
            f.write(memo + "\n")
            f.close()
        elif option == '-v':
            f = open("memo.txt")
            memo = f.read()
            f.close()
            print(memo)

        #python practice06.py -a " "
        #python practice06.py -v

    def five(self):
        #책 06-5 코드 들고옴.
        src = sys.argv[1]
        dst = sys.argv[2]

        f = open(src)
        tab_content = f.read()
        f.close()

        space_content = tab_content.replace("\t", " "*4)

        f = open(dst, 'w')
        f.write(space_content)
        f.close()

        #python practice06.py memo.txt memo_space.txt

if __name__ == "__main__":
    Bestman = Jaeyong()
    # print(Bestman.GuGu())
    # print(Bestman.two())
    # print(Bestman.three())
    # Bestman.four()
    """
    import time
    time.sleep(3)
    for i in range(3,0,-1):
        time.sleep(1)
        print(i)
    time.sleep(1)
    print("Boom!")
    time.sleep(1)
    """
    Bestman.five()
