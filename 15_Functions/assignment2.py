# # 1.
# def welcome():
#     print("welcome to python")
# welcome()


# # 2.
# def greet(name):
#     print("Hello",name)
# greet("Abhi")


# # 3.
# def show_number(number):
#     return number
# print(show_number(8))

# # 4.
# def add(a, b=0):
#     return a+b
# print(add(8,9))

# # 5.
# def square(number):
#     return number**2
# print(square(8))

# # 6.
# def is_even(number):
#     if number%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(is_even(8))

# # 7.
# def get_full_name(first_name, last_name):
#     str= first_name + last_name
#     return str
# print(get_full_name("ABHISHEK ","THAKUR"))

# # 8.
# def introduce(name, city="Pune"):
#     print(f"Myself {name} i am from {city}.")
# introduce("Abhishek")

# # 9.
# def subtract(a, b):
#     return a-b
# print(subtract(8,9))
# print(subtract(9,8))

# # 10.
# def get_min_max(a, b):
#     if a>b:
#         print(f"Min: {b} , Max: {a}")
#     else:
#         print(f"Min: {a} , Max: {b}")
# get_min_max(8, 9)

# # 11.
# def calculate(a, b):
#     if a==0 or b==0:
#         print("Input Error ! Please enter a valid value.")
#     else:
#         print(f"Addition: {a+b}")
#         print(f"subtraction: {a-b}")
#         print(f"Multiplication: {a*b}")
#         print(f"Division: {a//b}")
# calculate(8,9)

# # 12.
# def count_digits(number):
#     if number<0:
#             print("Error!")
#     n=len(str(number))
#     return n
# print(count_digits(98776555))

# # 13.
# def classify_number(number):
#     if number>0:
#         print("Positive")
#     elif number<0:
#         print("Negative")
#     else:
#         print("Zero")
# classify_number(8)

# # 14.
# def calculate_total(price, quantity=1):
#     return price*quantity
# print(calculate_total(888))

# # 15.
# def create_email(username, domain="example.com"):
#     print(f"{username}@{domain}")
# create_email("iambxii","gmail.com")

# # 16.
# def format_name(first, last, uppercase=False):
#     if uppercase==True:
#         return first.upper()+last.upper()
#     else:
#         return first+last
# print(format_name("Abhishek ","Thakur",True))

# # 17.
# def percentage(marks, total=100):
#     perc=(marks*100)/total
#     print(f"{perc}%")
# percentage(391,500)

# # 18.
# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes*seconds_per_minute
# print(convert_minutes(89))

# # 19.
# def student_details(name, age, city):
#     print(city)
#     print(age)
#     print(name)
# student_details("Abhishek","21","Purnea")

# # 20.
# def bill(item, quantity=1, price=100):
#     return f"Bill = {quantity*price}"
# print(bill("Apple",1,120))

# # 21.
# def analyze_number(num):
#     if num%2==0:
#         if num>0:
#             print(f"Absolute num: {num}")
#         else:
#             print(f"Absolute num: {-(num)}")
#         count=0
#         digit=0
#         while num>0:
#             digit+=num%10
#             count+=1
#             num=num//10
#         print(count)
#         return "Even"
#     else:
#         if num>0:
#             print(f"Absolute num: {num}")
#         else:
#             print(f"Absolute num: {-(num)}")
#         count=0
#         digit=0
#         while num>0:
#             digit+=num%10
#             count+=1
#             num=num//10
#         print(count)
#         return "Odd"
# print(analyze_number(8899))

# # 22.
# def calculate_stats(a, b, c):
#     if a<=b and a<=c:
#         smallest=a
#     elif b<=a and b<=c:
#         smallest=b
#     elif c<=b and c<=a:
#         smallest=c

#     # to find a largest number

#     if a>=b and a>=c:
#         Largest=a
#     elif b>=a and b>=c:
#         Largest=b
#     elif c>=b and c>=a:
#         Largest=c

#     total=a+b+c

#     print(f"Largest: {Largest} Smallest: {smallest} Total: {total}")
# calculate_stats(8,9,2)
    
# # 23.
# def make_sentence(subject, verb, object):
#     return f"{subject} {verb} {object}."
# print(make_sentence(subject="I", verb="Love", object="Her"))

# # 24.
# def apply_discount(price, discount=0):
#     actual_price=price-discount
#     return actual_price
# print(apply_discount(888,88))

# # 25.
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus
# print(calculate_pay(8,1000,200))

# # 26.
# def get_coordinates(x=0, y=0):
#     return (x,y)
# print(get_coordinates(8,y=9))

# # 27.
# def compare(a, b):
#     if a>b:
#         return f"A is greater and Absolute value: {(a-b)}."
#     else:
#         return f"B is greater and Absolute value: {-(a-b)}."
# print(compare(8,9))

# # 28.
# def convert_temperature(value, scale="C"):
#     scale=scale.upper()
#     if scale=="F":
#         value=(value*9)/5+32
#         return f"Farenhite: {value}"
#     elif scale=="C":
#         value=((value-32)*5)/9
#         return f"Celcius: {value}"
#     else:
#         return "Enter a valid scale"
# print(convert_temperature(-40,"f"))

# # 29.
# def calculate_result(marks, passing_marks=35):
#     if marks>=passing_marks:
#         return "PASS"
#     else:
#         return "FAIL"
# print(calculate_result(89))

# # 30.
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return f"The Item: {item} costs {quantity*price+delivery_fee}."
# print(order_summary("pizza",delivery_fee=80))

