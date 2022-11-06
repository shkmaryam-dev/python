# 5. Given a two list. Create a third list by picking an odd-index element from the first
# list and even index elements from second.

lst = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
lst3 = []

n1 = len(lst)
n2 = len(lst2)

for i in range(0,n1):
    if i % 2 == 1:
        lst3.append(lst[i])

for j in range(0,n2):
    if j % 2 == 0:
        lst3.append(lst2[j])
print("List of odd and even element of list1 and list2 = " , lst3)

