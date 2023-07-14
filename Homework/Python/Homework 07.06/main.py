# print("Enter three numbers in terminal.")

# first = int(input("First number:  "))
# second = int(input("Second number: "))
# thirth = int(input("Thirth number: "))

# choice = int(input("What u want - 1)Sum; 2)Dobutok;\nEnter: "))

# if choice == 1:
#     print(f"Sum of numbers: {first+second+thirth}")
# elif choice == 2:
#     print(f"Dobutok of numbers: {(first*second*thirth)/3}")

# ================================================================

# print("Enter three numbers in terminal.")

# first = int(input("First number:  "))
# second = int(input("Second number: "))
# thirth = int(input("Thirth number: "))

# choice = int(input("What u want - 1)Max; 2)Min; 3)Average\nEnter: "))

# if choice == 1:
#     temp = first
#     if second > temp:
#         temp = second
#     if thirth > temp:
#         temp = thirth

#     print(f"Max value: {temp}")

# elif choice == 2:
#     temp = first
#     if second < temp:
#         temp = second
#     if thirth < temp:
#         temp = thirth

#     print(f"Min value: {temp}")

# elif choice == 3:
#     print(f"Aripfhmatic average: {(first+second+thirth)/3}")

# ================================================================

meters = int(input("Enter quantity of meters: "))
choice = int(input(
    f"What u want? - 1)meters in miles; 2)meters in inches; 3)meters in yards;\nEnter: "))

if choice == 1:
    print(
        f"Mile-to-Meter conversion: {meters} meters ->  Miles {meters/1609.34}")
elif choice == 2:
    print(
        f"Inches-to-Meter conversion: {meters} meters ->  Inches {meters*39.37}")
elif choice == 3:
    print(
        f"Yards-to-Meter conversion: {meters} meters ->  Yards {meters*1.09361}")
