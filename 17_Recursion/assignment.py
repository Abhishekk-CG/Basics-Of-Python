# # 1.
# 2
# 1
# STOP 
# None
# 1
# 2

# 2.
# if n==0: #This is the base case because when this condition satisfies the recursion stops meaning it will simply return something instead of calling the function again.

# 3.
# This does reach the base case because recursion goes in the opposite direction of the base case.
# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n - 1)
# count(2)

# 4.
# It will return an error because there is nothing returned it returns nonetype 
# and thus the addition of none type and int gives an error.
# def answer(n):
#     if n == 0:
#         return 0
#     return n + answer(n - 1)
# print(answer(3))

# # 5.
# def countdown(n):
#     if n==0:
#         print("Done")
#         return
#     print(n)
#     countdown(n-1)
# countdown(3)

# # 6.
# count=1
# def count_up(n):
#     global count
#     if count==n:
#         print(count)
#         return
#     print(count)
#     count+=1
#     count_up(n)
# count_up(4)

# # 7.
# count=0
# sum=0
# def sum_to(n):
#     global count
#     global sum
#     if count==n:
#         print(sum)
#         return
#     count+=1
#     sum+=count
#     sum_to(n)
# sum_to(0)
    
# # 8.
# count=1
# factor=1
# def factorial(n):
#     global count
#     global factor
#     if count==n or n==0:
#         print(factor)
#         return
#     count+=1
#     factor*=count
#     factorial(n)
# factorial(0)
    
# # 9.
# num=0
# sum=0
# def digit_sum(n):
#     global num
#     global sum
#     sum+=n%10
#     num=n//10
#     if num<=0:
#         print(sum)
#         return
#     digit_sum(num)
# digit_sum(0)

# # 10.
# result=1
# repeatition=0
# def power(base, exponent):
#     global result
#     global repeatition
#     if exponent==repeatition:
#         print(result)
#         return
#     result*=base
#     repeatition+=1
#     power(base,exponent)
# power(2,0)

# 11.
