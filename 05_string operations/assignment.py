#1.
from itertools import count


your_name = "John Doe"
your_city = "New York"
fav_language = 'Python'
message = "This is me writing this code."
print(your_name,your_city,fav_language,message)
#2
empty = ("")
print(empty)
print(len(empty))
print(type(empty))
#3.
third = "Python Programming"
print(third)
print(len(third))
print(third[0])
print(third[-1])
print(third[2])
print(third[-2])
#4.
forth = "Programming"
print(forth[0])
print(forth[1])
print(forth[4])
print(forth[10])
#5.
print(forth[-1])
print(forth[-2])
print(forth[-3])
print(forth[-11])
#6.
sixth = "Abhishek Thakur"
print(sixth[0])
print(sixth[-1])
print(sixth[9])
#7.
seventh = "Python Programming"
print(seventh[0:6])
print(seventh[7:18])
print(seventh[0:5])
print(seventh[13::1])
#8.
eighth = "ABCDEFGHIJKL"
print(eighth[::2])
print(eighth[::3])
print(eighth[1:9:2])
print(eighth[::-1])
#9.
ninth = "Python Programming"
print(ninth[13::1])
print(ninth[8::1])
print(ninth[::-1])
#10.
tenth = "ABCDEFGHIJ"
print(tenth[:4:1])
print(tenth[8::1])
print(tenth[::2])
print(tenth[::-1])
print(tenth[1:10:1])
#11.
eleventh = "apple"
eleventh1 = "this's apple"
eleventh2 = "this is apple and this is orange"
print(len(eleventh))
print(len(eleventh1))
print(len(eleventh2))
#12.
twelfth = "Python Programming"
size = len(twelfth)
print(twelfth[size - 1])
#13.
first_name="Abhishek"
last_name="Thakur"
full_name=first_name + " " + last_name
print(full_name)
#14.
Name = "Abhishek Thakur"
Age = 25
City = "New York"
Programming_language = "Python"
print(f"My name is {Name}. I am {Age} years old. I live in {City} and my favorite programming language is {Programming_language}.")
#15.
name="Abhishek"
age=20
c=name+str(age)
print(c)
#16
d="@abxii07"
print(d*3)
print(d*5)
print(d*10)
#17.
e="*"
print(e*10)
#18.
f="python programming language"
print(f.upper())
print(f.lower())
print(f.capitalize())
print(f.title())
print(f.swapcase())
#19.
g="Python"
h="python"
i=(g==h)
j=g.lower()==h.lower()
print(i)
print(j)
#20.
k="Python is a programming language"
print("Python" in k)
print("Java" in k)
print("programming" in k)
print("language" in k)
#21.
print(k.find("Python"))
print(k.find("Java"))
print(k.find("programming"))
print(k.find("language"))
#22.
print(k.index("Python"))
#print(k.index("Java"))
print(k.index("programming"))
print(k.index("language"))
#23.
l="banana"
print(l.count("a"))
print(l.count("b"))
print(l.count("n"))
#25.
m=filename = "student_notes.pdf"
print(m.startswith("student"))
print(m.endswith(".pdf"))
print(m.endswith(".txt"))
#26.
text = "apple apple apple"
print(text.replace("apple", "mango"))
#27.
print(text.replace("apple", "mango",1))
#28.
text = "Python"
text1 = text.upper()
print(text1)
print(text)
#29.
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#30.
name=input("Enter your name: ")
print(f"my name is {name.strip()}" )
#31.
z="Python is easy to learn"
print(z.split())
#32.
y="apple,banana,mango,orange"
print(y.split(","))
#33.
words = ["Python", "is", "easy"]
print(" ".join(words))
#34.
words1 = "Python-is-easy"
print("/".join(words1.split("-")))
#35.
name="Abhishek"
age=20
city="New York"
print(f"My name is {name}. I am {age} years old. I live in {city}.")
#36.
a = 10
b = 20
print(f"The sum of both is {a + b}.")
#38.
name = input("Enter your name: ")
name1 = name.strip()
print(f"My name is {name}.")
print(f"My name is {name1}.")
print(f"My name is {name.upper()}.")
print(f"My name is {name.lower()}.")
print(f"My name is {name.title()}.")
print(len(name1.strip()))
print(name1[0])
print(name1[-1])
print("Abhishek" in name1)
#39.
sen=input("Enter a sentence: ")
sen1=sen.strip()
sen11=len(sen1.split())
print(f"My sentence is {sen1}.")
print(len(sen1))
print(sen1[0])
print(sen1[-1])
print(sen1.upper())
print(sen1.lower())
print(sen1.title())
print("Python" in sen1)
print(sen1.find("a"))
print(sen11)
