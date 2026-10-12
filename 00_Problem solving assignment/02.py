#1.
for i in range(1,4):
    for j in range(1,4):
        print("*",end="")
    print()
#2.
for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()
#3.
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()
#4.
for i in range(1,6):
    for j in range(1):
        print("* "*i)
    print()
#5.
for i in range(1,6):
    for j in range(1):
        star="* "*(6-i)
        print(star)
    print()
#6.
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#7.
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#8.
for i in range(1,6):
    for j in range(1,11):
        table=i*j
        print(table,end=" ")
    print()
#9.
for i in range(1,4):
    for j in range(1,6):
        output=i*j
        print(output,end=" ")
    print()
#10.
for i in range(1,6):
    for j in range(1,6):
        print(j**2,end=" ")
    print()
#11.
var=65
for i in range(1,6):
    for j in range(i):
        print(chr(var+j),end="")
    print()
#12.
var=64
for i in range(1,6):
    var+=1
    for j in range(i):
        print(chr(var),end="")
    print()
#13.
for i in range(5):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num+=2
    print()
#14.
for i in range(5):
    num=2
    for j in range(i+1):
        print(num,end=" ")
        num+=2
    print()
#15.
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
#16.
for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()
#17.
num=0
for i in range(3):
    for j in range(3):
        num+=1
        print(num,end=" ")
    print()
#18.
num=0
for i in range(4):
    for j in range(5):
        num+=1
        print(num,end=" ")
    print()
#19.
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})",end=" ")
    print()
#20.
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} {j}")
#21.
for i in range(1,11):
    for j in range(1,11):
        value=i*j
        print(value,end=" ")
    print()
#22.
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
#23.
for i in range(5):
    for j in range(1,6-i):
        print(j,end=" ")
    print()
#24.
for i in range(5):
    for j in range(5,0+i,-1):
        print(j,end=" ")
    print()
#25.
for i in range(1,6):
    for j in range(5):
        print(i,end=" ")
    print()
#13.
for i in range(1,11,2):
    for j in range(i+1):
        if j%2==1:
            print(j,end=" ")
    print()