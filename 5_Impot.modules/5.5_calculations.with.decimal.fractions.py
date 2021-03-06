"""
    При ииспользовании в программах арифметических вычилений с числами с плавающей точкой
могут возникать погрешности. Это обучловлено округлением десятичных дробей.
"""

# Задания:
# 1. Инициализировать переменные с плавающей точкой.

item_1 = 0.70 # Пункт
rate_1 = 1.05 # Налог

# 2. Проинициализировать еще 2 переменные путем арифметических операций над вышеописанными.

tax_1 = item_1 * rate_1   # Ставка
total_1 = item_1 + tax_1  # Всего

# 3. Вывести форматированные значения  переменных, использующих 2 знака после запятой для дробей.

print('Item:\t', '%.2f' % item_1)
print('Tax:\t', '%.2f' % tax_1)
print('Total:\t', '%.2f' % total_1)

print('\nItem:\t', '%.20f' % item_1)
print('Tax:\t', '%.20f' % tax_1)
print('Total:\t', '%.20f' % total_1)

"""
    Очевидно, что значение tax немного меньше, чем 0,735, поэтому оно округлено до 0,73. А значение
total чуть выше чем, 1,435, поэтом округлено до 1,44.
    Чтобы избежать таких ошибок при выполнении арифметических операций над числами с плавающей точкой
используется модуль decimal.
В финансовой отчетности повсеместно используется Decimal().
"""

# 4. Импортирвоать модуль decimal.

from decimal import *

# 5. Отредактировать первые 2 инструкции присваивания:

item_2 = Decimal(0.70)
rate_2 = Decimal(1.05)

# 6. Значения tax и total округлены вниз.

tax_2 = item_2 * rate_2   # Ставка
total_2 = item_2 + tax_2  # Всего

print('\nItem:\t', '%.20f' % item_2)
print('Tax:\t', '%.20f' % tax_2)
print('Total:\t', '%.5f' % total_2)

# TODO: Почему decimal() считается более точным, если в данном примере 1.435 округлется до 1.43 ???