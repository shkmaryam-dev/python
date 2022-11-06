# 11. calculate the sum of all number between 1 and given number

n = int(input("Enter value..."))
sum = 0

for i in range(1, n+1):
    sum = sum+i
print(sum)
