# # 1.
# def first():
#     city="Ahmedabad"
#     print(city)
# first()

# # 2.
# school="SSNL"
# def second():
#     print(school)
# second()

# # 3.
# if True:
#     value=89
# print(value)

# # 4.
# for i in range(1):
#     num=89
# print(num)

# 5.
# scoping simply means which all are the places where the variables can be accessed.
# variable lifetime means for how long the variables cab be accessed like in a function the variable can be accessed only inside the function.

# 6.
# 200
# 100

# # 7.
# clicks = 0
# def click():
#     global clicks
#     clicks += 1
#     print(clicks)
# click()
# print(clicks)

# 8.
# Because print is written before the variable has got some value and inside a fn. 
# when print is written before the variable declaration it simply gives the error 
# because the python compiler gets the variable inside the function but it could 
# not fetch the value.

# # 9.
# def outer():
#     value=89
#     def inner():
#         nonlocal value
#         value=98
#         print(value)
#     inner()
# outer()

# # 10.
# def shopping_list():
#     items=["Apple","Ball","Cat","Dog"]
#     return items
# my_list=shopping_list()
# print("Original List",my_list)
# my_list.append("Elephant")
# my_list[0]="Aeroplane"
# print("Modified List",my_list)

# # 11.
# def outer():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
# counter=outer()
# print(counter())
# print(counter())
# print(counter())

# # 12.
# x=1
# def outer():
#     x=2
#     def inner():
#         x=3
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)
# output:- 3 2 1

# 13.

# 14.
# variable in nonlocal scope remains available because of the concept of closure that's 
# closure is there it keeps a track of its nonlocal scope variables

# 15.
# Because its an inbuilt keyword that has some inbuilt task to be done so we avoid using these variable names.