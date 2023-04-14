# Присвойте двум переменным любые числовые значения.
num1 = 10
num2 = 20


# Используя переменные из п. 1, с помощью
# оператора and составьте два сложных логических выражения,
# одно из которых дает истину, другое – ложь.
res1 = num1 < 15 and num2 != 7
res2 = num1 > 11 and num2 < 30
print(res1)
print(res2)


# Аналогично выполните п. 2, но уже с оператором or.
res1 = num1 < 15 or num2 != 7
res2 = num1 > 11 or num2 < 30
print(res1)
print(res2)


# Попробуйте использовать в логических выражениях переменные
# строкового типа. Объясните результат.
str1 = "Yes"
str2 = "No"
res3 = str1 == str2 # проверяет схожесть двух строк. Если похжи - true, если нет - false
print(res3)


# Напишите программу, которая запрашивала бы у пользователя
# два числа и выводила бы True или False в зависимости от того,
# больше первое число второго или нет.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = number1 > number2
print(result)


# Даны два целых числа. Выведите значение наименьшего из них.
number1 = 8
number2 = 6
print(min(number1, number2))


# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0.
# Для данного числа x выведите значение sign(x). Эту задачу
# желательно решить с использованием каскадных инструкций if...
# elif... else.
x = int(input("Enter number: "))
if x > 0:
    print("sign(x) = 1")
elif x < 0:
    print("sign(x) = -1")
else:
    print("sign(x) = 0")


# Дано натуральное число. Требуется определить, является ли год
# с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в
# соответствии с григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен 100, а также
# если он кратен 400.
year = int(input("Enter number year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")

# Даны три целых числа. Выведите значение наименьшего из них.
number1 = 17
number2 = 9
number3 = 12
print(min(number1, number2, number3))

# Даны три целых числа. Определите, сколько среди них
# совпадающих. Программа должна вывести одно из чисел: 3
# (если все совпадают), 2 (если два совпадает) или 0 (если все
# числа различны).
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number "))
if number1 == number2 == number3:
    print(3)
elif number1 == number2 or number1 == number3 or number2 == number3:
    print(2)
else:
    print(0)

