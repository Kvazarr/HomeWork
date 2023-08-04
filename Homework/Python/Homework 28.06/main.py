# exit = False
# name = []

# while exit != True:
#     word = input(f"Enter files name: ")
#     name.append(word)

#     if word == "quit":
#         files = open('file', 'w')
#         name_str = ' '.join(name)
#         files.write(name_str)
#         files.close()
#         exit = True

# files = open('file', 'r')
# print(files.read())
# files.close()

name = []
exit = False

while exit != True:
    word = input("Enter files name: ")
    name.append(word)

    if word == 'quit':
        name_str = ' '.join(name)
        exit = True

temp = set(name_str)
name_str = ' '.join(temp)
long = len(name_str)
space = ' '

files = open('file', 'w')
for i in range(long):
    if name_str[i] == space:
        continue
    files.write(f"{name_str[i]} ")
files.close()

files = open('file', 'r')
print(files.read())
files.close()
