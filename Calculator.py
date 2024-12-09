num1=int(input("Enter The No. 1: "))
num2=int(input("Enter The No. 2: "))
Operator=input("Enter The Operator: ")
if Operator=='+':
    print(num1+num2)
elif Operator=='-':
    print(num1-num2)
elif Operator=='*':
    print(num1*num2)
elif Operator=='/':
    print(num1/num2)
elif Operator=='%':
    print(num1/num2)
else:
    print('Invalid operator')
    
