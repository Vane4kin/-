score = 0

print("1. Що покаже цей код?")
print("for i in range(5):")
print("  if i % 2 == 0:")
print("    continue")
print("  print(i)")
print("Числа: 1, 3 та 5")
print("Помилка через неправильне виведення інформації")
print("Помилка, тому що i не присвоєна")
print("Числа: 1 та 3")
print("Числа: 0, 2 та 4")
answer = input("Ваша відповідь: ")
if answer == "Числа: 1 та 3":
    score += 1

print("\n2. Що буде результатом цього коду?")
print("x = 23")
print("num = 0 if x > 10 else 11")
print("print(num)")
print("10")
print("Помилка")
print("0")
print("11")
print("23")
answer = input("Ваша відповідь: ")
if answer == "23":
    score += 1

print("\n3. Яка функція виводить щось у консоль?")
print("print();")
print("out();")
print("write();")
print("log();")
answer = input("Ваша відповідь: ")
if answer == "print();":
    score += 1

print("\n4. Скільки бібліотек можна імпортувати в один проект?")
print("Не більше 10")
print("Не більше 3")
print("Необмежену кількість")
print("Не більше 5")
print("Не більше 23")
answer = input("Ваша відповідь: ")
if answer == "Необмежену кількість":
    score += 1

print("\n5. Що покаже цей код?")
print("for j in 'Hi! I\\'m mister Robert':")
print("  if j == '\\\\':")
print("    print(\"Знайдено\")")
print("    break")
print("else:")
print("  print (\"Готово\")")
print("\"Знайдено\"")
print("\"Готово\"")
print("\"Знайдено\" та \"Готово\"")
print("Помилка коду")
answer = input("Ваша відповідь: ")
if answer == "\"Знайдено\"":
    score += 1

print("\n6. Де правильно створено змінну?")
print("$num = 2")
print("Немає відповідного варіанта")
print("num = float(2)")
print("int num = 2")
print("var num = 2")
answer = input("Ваша відповідь: ")
if answer == "num = float(2)":
    score += 1

print("\n7. Що буде показано в результаті?")
print("name = \"John\"")
print("print('Hi, %s' % name)")
print("\"Hi, John\"")
print("Помилка")
print("\"Hi, name\"")
print("\"Hi, \"")
answer = input("Ваша відповідь: ")
if answer == "\"Hi, John\"":
    score += 1

print("\n8. Які помилки допущені у коді нижче?")
print("def factorial(n):")
print("  if n == 0:")
print("    return 1")
print("  else:")
print("    return n * factorial(n - 1)")
print("print(factorial(5))")
print("Необхідно вказати тип значення, що повертається")
print("У коді немає жодних помилок")
print("Функція не може викликати сама себе")
print("Функція завжди буде повертати 1")
answer = input("Ваша відповідь: ")
if answer == "У коді немає жодних помилок":
    score += 1

print("\n9. Яка бібліотека відповідає за час?")
print("clock")
print("time")
print("localtime")
print("Time")
answer = input("Ваша відповідь: ")
if answer == "time":
    score += 1

print("\n10. Як отримати дані від користувача?")
print("Використати метод input()")
print("Використати метод get()")
print("Використати метод read()")
print("Використати метод readLine()")
print("Використати метод cin()")
answer = input("Ваша відповідь: ")
if answer == "Використати метод input()":
    score += 1

print("\nВаш результат: ", score, " з 10")
