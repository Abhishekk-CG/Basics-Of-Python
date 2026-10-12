# #1.
# i=1
# while i<=5:
#     print("Hello")
#     i+=1
# #2.
# i=0
# while i<=9:
#     print(i,end=" ")
#     i+=1
# #3.
# i=1
# while i<=10:
#     print(i)
#     i+=1
# #4.
# i=10
# while i>=1:
#     print(i,end=" ")
#     i-=1
# #5.
# i=5
# while i<=50:
#     print(i,end=" ")
#     i+=5
#6.
# i=2
# while i<=20:
#     print(i,end=" ")
#     i+=2
# #7.
# i=1
# while i<=19:
#     print(i,end=" ")
#     i+=2
# #8.
# i=3
# while i<=18:
#     print(i,end=" ")
#     i+=3
# #9.
# i=20
# while i>=2:
#     print(i,end=" ")
#     i-=2
# #10.
# n=int(input("Enter your range: "))
# i=1
# while i<=n:
#     print(i)
#     i+=1
# #11.
# n=int(input("Enter a range: "))
# i=2
# while i<=n:
#     print(i)
#     i+=2
# #12.
# n=int(input("Enter a range: "))
# i=1
# while i<=n:
#     print(i)
#     i+=2
# #13.
# n=int(input("Enter a range: "))
# i=3
# while i<=n:
#     print(i)
#     i+=3
# #14.
# n=int(input("Enter a range: "))
# i=6
# while i<=n:
#     print(i)
#     i+=6
# #15.
# n=int(input("Enter a range: "))
# i=2
# count=0
# while i<=n:
#     count+=1
#     print(i)
#     i+=2
# print(f"THe total number of even numbers are {count}.")
# #16.
# n=int(input("Enter a range: "))
# i=1
# total=0
# while i<=n:
#     print(i)
#     total+=i
#     i+=1
# print(f"The sum of it is {total}.")
# #17.
# n=int(input("Enter a number range: "))
# i=2
# total=0
# while i<=n:
#     print(i)
#     total+=i
#     i+=2
# print(f"The sum of it is {total}.")
# # 18.
# n=int(input("Enter the range for loop iteration: "))
# i=1
# total=0
# while i<=n:
#     print(i)
#     total+=i
#     i+=2
# print(f"The sum of total odd numbers form 1 to {n} is {total}.")
# # 19.
# n=int(input("Enter a number for its table: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
# # 20.
# n=int(input("Enter a number: "))
# i=1
# multi=1
# while i<=n:
#     multi*=i
#     i+=1
#     print(multi,end=" ")
# # 21.
# str=input("Enter a string: ")
# length=(len(str)-1)
# i=0
# while i<=length:
#     char=str[i]
#     i+=1
#     print(char)
# # 22.
# str=input("Enter a string: ")
# length=(len(str)-1)
# i=0
# while i<=length:
#     char=str[i]
#     i+=1
#     print(char,end=" ")
# # 23.
# str=input("Enter a string: ")
# length=(len(str)-1)
# i=0
# count=0
# while i<=length:
#     char=str[i]
#     i+=1
#     count+=1
#     print(char)
# print(f"There are {count} characters in the string.")
# # 24.
# str=input("Enter a string: ")
# length=(len(str)-1)
# i=0
# count=0
# while i<=length:
#     char=str[i]
#     i+=1
#     if char=="a":
#         count+=1
# print(f"There are {count} times A appears in the string.")
# # 25.
# str=input("Enter a string: ")
# length=(len(str)-1)
# i=0
# count=0
# while i<=length:
#     char=str[i]
#     i+=1
#     if "Z">=char>="A":
#         count+=1
# print(f"There are {count} times Uppercase letter appears in the string.")
# # 26.
# i=1
# while i<=4:
#     for j in range(4):
#         print("*",end="")
#     print()
#     i+=1
# # 27.
# i=1
# while i<=5:
#     for j in range(5):
#         print("*",end="")
#     print()
#     i+=1
# # 28.
# i=1
# while i<=5:
#     for j in range(i):
#         print("*",end="")
#     print()
#     i+=1
# # 29.
# i=1
# while i<=5:
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
#     i+=1
# # 30.
# n=int(input("Enter the range: "))
# i=1
# while i<=n:
#     for j in range(1,n+1):
#         print(i*j,end=" ")
#     print()
#     i+=1
