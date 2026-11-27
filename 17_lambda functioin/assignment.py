# 1.
sum=lambda a,b: a+b
print(sum(10,20))

# 2.
square=lambda n: n*n
print(square(6))

# 3.
cube=lambda n: n*n*n
print(cube(3))

# 4.
check=lambda num:"EVEN" if num%2==0 else "ODD"
print(check(7))

# 5.
greater_num=lambda a,b:"A" if a>b else "B"
print(greater_num(89,98))

# 6.
celcius_to_farenhite=lambda celcius:(celcius*9/5)+32
print(celcius_to_farenhite(25))

# 7.
string_length=lambda str:len(str)
print(string_length("PYTHON"))

# 8.
string_upper=lambda str:str.upper()
print(string_upper("hello world"))

# 9.
last_character=lambda str:str[-1]
print(last_character("CODING"))

# 10.
final_price=lambda original_price,discount_percentage: original_price - (original_price*discount_percentage/100)
print(final_price(1000,10))