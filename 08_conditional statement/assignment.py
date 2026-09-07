#1.
a=int(input("Enter a number: "))
if a>=10 :
    print("The number is greater than 10.")
#2.
age=int(input("Enter your age: "))
if age>=18 :
    print("You Are An Adult")
#3.
num=int(input("Enter any number: "))
if num > 0 :
    print("The number is Positive")
#4.
marks=int("Enter student's marks: ")
if marks >= 40:
    print("pass")
#5.
num1=int(input("Enter Any Number: "))
if num1 == 0 :
    print("the number is equals to zero")
#6.
number=int(input("Enter any number: "))
if number>=0:
    print("It's a positive Number")
else:
    print("Not a Positive Number")
#7.
age=int(input("Enter your Age: "))
if age>=18:
    print("You Are An Adult")
else:
    print("You Are A Minor")
#8.
num=int(input("Enter A Number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
#9.
marks=int(input("Enter Your Marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")
#10.
a=int(input("Enter a Number: "))
b=int(input("Enter Other Number: "))
if a>b:
    print(f"{a} is Greater than {b}" )
else:
    print(f"{b} is greter than {a}")
#11.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("A")
elif marks>=75<=89:
    print("B") 
elif marks>=60<=74:
    print("c")
elif marks>=40<=59:
    print("D")
else:
    print("F")
# 12.
a=int(input("Enter a number: ")) 
if a>0:
    print("Positive")
elif a==0:
    print("zero")
else:
    print("Negative")
#13.
a=int(input("Enter a Number: "))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday") 
elif a==3:
    print("wednesday") 
elif a==4:
    print("Thursday") 
elif a==5:
    print("Friday")
else:
    print("Others") 
# 14.
a=int(input("Enter your Marks: "))
if a>=90:
    print("Excellent")
elif a>=80:
    print("Good")
elif a>=40:
    print("Pass")
else:
    print("Fail")
#15. 
a=int(input("Enter a number: "))
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else:
    print("Others")
#16.
age=int(input("Enter your age: "))
if age>=18:
    if age<=60:
        print("You are Between 18 and 60.")
#17.
marks=int(input("Enter your Marks: "))
if marks>=40:
    if marks<=75:
        print("Good")
else:
    print("Fail")
#18.
a=int(input("Enter a number: "))
if a>0:
    if a>100:
        print("The Number is grater than 100.")
else:
    print("The Number is a Negative Number.")
#19.
age=int(input("Enter your age: "))
if age>=18:
    if age<=60:
        print("Adult")
else:
    print("Minor")
#20.
a=int(input("Enter a Number: "))
if a!=0:
    if a>0:
        print("positive")
    else:
        print("Negative")
else:
    print("Zero")
#21.
age=int(input("Enter your Age: "))
marks=int(input("Enter your Marks: "))
if age>=18:
    if marks>=40:
        print("Eligible")
else:
    print("Ineligible")
#22.
number=int(input("Enter any number: "))
if number<10:
    if number>100:
        print("Special")
#23.
age=int(input("Enter your Age: "))
identity=bool(input("has_id is: "))
if age>=18:
    if identity==True:
        print("Allowed")
#24.
a=int(input("Enter a Number: "))
b=int(input("Enter any number: "))
if a>10:
    if b>10:
        print("Both the numbers are Greater than 10.")
#25.
number=int(input("Enter a Number: "))
if number<0:
    if number>100:
        print("Special Number")
#26.
shop=input("Enter Your Shop Name: ")
status=bool(input("is_closed: "))
if not(status==True):
    print("Open")
else:
    print("Closed")
#27.
x=int(input("Enter any Number: "))
if 10<x<50:
    print("Number lies between 10 and 50")
#28.
x=int(input("Enter any Number: "))
if x<10 or x>50:
    print("the number is outside the range.")
#29.
student=bool(input("is_student(True/False): ").capitalize)
identity=bool(input("has_Id(True/False): ").capitalize)
ticket=bool(input("has_ticket(True/False): ").capitalize)
if student==True:
    if identity==True:
        if ticket==True:
            print("Allowed")
else:
    print("Not Allowed")
#30.
age=int(input("Enter your Age: "))
marks=int(input("Enter your Marks: "))
has_id=bool(input("has_id(True/False): ").capitalize)
if age>=18:
    if marks>=40:
        if has_id==True:
            print("Eliible")
else:
    print("Not Eliible")
    



