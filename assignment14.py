# 14. Write a Python program to display all the prime numbers within a range

lower = int(input("Enter starting number: "))
upper = int(input("Enter ending number: "))

if upper < lower:
    print("Please give a proper input")
    raise SystemExit()
else:
    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
