if __name__ == "__main__":
    # Q1: 다음 코드의 결과 값은?
    a = "Life is too short, you need python"

    if "wife" in a:
        print("wife")
    elif "python" in a and "you" not in a:
        print("python")
    elif "shirt" not in a:
        print("shirt")
    elif "need" in a:
        print("need")
    else:
        print("none")

    """
    정답: shirt
    """

    # Q2: while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
    # print(sum([num for num in range(1, 1001) if num % 3 == 0]))

    number = 0; sum = 0
    while number <= 1000:
        number += 1
        if number % 3 == 0:
            sum += number

    print(sum)

    # Q3: while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
    num = 1
    while num <= 5:
        print('*' * num)
        num += 1

    # Q4: for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
    for i in range(1, 101):
        print(i, end=" ")
        if i % 10 == 0:
            print()

    # Q5
    '''
    A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
    [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    for문을 사용하여 A 학급의 평균 점수를 구해 보자.
    '''
    grades = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    avg = 0
    for grade in grades:
        avg += grade / len(grades)
    print(avg)

    # Q6
    '''
    리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
    numbers = [1, 2, 3, 4, 5]
    result = []
    for n in numbers:
        if n % 2 == 1:
            result.append(n*2)
    위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
    '''
    result = [number*2 for number in range(1, 6) if number % 2]
    print(result)
