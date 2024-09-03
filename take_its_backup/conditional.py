# Print "I'll learn." if day_of_week is saturday or sunday, else print "I'll practice."
day_of_week=input("Enter day of the week: ").lower()  #lower() ->coverting to lowercase, upper() -> converting to uppercase
print(day_of_week)

if day_of_week=="saturday" or day_of_week=="sunday":
    print("I'll learn.")
else:
    print("I'll practice.")


# Calculating based on choices
num1=int(input("Enter first number: "))  
num2=int(input("Enter second number: ")) 

choice=input("Enter the operation: (Options +, -, *, /, %)")
if choice=="+":
    sum=num1+num2
    print("Addition: ",sum)
elif choice=="-":
    diff=num1-num2
    print("Substraction: ",diff)
elif choice=="*":
    product=num1*num2
    print("Multiplication: ",product)
elif choice=="/":
    div=num1/num2
    print("Division: ",div)
elif choice=="%":
    remainder=num1%num2
    print("Remainder: ",remainder)
else:
    print("Invalid Choice")


