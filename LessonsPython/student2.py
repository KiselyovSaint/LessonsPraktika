# Переменные.

# Создаём переменную:
number = 5

# Вывод переменной:
print(number)

# Изменение значения переменной:
number = 7
print(number)

# Комбинирование
print("Результат: ", number)

# Удаление переменной:
del number

# Создаём переменные:
digit = 4.54356876
word = "Результат:"
# Вывод:
print(word, digit)

# Создаём переменную (bool)
booleanOne = True
booleanTwo = False
print(word, booleanOne)


# Типы данных

var_int = 5 # тип данных int (целые числа)
var_float = 5.721 # тип данных float (числа с плавающей точкой)
var_str = "Hello" # тип данных string (строка)
var_bool = True # тип данных bool (Логический тип данных, Истина/Ложь, True/False)


# Приведение типов (преобразования переменной одного типа данных в другой)

# Пример 1. str
result = "Результат:"
number_one = 10
print(result + str(number_one))

# Пример 2. int
str_num = "5"
number_two = 12
print(result, int(str_num) + number_two)

# Пример 3. str и int вместе
print(result + str(int(str_num) + number_two))

# Аналогично можно и с float, и с bool


# Получение данных, input(). Пример использования:
# По умолчанию введённое значение является типом STRING, поэтому указываем int
num1 = int(input("Введите первое число: ")) # В переменную num1 добавится введённое значение
num2 = int(input("Введите второе число: ")) # В переменную num2 добавится введённое значение

# Вывод введённых значений:
print(num1)
print(num2)

# Сложение введённых значений и вывод результата:
print("Результат:", num1 + num2)

# Различные способы изменения значения переменной:
number_sposob = 2
print(number_sposob)

# Изменяем:
number_sposob = number_sposob + 3
print(number_sposob)
# Или
number_sposob += + 3
print(number_sposob)

# Умножение строк (вывод строки n-е количество раз)
message = "Hello"
print (message * 3) # Вывод 3 раза Hello


# У одной переменной можно менять тип данных изменяя лишь значение

# test имеет тип string
test = "Text"
print (test)

# теперь test имеет тип int
test = 70
print (test)