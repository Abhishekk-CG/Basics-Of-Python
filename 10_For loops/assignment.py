#1.
a="hello"
for i in range(1,6):
    print(a)
#2.
for i in range(0,10):
    print(i, end=" ")
#3.
for i in range(1,11):
    print(i)
#4.
for i in range(10,0,-1):
    print(i)
#5.
for i in range(5,55,5):
    print(i)
#6.
for i in range(2,22,2):
    print(i)
#7.
for i in range(1,20,2):
    print(i)
#8.
for i in range(3,21,3):
    print(i)
#9.
for i in range(20,0,-2):
    print(i)
#10.
n=int(input("Enter the range: "))
for i in range(1,n+1):
    print(i)
#11.
n=int(input("Enter the range: "))
for i in range(2,n+1):
    if i%2==0:
        print(i)
#12.
n=int(input("Enter the range: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i)
#13.
n=int(input("Enter the range: "))
for i in range(1,n+1):
    if i%3==0:
        print(i)
#14.
n=int(input("Enter the range: "))
for i in range(1,n+1):
    if i%6==0:
        print(i)
#15.
n=int(input("Enter the range: "))
count=0
for i in range(2,n+1,2):
    count=count+1
print(f"The total even numbers are {count}.")
#16.
n=int(input("Enter the range: "))
sum=0
for var in range(1,n+1):
    sum=sum+var
print(f"The total sum of n numbers are equal to {sum}")
#17.
n=int(input("Enter the range: "))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print(f"The sum of all even numbers are {sum}")
#18.
n=int(input("Enter the range: "))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
print(f"The sum of all odd numbers are {sum}")
#19.
n=int(input("Enter the Number: "))
multi=0
for i in range(1,11):
    multi=multi+n
    print(multi,end=" ")
#20.
n=int(input("Enter the number: "))
num=1
for i in range(1,n+1):
    num=num*i
print(f"The multiplication is {num}.")
#21.
str=input("Enter the string: ")
n=len(str)
for i in range(0,n):
    print(str[i])
#22.
str=input("Enter the string: ")
n=len(str)
for i in range(0,n):
    print(str[i],end="")
#23.
str=input("Enter the string: ")
n=len(str)
count=0
for i in range(n):
    count=count+1
print(f"The number of characters in string is {count}")
#24.
str=input("Enter the string: ")
count=0
for character in str:
    if character=="a":
        count += 1
print(count)
#25.
str=input("Enter the string: ")
count=0
for character in str:
    if character>="A" and character<="Z":
        count=count+1
print(count)
#26.
for row in range(3):
    for column in range(4):
        print("*",end="")
    print()
#27.
for row in range(5):
    for column in range(5):
        print("*",end="")
    print()
#28.
for row in range(1,6):
    for column in range(1,row+1):
        print("*",end="")
    print()
#29.
for row in range(6):
    for column in range(1,row+1):
        print(column,end="")
    print()
#30
n=int(input("Enter a range: "))
for row in range(1,n+1):
    for column in range(1,n+1):
        print(column*row,end=" ")
    print()
#31.
n=int(input("Enter a range: "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end="")
    print()