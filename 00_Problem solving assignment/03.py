#1.


# #2.
# Pass=0
# fail=0
# good=0
# excellent=0
# for i in range(10):
#     marks=int(input("Enter marks of the student: "))
#     if 100>=marks>=75:
#         excellent=excellent+1
#         print("Excellent")
#     elif 74>=marks>=50:
#         good=good+1
#         print("Good")
#     elif 49>=marks>=35:
#         Pass=Pass+1
#         print("Pass")
#     elif marks<35:
#         fail=fail+1
#         print("Fail")
#     else:
#         print("Enter a valid data")
# print(f"The total number student who got excellent grade is {excellent}")
# print(f"The total number student who got good grade is {good}")
# print(f"The total number student who got pass grade is {Pass}")
# print(f"The total number student who got failed is {fail}")
# #3.
# sen=input("Enter a sentence: ").split()
# lenth=len(sen)
# highest_score=0
# highest_word=""
# for i in range(lenth):
#     word=sen[i]
#     score=0
#     for ch in word:
#         if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#             score=score+2
#         elif ch=='b' or ch=='c' or ch=='d' or ch=='f' or ch=='g' or ch=='h' or ch=='j' or ch=='k' or ch=='l' or ch=='m' or ch=='n' or ch=='p' or ch=='q' or ch=='r' or ch=='s' or ch=='t' or ch=='v' or ch=='w' or ch=='x' or ch=='y' or ch=='z':
#             score=score+3
#         elif ch.isdigit():
#             score +=3
#         else:
#             score +=4
#     if score>highest_score:
#         highest_score=score
#         highest_word=word
# print(f"The highest scoring word is {highest_word} and highest score is {highest_score}.")
# #4.
# for i in range(5):
#     pwd=input("Enter your Password: ").strip()
#     cond1=(len(pwd)>=8)
#     cond2=False
#     cond3=False
#     cond4=False
#     cond5=False
#     for ch in pwd:
#         if ch.isupper():
#             cond2=True
#         elif ch.islower():
#             cond3=True
#         elif ch.isdigit():
#             cond4=True
#         else:
#             cond5=True
#     score=0
#     if cond1==True:
#         score+=1
#     if cond2==True:
#         score+=1
#     if cond3==True:
#         score+=1
#     if cond4==True:
#         score+=1
#     if cond5==True:
#         score+=1 
#     if score==5:
#         print("Strong")
#     if score==3 or score==4:
#         print("Medium")
#     if score<3:
#         print("Weak")
# #5.
# sent=input("Enter your Sentence: ").split()
# length=len(sent)
# long=0
# medium=0
# short=0
# for i in range(length):
#     word=sent[i]
#     word_len=len(word)
#     if word_len>6:
#         long+=1
#         print("Long")
#     elif 6>=word_len>=4:
#         medium+=1
#         print("Medium")
#     elif word_len<=3:
#         short+=1
#         print("Short")
# print(f"The total number of long words are {long} and medium words are {medium} and short words are {short}.")
# #6.
# even=0
# odd=0
# for i in range(5):
#     num=int(input("Enter a number: "))
#     num=str(num)
#     length=len(num)
#     if length%2==0:
#         even+=1
#         print("Even digit number")
#     elif length%2==1:
#         odd+=1
#         print("odd digit number")
# if even>odd:
#     print("Even occurs more")
# elif odd>even:
#     print("Odd occurs more")
# else:
#     print("Equal")
# #7.
# count=0
# str=input("Enter a string: ").strip()
# for ch in str():
# #8.
# total_amt=0
# budget=0
# regular=0
# premium=0
# luxury=0
# for i in range(8):
#     price=int(input("Enter the price of the product: "))
#     total_amt += price
#     if price>=5000:
#         luxury+=1
#         print("luxury")
#     elif 4999>=price>=2000:
#         premium+=1
#         print("premium")
#     elif 1999>=price>=500:
#         regular+=1
#         print("Regular")
#     elif price<=500:
#         budget+=1
#         print("Budget")
#     else:
#         print("Enter a valid value")
# print(f"The total amount of purchase will be {total_amt}.")
# print(f"The total luxury items are {luxury} and premium items are {premium} and regular items are {regular} and budget items are {budget}.")
# print(f"The average amount of total items purchased is {total_amt/5}.")
# #9.
# vowel=0
# consonant=0
# digit=0
# special_character=0
# sen=input("Enter a string: ").split()
# length=len(sen)
# for i in range(length):
#     word=sen[i]
#     position=0
#     for ch in word:
#         position+=1
#         if position%2==0:
#             print("Position is even")
#         elif position%2==1:
#             print("The position is odd")
#         if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#             vowel+=1
#             print("vowel")
#         elif ch.isalpha():
#             consonant+=0
#             print("consonant")
#         elif ch.isdigit():
#             digit+=0
#             print("digit")
#         else:
#             special_character+=0
#             print("special character")
# print(f"The total number of vowels are {vowel} and consonants are {consonant} and digits are {digit} and special characters are {special_character}.")
# #10.
# star=0
# n=int(input("Enter the range: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#         star=0
#         for k in range(3*star+1):
#             star+=1
#             print("*",end="")
#     print()
# #11.
# for i in range(5):
#     username=input("Enter your username: ").strip()
#     length=len(username)
#     char=username[0]
#     digit=0
#     alphabet=0
#     underscore=0
#     score=0
#     cond1=False
#     cond2=False
#     cond3=False
#     cond4=False
#     for j in range(length):
#         if username[j].isdigit():
#             cond1=True
#             digit+=1
#         elif username[j].isalpha()  or username in'aeiou':
#             cond2=True
#             alphabet+=1
#         elif username[j]=="_":
#             cond3=True
#             underscore+=1
#         elif length>=5:
#             cond4=True
#         else:
#             print("invalid Username")
#     if cond1==True:
#         score+=1
#     if cond2==True:
#         score+=1
#     if cond3==True:
#         score+=1
#     if cond4==True:
#         score+=1
#     if score==4:
#         print("Valid")
#     if 3>=score>=2:
#         print("Needs Improvement")
#     if score<=1:
#         print("Invalid")
# #12.
# vowel=0
# consonants=0
# sentence=input("Enter a sentence: ").split()
# length=len(sentence)
# for i in range(length):
#     word=sentence[i]
#     for char in word:
#         if char in "aeiouAEIOU":
#             vowel+=1
#         elif char.isalpha():
#             consonants+=1
# if vowel>consonants:
#     print("Vowels win")
# elif vowel<consonants:
#     print("Consonants win")
# elif vowel==consonants:
#     print("Draw")
# #13.
# total=0
# for i in range(6):
#     usage=int(input("Enter your used units: "))
#     if usage>400:
#         bill=((usage-400)*15+3200)
#         print(bill)
#     elif 400>=usage>=201:
#         bill=((usage-300)*10+1200)
#         print(bill)
#     elif 200>=usage>=101:
#         bill=((usage-100)*7+500)
#         print(bill)
#     elif 100>=usage>0:
#         bill=(usage*5)
#         print(bill)
#     else:
#         print("Enter your usage correctly")
#     total+=bill
#     if bill>3000:
#         print("High")
#     if 3000>=bill>=1000:
#         print("Medium")
#     if bill<1000:
#         print("low")
# print(f"The total revenue is Rs.{total}")
# #14.
# sentence=input("Enter a sentence: ").split()
# length=len(sentence)
# for i in range(length):
#     word=sentence[i]
#     vowel=0
#     consonant=0
#     for char in word:
#         if char in "aeiouAEIOU":
#             vowel+=1
#         elif char.isalpha():
#             consonant+=1
#     if vowel>consonant:
#         print("Vowel heavy")
#     elif vowel<consonant:
#         print("Consonant heavy")
#     else:
#         print("Balanced")
# #15.
# order=int(input("Enter the order of square matrix: "))
# even = 0
# odd = 0
# negative = 0
# positive = 0
# zero = 0
# largest=None
# for i in range(order):
#     for j in range(order):
#         element=int(input("Enter the elements of the matrix: "))
#         if element%2==0:
#             even+=1
#         elif element%2==1:
#             odd+=1
#         if element>0:
#             positive+=1
#         elif element<0:
#             negative+=1
#         elif element==0:
#             zero+=1
#         if element>largest:
#             largest=element
# print(f"The total even no is {even} and odd no is {odd} and positive no is {positive} and negative no is {negative} and zero is {zero}.")
# print(f"THe largest element is {largest}.")
# #16.
# upper=0
# lower=0
# digit=0
# special_char=0
# highest_percentage=0
# highest_category=""
# password=input("Enter your password: ")
# length=len(password)
# for i in range(length):
#     password[i]
#     if password[i].islower():
#         lower+=1
#     elif password[i].isupper():
#         upper+=1
#     elif password[i].isdigit():
#         digit+=1
#     else:
#         special_char+=1
#     perc1=lower*100/length
#     perc2=upper*100/length
#     perc3=digit*100/length
#     perc4=special_char*100/length
#     if perc1>highest_percentage:
#         highest_percentage=perc1
#         highest_category="Lowercase"
#     elif perc2>highest_percentage:
#         highest_percentage=perc2
#         highest_category="Uppercase"
#     elif perc3>highest_percentage:
#         highest_percentage=perc3
#         highest_category="digit"
#     elif perc4>highest_percentage:
#         highest_percentage=perc4
#         highest_category="Special Character"
# print(f"The highest percentage of password is {highest_percentage} and is {highest_category}")
# #17.
# vowel=0
# consonant=0
# hig_marks=0
# topper=""
# for i in range(5):
#     name1=input("Enter your name: ")
#     name=name1.split()
#     length=len(name)
#     highest_alphabet=""
#     for j in range(length):
#         words=name[j]
#         for char in words:
#             if char in "aeiouAEIOU":
#                 vowel+=1
#             elif char.isalpha():
#                 consonant+=1
#             else:
#                 print("Enter a valid name")
#     marks=int(input("Enter your marks: "))
#     if marks>=90:
#         grade="A"
#     elif marks>=80:
#         grade="B"
#     elif marks>=70:
#         grade="C"
#     elif marks>=60:
#         grade="D"
#     elif marks>=50:
#         grade="E"
#     else:
#         grade="Fail"

