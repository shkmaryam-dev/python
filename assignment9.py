# 9. Add a list of elements to a given set: {‘yellow’,’orange’} List:[blue,black]

str = {'Black' , 'Blue'}
lst = ['Green' , 'Yellow']

for i in range(0,len(lst)):
    str.add(lst[i])
    print(str)