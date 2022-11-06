from operator import truediv


myint = 5
myfloat =13.2
mystr = "his is a string" #global variable
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydist = {"one" : 1, "two" : 2} #dictionary

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydist)

#re-declaring a varibale works
# myint = "abc"
# print(myint)

#to access a member of a swsuence type, use[]
# print(mylist[2])
# print(mytuple[1])

#use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2]) #skip the value of 2 and print the value 

#you can use slices to revere a sequence
# print(mylist[::-1]) #not  specified a start and value just simple add : : ad the location of statrt and end and -1 for reverse the value

#dicionaries are accessed via keys
# print(mydist["one"])
  
#ERROR : variables of different types cannot be combined
#print("string type" + 123) #it show the error of type conversion bw int to str 
#print("string type" + str(123)) #it convert int to str

#Global vs. local variables in functions
def someFunction():
    global mystr #this statement is print def value twice , & the reason is i'm affecting the global value(it's override the global value)
    mystr = "def" #local variable
    print(mystr) #calling local variable
    
someFunction()
print(mystr) #called gloable variable

del mystr #delete the variable
print(mystr) #showing error bcz we delete the variable 
      