#     if vowel>consonant:
#         highest_alphabet="Vowel"
#     else:
#         highest_alphabet="Consonant"
#     total_char=vowel+consonant
#     if marks>hig_marks:
#         hig_marks=marks
#         topper=name1
#     print(f"{name1} has got {grade} grade.")
#     print(f"Total no. of vowels are {vowel} and consonants are {consonant}.")
#     print(f"The total characters in students name is {total_char}.")
#     print(f"The name has more {highest_alphabet} alphanets.")
# print(f"{topper} has got the maxm marks and is {hig_marks} marks.")
# #18.
# total_bal=0
# count=0
# for i in range(7):
#     day=input("Enter day name: ")
#     number1=int(input("Enter total number of deposites done on that day: "))
#     number2=int(input("Enter total number of withdrawals done on that day: "))
#     for j in range(number1):
#         dep=int(input("Enter the deposit amount: "))
#         if dep>0:
#             total_bal+=dep
#             count+=1
#             print(f"Your updated Balance is Rs.{total_bal}.")
#         else:
#             print("Please enter the valid amount.")
#     for k in range(number2):
#         withdraw=int(input("Enter the Withdrawal amount: "))
#         total_bal-=withdraw
#         count+=1
#         if withdraw>0 and withdraw%100==0 and total_bal>=0:
#             print(f"Your updated Balance is Rs.{total_bal}.")
#         elif total_bal<0:
#             print("Insufficient amount.")
#         else:
#             print("Enter the valid Amount.")
#         if total_bal<1000:
#              print("Low Balance")
# print(f"The total balance is {total_bal} and total number of transactions done is {count}.")
# #19.
# digits=False
# url_text=False
# special_char=False
# sent=input("Enter a sentence: ").split()
# length=len(sent)
# for i in range(length):
#     word=sent[i]
#     for char in word:
#         if char.isdigit():
#             digits=True
#         if char in ".:/":
#             url_text=True
#         else:
#             special_char=True
# if digits==url_text==special_char==True:
#     print("Safe")
# elif digits==url_text==True or url_text==special_char==True or digits==special_char==True:
#     print("Review")
# else:
#     print("Suspecious")
# #20.
# n=int(input("Enter the range for the grid: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         product=i*j
#         if product%5==0:
#             print("F",end="")
#         elif product%2==0:
#             print("E",end="")
#         else:
#             print("O",end="")
#     print()
# #21.
# total_discount=0
# disc1=0
# disc2=0
# disc3=0
# disc4=0
# for i in range(10):
#     price=inr(input("Enter the price of product: "))
#     if price>=5000:
#         disc=(price/5)
#         total_discount+=disc
#         final_price=price-disc
#         disc1+=1
#         print(f"The final price of the product is Rs.{final_price}.")
#     elif price>=3000:
#         disc=(price*15/100)
#         total_discount+=disc
#         final_price=price-disc
#         disc2+=1
#         print(f"The final price of the product is Rs.{final_price}.")
#     elif price>=1000:
#         disc=(price*10/100)
#         total_discount+=disc
#         final_price=price-disc
#         disc3+=1
#         print(f"The final price of the product is Rs.{final_price}.")
#     else:
#         disc=0
#         total_discount+=disc
#         final_price=price-disc
#         disc4+=1
#         print(f"The final price of the product is Rs.{final_price}.")
# print(f"The person has got the 20% off for {disc1} items and 15% off for {disc2} items and 10% off for {disc3} items and no discount for {disc4} items.")
# print(f"The total discount amount is {total_discount}.")
# #22.
# str=input("Enter the repeting string: ")
# length=len(str)
# for i in range(length):
#     char=str[i]
# #23.
# junior=0
# mid=0
# senior=0
# executive=0
# total_salary=0
# for i in range(8):
#     salary=input("Enter your salary: ")
#     if salary>100000:
#         executive+=1
#         total_salary+=salary
#         print("Executive")
#     elif salary>50000:
#         senior+=1
#         total_salary+=salary
#         print("Senior")
#     elif salary>25000:
#         mid+=1
#         total_salary+=salary
#         print("Mid")
#     elif salary<=25000:
#         junior+=1
#         total_salary+=salary
#         print("Junior")
# print(f"The total {executive} are executives and {senior} are seniors and {mid} are mediokers and {junior} are juniors.")
# print(f"The average salary of all is Rs.{total_salary/8}")
# #24.
# count=0
# sent=input("Enter your sentence: ").split()
# secr=input("Enter the secret word: ")
# length=len(sent)
# for i in range(length):
#     word=sent[i]
#     if word==secr:
#         count+=1
# if count==0:
#         print("Secret word not found")
# else:
#     print(f"The secret word is {secr} and it occurs {count} times in sentence.")
#25.



