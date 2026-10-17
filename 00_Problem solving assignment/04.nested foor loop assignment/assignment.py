# # 1.
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
# # 2.
# n=int(input("Enter your range: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i} X {j} = {i*j}")
# # 3.
# str=input("Enter your pattern symbol: ")
# for i in range(3):
#     for j in range(4):
#         print(str,end="")
#     print()
# # 4.
# m=int(input("Enter your row range: "))
# n=int(input("Enter your col. range: "))
# for i in range(m):
#     for j in range(n):
#         print(f"({i},{j})",end="")
#     print()
# # 5.
# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end="")
#     print()
# # 6.
# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end="")
#     print()
# # 7.
# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# # 8.
# n=int(input("Enter your number: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# # 9.
# m=int(input("Enter your row range: "))
# n=int(input("Enter your col. range: "))
# for i in range(m):
#     for j in range(n):
#         print("*",end="")
#     print()
# # 10.
# n=int(input("Enter your range: "))
# for i in range(n):
#     bag=""
#     for j in range(1,n+1):
#         if j%2==0:
#             bag+="1"
#         else:
#             bag+="0"
#     print(bag)
# # 11.
# m=int(input("Enter your row range: "))
# n=int(input("Enter your col. range: "))
# for i in range(m):
#     for j in range(1,n+1):
#         if j%2==0:
#             print(j,end=" ")
#         else:
#             continue
#     print()
# # 12.
# n=int(input("Enter your range: "))
# for i in range(n):
#     for j in range(1,n+1):
#         if j%2!=0:
#             print(j,end=" ")
#     print()
# # 13.
# n=int(input("Enter your range: "))
# for i in range(n):
#     for j in range(n):
#         if (i+j)%2!=0:
#             print("O",end=" ")
#         else:
#             print("E",end=" ")
#     print()
# # 14.
# n=int(input("Enter your range: "))
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print()