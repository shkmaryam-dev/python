# 6. Given an input list removes the element at index 4 and add it to the 2nd position
# and also, at the end of the list

lst = []
n = int(input("Enter value...."))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print("\n")
print(lst)

element = lst[4]
print(element)
lst.remove(lst[4])
lst.insert(1,element)
lst.insert(lst[-1],element)
print(lst)