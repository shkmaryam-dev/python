# 12. Given a list iterate it and display numbers which are divisible by 5 and if you find
# number greater than 150 stop the loop iteration

lst = [14, 25, 13, 20, 5, 1, 36, 7, 35, 150, 10]
for i in range(0,len(lst)):
    if lst[i] % 5 == 0:
        if lst[i] == 150:
            break
        else:
            print(lst[i])

