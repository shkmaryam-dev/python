# 4. Given a list of numbers, return True if first and last number of a list is same

lst = []
n = int(input("Enter value...."))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print("\n")
print(lst)
first = lst[0]
last = lst[n-1]
if first==last:
    print("true")
else:
    print("fasle")