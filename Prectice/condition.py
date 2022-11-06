# Conditional Statement

def main():
    x = input("Enter the value of x : ")
    y = input("Enter the value of y : ")
   
    
#condiotnal flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x==y:
        result = "x is equal to y"
    else:
        result = "x is greater than y"
    print(result)
    
main()