# #26.
# total=0
# outstanding=0
# excellent=0
# good=0
# average=0
# poor=0
# for i in range(10):
#     rating=float(input("Enter the rating of the movie: "))
#     if 10>=rating>=9.1:
#         print("Outstanding")
#         outstanding+=1
#         total+=rating
#     elif 9>=rating>=7.1:
#         print("Excellent")
#         excellent+=1
#         total+=rating
#     elif 7>=rating>=5.1:
#         print("Good")
#         good+=1
#         total+=rating
#     elif 5>=rating>=3.1:
#         print("Average")
#         average+=1
#         total+=rating
#     elif 3>=rating>=0:
#         print("Poor")
#         poor+=1
#         total+=rating
# print(f"The total no. of movie who got Outstanding ratings are {outstanding} and no. of movies which has got the excellent rating is {excellent} and no. of good movies are {good} and no. of average {average} and number of poor movies are {poor}.")
# print(f"The Average rating for these movies are {total/10}.")
# #27.
# sentence=input("Enter a sentence: ").split()
# length=len(sentence)
# for i in range(length):
#     word=sentence[i]
#     count=0
#     for j in range(length):
#         if word==sentence[j]:
#             count+=1
#     if count>1:
#         print(f"{word} appears {count} times.")
#28.
even=0
highest_digit=0
highest_num=0
for i in range(10):
    num=input("Enter an integer: ")
    length=len(num)
    for i in range(length):
        digit=num[i]
        if digit in "02468":
            even+=1
    if even>highest_digit:
        highest_digit=even
        highest_num=num
        print(f"{highest_num} has highest number of even digits.")
    elif 