""""
    Обработка исключений
    
    Части программы, в которых возможно появление ошибок, например, работающие с пользовательским
вводом, разрешается заключать в специальные блоки try-exept, с помощью которых можно обрабатывать
"исключительные ситуации".
    Инструкции, способные вызвать ошибки группируются в блок try.
    Команды, способные обрабаоть ошибки - в блок except.
    После может стоять необязательный блок finally, где описываются инструкции, которые должны
выполниться после обработки всех исключений.
    
    В Python есть множество типов ислкючений, например NameError, которое происходит, если имя
переменной не найдено.
    IndexError - при попытке обращения к несуществующему индексу.
    ValueError - при передаче агрумента с некорректным значением во встроенную операцию.

Каждое  исключение возвращает сообщение с описательной информацией, которое можно использовать,
присвоив его какой-нибудь переменной с помощью ключевого слова as, чтобы отобразить природу
происхождения исключения.

    Инструкции в блоке try выполняются до тех пор, пока не вызовется исключение.
"""""

# Задание 1
# 1. Проинициализировать переменную со строковым значением.

title = 'Python in easy steps'

# 2. Добавить инструкцию try, в котором производится попытка вывести значение переменной, но ее имя,
# указать неверно

try:
    print(titel)

# 3. Добавить блок инструкции exept для вывода сообщения об ошибке.

# except NameError as msg:
#     print(msg)

# 4. Для обработки множества исключений внутри блока except нужно в скобках через запятую указать типы
# этих исключений

except(NameError, IndexError) as msg:
    print(msg)

# Задание 2
# 1. Проинициализировать целочисленную переменную

day = 32

# 2. Добавить блок инструкции try, в котором проверяется значение переменной, затем указывается
# исключение и соответсвующее сообщение для пользователя.

try:
    if day > 31:
        raise ValueError('Invalid day Number')
    # Добавляем операторы

# 3. Добавить блок инструкций except для вывода сообщения в случае появления исключения ValueError

except ValueError as msg:
    print('The programm fount an', msg)

# 4. Добавить блок инструкций finally для вывода сообщения после успешной обработки исключения.

finally:
    print('But today is beautiful anyway.')