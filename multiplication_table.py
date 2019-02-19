number1 = 1
number2 = 1
total = 0


while total < 100:
    if total == (number1 * 10):
        number1 = number1 + 1
        number2 = 1
        total = 0

    while total < (number1 * 10):
        total = number1 * number2
        print("%d x %d = %d" %(number1, number2, total))
        number2 = number2 + 1

