# 1. Given a two integer numbers return their product and  if the product is greater
# than 1000, then return their sum

a=input("Enter the value of a : ")
b=input("Enter the value of b: ")
mul=int(a)*int(b)
add=int(a)+int(b)
if(mul>1000):
    print("Addition of 2 value is : " +str(add))
else:
    print("Multiplication of 2 value is : " +str(mul))