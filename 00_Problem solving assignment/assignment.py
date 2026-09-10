# #1.
# num=int(input("Enter a number: "))
# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")
# #2.
# num=int(input("Enter a number: "))
# div=num/2
# if num%2==0:
#     if div>0:
#         print("Positive Even")
#     elif div<0:
#         print("Negative Even")
# elif num%2==1:
#     if div>0:
#         print("Positive odd")
#     elif div<0:
#         print("Negative odd")
# if num%2==0 and div==0:
#     print("Zero")
# #3.
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# if num1>num2:
#     print("First number is greater than second")
# elif num1<num2:
#     print("second number is greater than first")
# else:
#     print("Both are Equal")
# #4.
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# if num2>num1<num3:
#     print("First is the smallest")
# elif num1>num2<num3:
#     print("Second is the smallest")
# else:
#     print("Third is the smallest")
# #5.
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# if num2<num1>num3:
#     print("First is the Greatest")
# elif num1<num2>num3:
#     print("Second is the Greatest")
# else:
#     print("Third is the Greatest")
# #6.
# num=int(input("Enter a number: "))
# if num%5==0 and num%11==0:
#     print("Its Divisible by Both 5 and 11")
# elif num%5==0:
#     print("Its Divisible by 5")
# elif num%11==0:
#     print("Its Divisible by 11")
# else:
#     print("Divisible by neither")
# #7.
# num=int(input("Enter a number: "))
# if num%3==0 and num%7==0:
#     print("Its Divisible by Both 3 and 7")
# elif num%3==0:
#     print("Its Divisible by 3")
# elif num%7==0:
#     print("Its Divisible by 7")
# else:
#     print("Divisible by neither")
# #8.
# marks=int(input("Enter Your Marks: "))
# if marks<0:
#     print("Invalid Marks")
# elif marks>100:
#     print("Invalid Marks")
# elif marks>=40:
#     print("Pass")
# else:
#     print("Fail")
# #9.
# marks=int(input("Enter Your Marks: "))
# if 100>=marks>=90:
#     print("A")
# elif 89>=marks>=80:
#     print("B")
# elif 79>=marks>=70:
#     print("C")
# elif 69>=marks>=60:
#     print("D")
# elif 59>=marks>=40:
#     print("E")
# else:
#     print("Fail")
# #10.
# age=int(input("Enter your age: "))
# if age<0:
#     print("Invalide age")
# elif age>=0 and age<18:
#     print("Cant vote")
# else:
#     print("Can vote")
# #11.
# year=int(input("Enter the year: "))
# if (year%4==0 or year%400==0) and (not(year%100==0)):
#     print("Leap year")
# else:
#     print("Not a leap year")
# #12.
# char=input("Enter your data: ")
# if "A"<=char<="Z":
#     print("Uppercase")
# elif "0"<=char<="9":
#     print("Digit")
# elif "a"<=char<="z":
#     print("lowercase")
# else:
#     print("Special character")
# #13.
# char=input("Enter an alphabet: ").lower()
# if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#     print("Vowel")
# elif char=="b" or char=="c" or char=="d" or char=="f" or char=="g" or char=="h" or char=="j" or char=="k" or char=="l" or char=="m" or char=="n" or char=="p" or char=="q" or char=="r" or char=="s" or char=="t" or char=="v" or char=="w" or char=="x" or char=="y" or char=="z":
#     print("Consonant")
# else:
#     print("Invalid Input")
# #14.
# Cost=int(input("Enter the cost price: "))
# Selling=int(input("Enter thr selling price: "))
# value=(Selling-Cost)
# if value>0:
#     print("Profit")
# elif value<0:
#     print("Loss")
# else:
#     print("Np profit No loss")
# #15.
# Cost=int(input("Enter the cost price: "))
# Selling=int(input("Enter thr selling price: "))
# value=(Selling-Cost)
# if Cost<=0 or Selling<=0:
#     print("Error! Enter a Valid price")
# if value>0:
#     print(f"profit!!! you have gained {value/Cost*100}% profit.")
# elif value<0:
#     print(f"loss!!! you have faced {-(value/Cost*100)}% loss")
# else:
#     print("No profit No loss")
# #16.
# units=int(input("Enter your Units used: "))
# units1=units-200
# units2=units-100
# if units>200:
#     print(f"yout total bill is {1200+(units1*10)} rupees.")
# elif 200>=units>100:
#     print(f"yout total bill is {500+(units2*7)} rupees.")
# elif units>=100:
#     print(f"Your total bill is {units*5} rupees.")
# #17.
# num1=int(input("Enter first number: "))
# num2=int(input("Entr second number: "))
# print("'Enter the respective operator signs only for respective operations /n"
#                         "[+ - * /]'")
# oper=input("Enter the operator: ")
# if oper=="+" or oper=="-" or oper=="*" or oper=="/":
#     if oper=="+":
#         print(f"The addition is {num1+num2}.")
#     elif oper=="-":
#         print(f"The subtraction is {num1-num2}.")
#     elif oper=="*":
#         print(f"The multiplication is {num1*num2}.")
#     elif oper=="/":
#         print(f"The division is {num1/num2}.")
# else:
#     print("Enter a valid operator")
# #18.
# temp=int(input("Enter the temperature: "))
# if temp<0:
#     print("Freezing")
# elif 15<=temp>=0:
#     print("Very cold")
# elif 25<=temp>=16:
#     print("Cold")
# elif 35<=temp>=26:
#     print("Normal")
# else:
#     print("Hot")
# #19.
# range=int(input("Enter the Number: "))
# if 10>=range>=0:
#     print("The number lie between 0 to 10.")
# elif 50>=range>=11:
#     print("The number lie between 11 to 50.")
# elif 100>=range>=51:
#     print("The number lie between 51 to 100.")
# elif range>100:
#     print("The number lies above 100.")
# else:
#     print("Enter a Positive Number")
# #20.
# a=int(input("Enter first side of triangle: "))
# b=int(input("Enter second side of triangle: "))
# c=int(input("Enter third side of triangle: "))
# if a + b > c and a + c > b and b + c > a:
#     print("These are valid sides of traingle")
# else:
#     print("These are not the valid sides ")
##21.
# a=int(input("Enter first side of triangle: "))
# b=int(input("Enter second side of triangle: "))
# c=int(input("Enter third side of triangle: "))
# if a + b > c and a + c > b and b + c > a:
#     print("These are valid sides of traingle")
#     if a==b==c:
#         print("Equilaterl Triangle")
#     elif a==b!=c or a==c!=b or b==c!=a:
#         print("Isosceles Triangle")
#     elif a!=b!=c:
#         print("Scalene Triangle")
# else:
#     print("They would not form a valid traingle")
# #22.
# balance=int(input("Enter your account balance: "))
# withdraw_amt=int(input("Enter the withdrawal amount: "))
# if withdraw_amt<=0 or balance<=0:
#     print("Enter a valid Amount")
#     if withdraw_amt%100!=0 and withdraw_amt<0:
#         print("Enter a valid amount divisible by 100")
# remaining_balance=(balance-withdraw_amt)
# if remaining_balance<0:
#     print("you can't withdraw amount more than your account balance ")
# if remaining_balance>=500:
#     print(f"withdrawal successful your account Balance is {remaining_balance}" )
# else:
#     print("'You cant withdraw money beacuse your account Balance will be less than Rs.500 " \
#     "which will lead to the panelty'")
# #23.
# username=input("Enter your Username: ")
# password=input("Enter your password: ")
# if username=="admin":
#     if password=="python123":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("User Not Found")
# #24.
# price=int(input("Enter the Amount: "))
# if price<500:
#     print(f"Your original amount is {price} and you will get 0% discount")
# elif 999>=price>=500:
#     price(f"your original price is {price} and you are goint to get 5% discount so the discounted price for you is {price-(price*5/100)}.")
# elif 1999>=price>=1000:
#     price(f"your original price is {price} and you are goint to get 10% discount so the discounted price for you is {price-(price*10/100)}.")
# elif 4999>=price>=2000:
#     price(f"your original price is {price} and you are goint to get 15% discount so the discounted price for you is {price-(price*15/100)}.")
# elif 5000<=price:
#     price(f"your original price is {price} and you are goint to get 20% discount so the discounted price for you is {price-(price*20/100)}.")
# #25.
# sub1=int(input("Enter your marks: ")) 
# sub2=int(input("Enter your marks: ")) 
# sub3=int(input("Enter your marks: ")) 
# if 100>=sub1>=0 and  100>=sub2>=0 and  100>=sub3>=0:
#     if sub1>35 and sub2>35 and sub3>35:
#         print("Pass")
#         average=(sub1+sub2+sub3)/3
#         print(f"Your Average is {average}.")
#         if 100>=average>=75:
#             print("Distinction")
#         elif 74>=average>=60:
#             print("First class")
#         elif 59>=average>=50:
#             print("Second class")
#         elif 49>=average>=35:
#             print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Enter valid marks")
# #26.
# day=int(input("Enter the day": ))
# month=int(input("Enter the month: "))
# year=int(input("Enter the year: "))
# #27.
# Hours=int(input("Enter hours: "))
# Minutes=int(input("Enter minutes: "))
# Seconds=int(input("Enter seconds: "))
# time=(f"{Hours}:{Minutes}:{Seconds}")
# if 24>=Hours>=0 and 60>=Minutes>=0 and 60>=Seconds>=0:
#     print(f"Valid time ({time})")
# else:
#     print("Enter a valid time")
# #28.
# name1=input("Enter your name: ")
# age1=int(input("Enter your age: "))
# name2=input("Enter your name: ")
# age2=int(input("Enter your age: "))
# name3=input("Enter your name: ")
# age3=int(input("Enter your age: "))
# if age2>age3 and age1>age3:
#     print(f"{name3} is youngest.")
# elif age3>age2 and age1>age2:
#     print(f"{name2} is youngest.")
# elif age2>age1 and age3>age1:
#     print(f"{name1} is youngest.")
# elif age1==age2 and (age3>age1 or age3>age2):
#     print(f"{name1} {name2} have same age and are youngest.")
# elif age1==age2 and (age3<age1 or age3<age2):
#     print(f"{name3} is youngest.")
# elif age2==age3 and (age1>age3 or age1>age2):
#     print(f"{name2} {name3} have same age and are youngest.")
# elif age1==age2 and (age1<age3 or age1<age2):
#     print(f"{name1} is youngest.")
# elif age1==age3 and (age2>age1 or age2>age3):
#     print(f"{name1} {name3} have same age and are youngest.")
# elif age1==age3 and (age2<age1 or age2<age3):
#     print(f"{name3} is youngest.")
# elif age1==age2==age3:
#     print("All three are of same age")
#29.
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
if num1>num2>num3 or num3>num2>num1:
    print(f"{num2} is second largest.")
elif num2>num1>num3 or num3>num1>num2:
    print(f"{num1} is second largest.")
elif num1>num3>num2 or num2>num3>num1:
    print(f"{num3} is second largest.")