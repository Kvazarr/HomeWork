# try:
#     number_str = input("Enter your number for conversion: ")
#     number_int = int(number_str)
#     print(f"Int_number(type: {type(number_int)}, value: {number_int})")
# except ValueError:
#     print("Please, enter valid number")

def Func_within(number_str):
    print("Func within:")
    number_int = int(number_str)
    print(f"\tInt_number(type: {type(number_int)}, value: {number_int})")


def Func_outside(number_str):
    try:
        print("Func outside: ")
        number_int = int(number_str)
        print(f"\tInt_number(type: {type(number_int)}, value: {number_int})")
    except ValueError:
        print("\tPlease, enter valid number")


number_str = input("Enter your number for conversion to integer: ")


try:
    Func_within(number_str)
except ValueError:
    print("\tPlease, enter valid number")


Func_outside(number_str)
