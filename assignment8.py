# 8. Given a list iterate it and count the occurrence of each element and create a
# dictionary to show the count of each element

lst = [8, 7, 8, 0, 4, 4, 3, 9, 6, 3]
a = {}

for i in range(0, len(lst)):
    count = lst.count(lst[i])
    a[lst[i]] =count
    print(a)