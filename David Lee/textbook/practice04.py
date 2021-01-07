if __name__ == "__main__":
    # Q1: 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
    print("Q1")
    args = int(input("자연수 입력해: "))
    def is_odd(args):
        if args % 2 == 0:
            return 'even'
        if args % 2 == 1:
            return 'odd'
    print(is_odd(args))

    # Q2: 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
        # 평균 값을 구할 때 len 함수를 사용해 보자.
    print("Q2")
    def avg_many(*args):
        sum = 0
        for number in args:
            sum += number
        return sum / len(args)
    print(avg_many(1,3,5))

    # Q3:
    print("Q3")
    '''
    다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
    
    input1 = input("첫번째 숫자를 입력하세요:")
    input2 = input("두번째 숫자를 입력하세요:")
    
    total = input1 + input2
    print("두 수의 합은 %s 입니다" % total)

    이 프로그램을 수행해 보자.
    
    첫번째 숫자를 입력하세요:3
    두번째 숫자를 입력하세요:6
    두 수의 합은 36 입니다
    
    3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
    '''
    # int 함수를 사용해 보자.
    input1 = input("첫번째 숫자를 입력하세요:")
    input2 = input("두번째 숫자를 입력하세요:")

    total = int(input1) + int(input2)
    print("두 수의 합은 %s 입니다" % total)

    # Q4: 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
    print("Q4")
    '''
    print("you" "need" "python")
    print("you"+"need"+"python")
    print("you", "need", "python")
    print("".join(["you", "need", "python"]))
    '''
    print("you" "need" "python")
    print("you" + "need" + "python")
    print("you", "need", "python")
    print("".join(["you", "need", "python"]))

    # Q5
    print("Q5")
    '''
    다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
    
    f1 = open("test.txt", 'w')
    f1.write("Life is too short")
    
    f2 = open("test.txt", 'r')
    print(f2.read())
    
    이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
    '''
    f1 = open("../test.txt", 'w')
    f1.write("Life is too short")
    f1.close()

    f2 = open("../test.txt", 'r')
    print(f2.read())
    f2.close()

    # Q6: 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
        # (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
    print("Q6")


    # 07
    print("Q7")
    '''
    다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
    
    Life is too short
    you need java
    '''
    # replace 함수를 사용해 보자.
