"""
    Доступ к файлам, стр. 108, МакГрат

    Если с помощью dir() проверить модуль _builtins__, то найдем объект file, который определят
несколько методов для работы с файлами системы, включая такие методы как, open(), read(), write(),
close().
    Перед тем, как что-то читать из файла, его требуется открыть методом open().
    Аргументы, описывающие открытие файла - строковые величины и заключаются в кавычки.

Файловый режим  Операция
    r           Открыть для чтения сущ. файл.
    w           Открыть для записи сущ. файл. (Создает новый или открывает существующий и стирает его содержимое).
    a           Режим добавления текста. Открывает или созадет файл для записи в конец файла.
    r+          Открывает текстовый файл для чтения или записи.
    w+          Открывает текстовый файл для записи или чтения.
    a+          Открыть или создать текстовый файл для чтения или записи в конец файла.

    ! Если после любого из перечисленных режимов добавить символ b, то операция будет относиться не к текстовому, а к
    двоичному файлу. Например rb или w+b
    ! Метод readlines() возвращает список всех строк.

    После открытия файла появляется метод file, с помощью свойств последнего можно получить различные подробности,
относящиеся к данному файлу.

Свойство    Описание
name        Имя открываемого файла
mode        Режим открытия файла
closed      Возвращает True, если файл был закрыт, и False - если нет.
readable()  Логическая величина, определяющая, установлено ли на файл разрешение по чтению (True или False)
writable()  Логическая величина, определяющая, установлено ли на файл разрешение по записи (True или False)

    ! Если попытаться открыть несуществующий файл в режиме r, программа сообщит об ошибке.
"""

# Задачи:
# 1. Создать файловый объект, которым будет новый текстовый файл с именем example.txt для записи содержимого в него.

file = open('example.txt', 'w')

# 2. Вывести имя файла и режим его открытия.

print('File name:', file.name, '\nOpen mode:', file.mode)

# 3. Вывести разрешения на доступ к файлу.

print('Readable:', file.readable())
print('Writable:', file.writable())

# 4. Определить функцию, задающую состояние файла.

def get_status(f) :
    if (f.closed !=False) :
        return 'Closed'
    else :
        return 'Open'

# 5. Ввывести тек. состояние файла, затем закрыть и вывести состояние еще раз.

print('File status', get_status(file))
file.close()
print('File status', get_status(file))