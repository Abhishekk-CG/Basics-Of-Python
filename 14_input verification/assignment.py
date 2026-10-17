# # 1.
# i=True
# while i==True:
#     marks=int(input("Enter your marks: "))
#     if 100>=marks>=1:
#         i=False
# # 2.
# i=True
# while i==True:
#     num=int(input("Enter a number: "))
#     if num>0:
#         print(f"Number accepted = {num}")
#         i=False
# # 3.
# i=True
# while i==True:
#     age=int(input("Enter your marks: "))
#     if 120>=age>=0:
#         i=False
#     else:
#         print("Error !")
# 4.
# i=True
# while i==True:
#     choice=input("Enter your menu choice: ").lower()
#     if choice=="view profile" or choice=="edit profile" or choice=="settings" or choice=="exit":
#         i=False
# # 5.
# i=True
# while i==True:
#     password=input("Enter your password: ").strip()
#     length=len(password)
#     if length>=8:
#         i=False
# # 6.
# i=True
# while i==True:
#     temp=int(input("Enter your marks: "))
#     if 45>=temp>=-20:
#         i=False
# # 7.
# bal=5000
# i=True
# while i==True:
#     withdraw_bal=int(input("Enter your withdrawal balance: "))
#     if withdraw_bal<=0 or withdraw_bal>bal:
#         pass
#     else:
#         print("Withdrawal successful !")
#         print(f"Your remaining balance is Rs.{bal-withdraw_bal}.")
#         i=False
# # 8.
# i=True
# j=True
# while i==True and j==True:
#     username=input("Enter your username: ").strip()
#     n=len(username)
#     for char in username:
#         if char==" " :
#             j=False
#     if n
        
# # 9.
# i=True
# while i==True:
#     num=int(input("Enter a number: "))
#     if num%15==0:
#         print(f"Accepted number = {num}")
#         i=False
# # 10.
# pin=2468
# for i in range(3):
#     pinn=int(input("Enter your pin: "))
#     if pinn==pin:
#         print("Correct pin")
#     else:
#         print("Incorrect Pin")
# else:
#     print("Access denied")
# # 11.
# i=True
# while i==True:
#     n=int(input("Enter a number: "))
#     if 50>=n>=10:
#         i=False
#         print("Value Accepted")
#         if n%2==0:
#             print("Even number")
#         else:
#             print("Odd No.")
# # 12.
# bal=2000
# i=True
# while i==True:
#     deposit_amt=int(input("Enter your withdrawal balance: "))
#     if deposit_amt>0:
#         print(f"Your available balance is Rs.{bal+deposit_amt}.")
#         i=False
# # 13.
# i=True
# while i==True:
#     num=int(input("Enter your number: "))
#     if 100>=num>=1:
#         i=False
# # 14.
# i=True
# while i==True:
#     num=int(input("Enter your number: "))
#     if 100>=num>=1:
#         i=False
#         if num>=75:
#             print("Distinct")
#         elif num>=60:
#             print("First class")
#         elif num>=35:
#             print("Pass")
#         else:
#             print("Fail")
# # 15.
# i=True
# while i==True:
#     username=input("Enter your uername: ").split()
#     password=input("Enter your paassword: ").split()
#     if len(username)>=5:
#         for char in username:
#             if char!=" ":

# # 16.
# i=True
# while i==True:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     if b!=0:
#         operator=input("Enter the operator sign: ")
#         if operator=="+" or operator=="-" or operator=="*" or operator=="/":
#             i=False
#             if operator=="+":
#                 print(a+b)
#             elif operator=="-":
#                 print(a-b)
#             elif operator=="*":
#                 print(a*b)
#             elif operator=="/":
#                 print(a/b)
# # 17.
# bal=10000
# i=True
# while i==True:
#     print("""
# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Exit
# """)
#     choice=int(input("Enter your choice: "))
#     if choice==1 or choice==2 or choice==3 or choice==4:
#         i=False
#         if choice==1:
#             print(f"Available balance: {bal}")
#         if choice==2:
#             deposit_amt=int(input("Enter your deposit amount: "))
#             if deposit_amt<=0:
#                 i=True
#             else:
#                 print("Amount credited successfully")
#                 print(f"Your available balance is Rs.{bal + deposit_amt}.")
#         if choice==3:
#             withdraw_amt=int(input("Enter your withdrwal amount: "))
#             if withdraw_amt<=0 or withdraw_amt>bal:
#                 i=True
#             else:
#                 print("Amount debited successfully")
#                 print(f"Your available balance is Rs.{bal - withdraw_amt}.")
#         if choice==4:
#             i=False
#             print("Exited successfully")
# # 18.
# i=True
# while i==True:
#     month=int(input("Enter month number: "))
#     if 12>=month>=1:
#         i=False
#         day=int(input("Enter day number: "))
#         if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#             if 31>=day>=1:
#                 i=False
#             else:
#                 i=True
#         elif month==4 or month==6 or month==9 or month==1:
#             if 30>=day>=1:
#                 i=False
#             else:
#                 i=True
#         else:
#             if day<=29:
#                 i=False
#             else:
#                 i=True
# # 19.
# i=True
# while i==True:
#     price=int(input("Enter the price: "))
#     quantity=int(input("Enter the quantity of the product: "))
#     if price>0 and quantity>0:
#         i=False
#         print(f"You have to pay Rs.{price*quantity}")
# # 20.
# i=True
# while i==True:
#     n=int(input("Enter how may number you wants to input: "))
#     if 20>=n>=1:
#         i=False
#         total=0
#         for j in range(1,n+1):
#             num=int(input("Enter your number: "))
#             total+=num
#             avg=total/j
#         print(f"Your Average is: {avg}.")
# # 21.
# while True:
#     pwd=input("Enter your Password: ")
#     if (len(pwd) >= 8 and 
#         any(char.isupper() for char in pwd) and 
#         any(char.islower() for char in pwd) and 
#         any(char.isdigit() for char in pwd) and 
#         " " not in pwd):
#         break
#     else:
#         print("Enter your password again")
