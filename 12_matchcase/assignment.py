# # 1.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("You selected pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected pasta")
#     case 4:
#         print("You selected sandwich")
#     case _:
#         print("Invalid menu choice")
# # 2.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("wifi")
#     case 2:
#         print("bluetooth")
#     case 3:
#         print("Mobile data")
#     case 4:
#         print("Airplane mode")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid setting")
# # 3.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("check balance")
#     case 2:
#         print("withdraw money")
#     case 3:
#         print("Deposit Money")
#     case 4:
#         print("Change Pin")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")
# # 4.
# choice=input("Enter traffic signal colour: ").lower()
# match choice:
#     case "red":
#         print("Stop")
#     case "Yellow":
#         print("wait")
#     case "green":
#         print("go")
#     case _:
#         print("Invalid colour")
# # 5.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("View profile")
#     case 2:
#         print("view course")
#     case 3:
#         print("View Marks")
#     case 4:
#         print("View Attendance")
#     case 5:
#         print("Log out")
#     case _:
#         print("Invalid choice")
# # 6.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")
# # 7.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Account balance")
#     case 2:
#         print("mini statement")
#     case 3:
#         print("Fund Transfer")
#     case 4:
#         print("Bill Payment")
#     case 5:
#         print("Customer support")
#     case _:
#         print("Invalid choice")
# # 8.
# choice=int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Morning show")
#     case 2:
#         print("Afternoon show")
#     case 3:
#         print("Evening show")
#     case 4:
#         print("Night show")
#     case _:
#         print("Invalid choice")
# # 9.
# choice=input("Enter the weather condition: ").lower()
# match choice:
#     case "sunny":
#         print("Wear sunglasses")
#     case "rainy":
#         print("Carry an umbrella")
#     case "Cloudy":
#         print("weather may rain")
#     case "snowy":
#         print("wear warm clothes")
#     case _:
#         print("Unknown weather")
# # 10.
# choice=input("Enter the Payment method: ").lower()
# match choice:
#     case "upi":
#         print("UPI payment method selected")
#     case "card":
#         print("Card as a payment method selected")
#     case "Cash":
#         print("Cash as a payment method selected")
#     case "wallet":
#         print("wallet as a payment method selected")
#     case _:
#         print("Unknown payment method")
# # 11.
# file=input("Enter the type of file: ")
# match file:
#     case "pdf":
#         print("Document")
#     case "jpg":
#         print("Image")
#     case "png":
#         print("Image")
#     case "mp3":
#         print("Audio")
#     case "mp4":
#         print("Video")
#     case _:
#         print("Unknown file type")
# # 12
# type=input("Enter account type: ").strip().lower()
# match type:
#     case "admin":
#         print("full access")
#     case "teacher":
#         print("Teacher Dashboard")
#     case "Student":
#         print("Student Dashboard")
#     case "guest":
#         print("Limited Access")
# # 13.
# day=int(input("Enter a day number: "))
# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Invalid day schedule")
# # 14.
# priority=int(input("Enter the number of priority: "))
# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3|4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Input")
# # 15.
# level=int(input("Enter membership level: "))
# match level:
#     case 1 | 2:
#         print("Basic membership")
#         if level==1:
#             print("Bronze")
#         else:
#             print("Silver")
#     case 3 | 4 :
#         print("Advance membership ")
#         if level==3:
#             print("Gold")
#         else:
#             print("Platinum")
#     case _:
#         print("Invalid level")
# # 16.
# print("""Please Enter......
# 1 for Students
# 2 for teachers""")
# num=int(input("Enter the code: "))
# match num:
#     case 1:
#         print("""Enter 1 for Viewing course
#         2 for viewing marks
#         3 for viewing Attandence""")
#         choice=int(input("Enter your choice: "))
#         match choice:
#             case 1:
#                 print("Your course is B.tech")
#             case 2:
#                 print("You got 89 marks")
#             case 3:
#                 print("You are maintaining 100 percent attendance")
#             case _:
#                 print("Invalid input")
#     case 2:
#         print("""Enter 1 for Viewing students
#         2 for viewing marks
#         3 for viewing Attandence""")
#         choice=int(input("Enter your choice: "))
#         match choice:
#             case 1:
#                 print("Your students are...")
#             case 2:
#                 print("You got 89 marks")
#             case 3:
#                 print("You are maintaining 100 percent attendance")
#             case _:
#                 print("Invalid input")
#     case _:
#         print("Invalid output")
# 17.
