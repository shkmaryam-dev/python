#TODO : define a basic function
def func1():
    print("I am a function")
    
#TODO : fucntion that takes arguments
def func2(arg1,arg2):
    print(arg1, " " , arg2)
    
#TODO : function that returns a value
def cube(x):
    return x * x * x

#TODO : function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#TODO : function with variable number of argument

#func1() #function is being called directly , which exectues the content of the function,causing the print statement to print the string.
#print(func1()) #the function is also being called inside the print statement. so the o/p is the same as the first case. But then the outer print statement executes.and since out funciton doesn't return a result,
#print(func1) # the function is called itself is actually not being executed snce we're not including the parantheses. we're just printing the value of the function definition itself,which evaluted to this string right here. that represents the function object that we've defined so this demonstrated that function themselves are object that can be passed around the other pieces

# func2(10,20)
# print(func2(10,20))
# print(cube(3)) 

print(power(2))
print(power(2,3))