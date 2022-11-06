# 13. Reverse the following list using for loop

List1 = [10,20,30,40]
revList = []
n = len(List1)

for i in range(n-1,-1,-1):
    revList.append(List1[i])
print(revList)