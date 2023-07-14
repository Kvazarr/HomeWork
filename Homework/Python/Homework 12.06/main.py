# user_number = int(input("Enter your number to check: "))

# if user_number % 2 == 0:
#     print("Even number")
# elif user_number % 2 != 0:
#     print("Odd number")


# user_number = int(input("Enter your number to check: "))

# if user_number % 7 == 0:
#     print("Number is a multiple of 7")
# elif user_number % 7 != 0:
#     print("Number is a not multiple of 7")


# user_number1 = int(input("Enter your first number to check: "))
# user_number2 = int(input("Enter your second number to check: "))

# if user_number1 > user_number2:
#     print(f"Max number is: {user_number1}")
# else:
#     print(f"Max number is: {user_number2}")


# user_number1 = int(input("Enter your first number to check: "))
# user_number2 = int(input("Enter your second number to check: "))

# if user_number1 > user_number2:
#     print(f"Min number is: {user_number2}")
# else:
#     print(f"Min number is: {user_number1}")


# user_number1 = int(input("Enter your first number to check: "))
# user_number2 = int(input("Enter your second number to check: "))
# user_choice = input(
#     "What u want? - a)Sum; b)Difference; c)Average; d)Dobutok;\nEnter ur choice: ")

# if user_choice == 'a':
#     print(f"Sum of numbers: {user_number1+user_number2}")
# elif user_choice == 'b':
#     if user_number2 > user_number1:
#         print(f"Difference of numbers: {user_number2-user_number1}")
#     else:
#         print(f"Difference of numbers: {user_number1-user_number2}")
# elif user_choice == 'c':
#     print(f"Aripfhmatic average of numbers: {(user_number1+user_number2)/2}")
# elif user_choice == 'd':
#     print(f"Dobutok of numbers: {user_number1*user_number2}")
# else:
#     print("Wrong choice...Omg")


# user_day = int(input("Enter using numbers day of week u want to know: "))

# if user_day == 1:
#     print("Monday!")
# elif user_day == 2:
#     print("Tuesday!")
# elif user_day == 3:
#     print("Wednesday!")
# elif user_day == 4:
#     print("Thursday!")
# elif user_day == 5:
#     print("Friday!")
# elif user_day == 6:
#     print("Saturday!")
# elif user_day == 7:
#     print("Sunday!")
# else:
#     print("Wrong choice.")


# user_month = int(input("Enter using numbers the month u want to know: "))

# if user_month == 1:
#     print("January!")
# elif user_month == 2:
#     print("February!")
# elif user_month == 3:
#     print("March!")
# elif user_month == 4:
#     print("April!")
# elif user_month == 5:
#     print("May!")
# elif user_month == 6:
#     print("June!")
# elif user_month == 7:
#     print("July!")
# elif user_month == 8:
#     print("August!")
# elif user_month == 9:
#     print("September!")
# elif user_month == 10:
#     print("November!")
# elif user_month == 11:
#     print("October!")
# elif user_month == 12:
#     print("December!")


# user_number = int(input("Enter ur number to check: "))

# if user_number > 0:
#     print("Number is positive!")
# elif user_number < 0:
#     print("Number is negative!")
# elif user_number == 0:
#     print("Number is equal to zero")


user_number1 = int(input("Enter first number: "))
user_number2 = int(input("Enter second number: "))

if user_number1 == user_number2:
    print("numbers equal!")
elif user_number1 < user_number2:
    print(user_number1, user_number2)
elif user_number1 > user_number2:
    print(user_number2, user_number1)
