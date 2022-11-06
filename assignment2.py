# 2. Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

lst=[]
n=int(input("Enter the value....."))
for i in range(0,n):
    el = int(input())
    lst.append(el)

print("\n")
current = 0
sum = 0
for j in range(0,n):
    sum = sum+lst[current]
    print(sum)
    sum = lst[j]
    current = current+1

