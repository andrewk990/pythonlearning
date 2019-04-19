"""
    Работа с временем:

    Для работы с системным временем используется модуль datetime, содержащий объект datetime с атрибутами
year, month, day, hour, minute, second, microsecond.
    Объект datetime содержить метод today(), который присваивает атрибутам объекта значение текущей даты и времени
и возвращает их в виде кортежа. Она так же содержит метод getattr(), который требует 2 аргумента, указывающих имя
объекта и атрибут, который нужно получить.
    Альтернативным способом для доступа к атрибуту может служить точечная запись вида datetime.year.
    Все значения в объекте datetime хранятся в виде числовых величин, но могут быть преобразованы в текстовые
эквиваленты с помощью метода strftime(). Данный метод требует передачи единственного строкового аргумента (так
называемой директивы), указывающего, какую часть кортежа и в каком формате вернуть.

    Список возможных директив:
Директива:  Возвращаемое значение:
    %A      полное название дня недели (%a - для сокращенного)
    %B      полное название месяца (%b - для сокращенного)
    %c      дата и время (локальные)
    %d      порядковый номер дня в месяце от 1 до 31
    %f      кол-во микросекунд от 0 до 999999
    %H      десятичное представление часа от 0 до 23 (для 24-часового формата)
    %I      десятичное представление часа от 0 до 12 (для 12-часового формата)
    %j      порядковый номер дня в году от 0 до 366
    %m      порядковый номер месяца от 1 до 12
    %M      десятичное представление минут от 0 до 59
    %p      обозначение AM (до полудня), PM (после полудня)
    %S      десятичное представление секунд от 0 до 59
    %w      порядковый номер дня в неделе от 0 (вс.) до 6 (сб.)
    %W      порядковый номер недели в году от 0 до 53
    %X      локальное время (%x - локальная дата)
    %Y      полное десятичное представление года от 0001 до 9999
            (%y - для краткого представления от 00 до 99)
    %z      смещение часового пояса от UTC в виде +ЧЧММ или -ЧЧММ
    %Z      название часового пояса

!!! Поскольку объект datetime находится в модуле с тем же именем, простое импортирование модуля означает, что к нему
можно будет обращаться так: datetime.datetime.
!!! Используя импорт через from datetime import * позволит упростить запись до datetime.
!!! Для присвоения новыз значений отрибутам объекта datetime можно использовать метод replace().
    Пример:
        today = today.replace(year=2019)
"""

# Задания:

# 1. Импортировать модуль datetime, чтобы сделать доступными его функции

from datetime import *

# 2. Создать объект datetime и присвоить его атрибутам текущее значение даты и времени, вывести результат.

today = datetime.today()
print('Today is:', today)

# 3. Добавить цикл для вывода занчения каждого атрибута отдельно.

for attr in \
    ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond'] :
    print(attr, ':\t', getattr(today, attr))

# 4. Вавести значение времени используя точечную запись.

print('Time: ', today.hour, ':', today.minute, sep = '')

# 5. Присвоить day и month форматированное значение.

day = today.strftime('%a.')
month = today.strftime('%B')

# 6. Вывод форматированной даты:

print('Date:', day, month, today.day)