num1=int(input("Enter first number: "))  #By default, it is string type. So change it to integer.
num2=int(input("Enter second number: "))  # TypeCasting-> conversion of one datatype into another

#check datatype
print(type(num1))
print(type(num2))

# Sum of given numbers
sum=num1+num2
print("Sum of two numbers:",sum)

# Difference of two numbers
diff=num1-num2
print("Difference of two numbers:",diff)

#Product of two numbers
product=num1*num2
print("Product of two numbers:",product)

#Division of two numbers
div=num1/num2
print("Division of two numbers:",div)