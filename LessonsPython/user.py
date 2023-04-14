# Напишите программу (файл user.py), которая запрашивала бы у пользователя:
# - его имя (например, “What is your name?”)
# - возраст (“How old are you?”)
# - место жительства (“Where are you live?”)
# После этого выводила бы три строки:
# “This is имя”
# “It is возраст”
# “S)he live in место_жительства”
# Вместо имя, возраст, место_жительства должны быть данные, введенные пользователем.

first_name = input("What is your name? ")
age = int(input("How old are you? "))
house = input("Where are you live? ")
print("This is", first_name)
print("It is", age)
print("Lives in", house)