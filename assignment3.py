# 3.Given a string, display only those characters which are present at an even index number.

str = input("Enter String..")
n = len(str)
for i in range(0,n):
    if i % 2 != 0:
        print(str[i])