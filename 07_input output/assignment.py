#1.
a=input("enter your name: ")
print(f"your name is {a}")
#2.
b=input("enter your city name: ")
print("your city name is ",b)
#3.
c=input("enter your name: ")
d=int(input("enter your age: "))
print(f"your name is {c} and you are {d} years old.")
#4.
# str is returned always by default.
#5.
e=input("enter any data ")
print(type(e))
#6.
first_name=input("Enter your first name")
last_name=input("Enter your last name")
print(f"{first_name} {last_name}")
#7.
name=input("Enter your full name")
city=input("Enter your city name")
college=input("Enter your college name")
print(f"you are {name} from {city} studies in {college}")
#8.
first_name,last_name=input("Enter your first name and last name: ").split()
print(f"First Name: {first_name} Last Name: {last_name}")
#9.
var1,var2=input("Enter 2 words").split()
print(f"the first word is {var1} and the second word is {var2}.")
#10.
word1,word2,word3=(input("enter three words")).split()
print(f"the first word is {word1} the second word is {word2} and the third word is {word3}")
#11.
a=int("25")
print(type(a))
#12.
b=float("25.5")
print(type(b))
#13.
c=str(100)
print(type(c))
#14.
d=int(input("Enter any number"))
print(type(d))
#15.
e=float(input("Enter any decimal number"))
print(type(e))
#16.
#Because when we take any input from user the data taken is always in string value
# by default thus when we add 2 input values instead of addition it shows string concatenation.
#17.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
#18.
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")
#19.
a = 10
b = 20
print(f"the sum of both the variables are {a+b}")
#20.
name=input("Enter your name: ")
age=int(input("Enter your Age: "))
print(f"My name is {name} and i am {age} Years old.")
#21.
x=float(input("Enter the price: "))
print(f"The price od the product is {x:.2f}")
#22.
#The purpose of :.2f is to show you the float value by rounding it off to nearby 2 values.
#23.
product_name=input("Enter the Name of the Product: ")
price=float(input("Enter the price: "))
quantity=int(input("Enter the Quantity: "))
print(f"The name of the product is {product_name} and it's price is {price} which is ordered for {quantity} pieces.")
#24.
#It will display the output as A B C.
#25.
print("2026", "08", "19", sep="-")
#26.
print("Hello", end=" ")
print("world")
#27.
first=int(input("Enter a Number: "))
second=int(input("Enter other Number: "))
sum=first+second
print(f"The first number is {first} and the second number is {second} and sum of these numbers are {sum}")
#28.
a=float(input("Enter the price of a piece: "))
b=int(input("Enter the quantity Required: "))
print(f"Price of the item is {a} and you require {b} pieces so the total cost would be {a*b:.2f}")
#29.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))
print(f"You are {name}. you are {age} years old and you obtained {marks:.2f} marks.")
#30.
name=(input("Enter student's Name: "))
age=int(input("Enter student's age: "))
height=float(input("Enter student's height(in cm): "))
city=input("Enter student's city of residence: ")
print(f"The name of the Student is {name} and he is {age} years old and is {height:.2f} cms long and is the resident of {city} city.") 