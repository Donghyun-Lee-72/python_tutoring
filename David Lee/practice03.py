if __name__ == "__main__":
    # Q1
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

    # Q2
    number = 0
    sum = 0
    while number < 1000:
        number = number + 1
        if number % 3 == 0:
            sum = sum + number
        print(sum)

    # Q3
    a = 1
    star = ""
    while a <= 5:
        star += "*"
        print(star)
        a += 1

    # Q4
    for i in range(1,101):
        print(i)
        i += 1

    # Q5
    grades = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    avg = 0
    for grade in grades:
        avg += grade / len(grades)
    print(avg)

    # Q6
    number = [1,2,3,4,5]
    result = [num * 2 for num in number if num % 2 == 1]
    print(result)
    pass