list_1 = []
list_2 = []
list_3 = []

user_text_main = input("Enter your text: ")
user_text_v2 = input("Enter register word u want to find: ")

list_1 = user_text_main.split()
list_2 = user_text_v2.split()

for word in list_1:
    if word.lower() in list_2:
        list_3.append(word.upper())
    else:
        list_3.append(word)

user_text_main = ' '.join(list_3)

print(user_text_main)
