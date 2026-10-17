# # 1.
# output=1,2,3,4
# # 2.
# output=i
# # 3.
# output=2,4,infinite Loop
# # 4.
# n=int(input("Enter a range: "))
# for i in range(1,n+1):
#     if i==7:
#         break
#     print(i,end=" ")
# # 5.
# str=input("Enter a string: ").lower()
# for char in str:
#     if char=="s":
#         break
#     print(char)
# # 6.
# numbers=[9,7,5,3,1,-1,-3,-5,-7,-9]
# for number in numbers:
#     if number<0:
#         break
#     print(number)
# # 7.
# output= (1,1) (1,2) (2,1) (2,2) (3,1) (3,2) 
# # 8.
# str=input("Enter a sentence: ").split()
# search=input("Enter a substring to search: ")
# n=len(str)
# for i in range(n):
#     word=str[i]
#     if word==search:
#         print("Found")
#     break
# else:
#     print("Not found")
# # 9.
# output=1,2,3,5,6
# # 10.
# output= d c t n
# # 11.
# output=1 2 4 
# # 12.
# n=int(input("Enter the range: "))
# for i in range(1,n+1):
#     if i%3==0:
#         continue
#     print(i)
# # 13.
# str=input("Enter a string: ")
# chr=input("Enter a character: ")
# for char in str:
#     if char==chr:
#         continue
#     print(char,end="_")
# # 14.
# num=input("Enter all your marks separated by space: ").split()
# for marks in num:
#     marks=int(marks)
#     if marks<40:
#         continue
#     print(marks,end=" ")
# # 15.
# output=(a,1)(b,1)(a,3)(b,3)(a,4)(b,4)
# # 16.
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# # 17.
# str=input("Enter a string: ").lower()
# count=0
# for char in str:
#     if char in "aeiou":
#         continue
#     count+=1
# print(count)
# # 18.
# output= 1 2 3
#         done
# # 19.
# output=1 3 4 completed
# # 20.
# output=1 2 4 outside loop    
# # 21.
# output=else block 
# # 22.
# lis=input("Enter a value separated by space: ").split()
# target=int(input("Enter a number: "))
# for num in lis:
#     num=int(num)
#     if num==target:
#         print("Found")
#         break
# else:
#     print("Not Found")
# # 23.
# str=input("Enter a string: ").split()
# targ=input("Enter a target string: ")
# for word in str:
#     if targ==word:
#         print("Found")
#         break
# else:
#     print("Character missing")
# # 24.
# n=int(input("Enter a positive number greater than 1: "))
# if n<1:
#     print("Enter a valid number")
# for i in range(2,n):
#     if n%i==0:
#         print("Not prime")
#         break
# else:
#     print("Prime")
# # 25.
# output=all are even 
# # 26.
# output=
# a. A
# b. No output
# c. c
# # 27.
# str=input("Enter a string: ")
# targ=input("Enter a targer substring: ")
# for char in str:
#     if targ==char:
#         print("Found")
#         break
# else:
#     print("Not found")
# # 28.
# output=1 2 3 4
# # 29.
# output=finished
# #30
# output=loop ended 
# # 31.
# for i in range(1,5):
#     if i%2==0:
#         pass
# print(i)
# 32.
for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")
