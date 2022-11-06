# 7. Given a list slice it into a 3 equal chunks and reverse each list

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
start = 0
end = len(lst)
step = 3
spllst = []
lst1 = []
lst2 = []
lst3 =[]
newList = []

for x in range(start, end ,step):
    spllst = lst[x:x+step]
    # print(spllst)
    newList.append(spllst)
    # print(newList)

lst1 = newList[0]
lst2 = newList[1]
lst3 = newList[2]
print("list 1 is " , lst1[::-1])
print("list 2 is " , lst1[::-1])
print("list 3 is " , lst1[::-1])