import sys
from array import array
import array
import numpy as np

"""типы данных питона
динамическая утилизация - в процессе работы определяется тип переменной автоматически в процессе выполнения
"""
"""x=1
print(type(x))
print(sys.getsizeof(x))

x='hello'
print(type(x))
print(sys.getsizeof(x))

x= True
print(type(x))
print(sys.getsizeof(x))"""

"""l1= list([])
print(sys.getsizeof(l1))

l2=list([1,2,3])
print(sys.getsizeof(l2))

l3=list([1,'2',True])
print(sys.getsizeof(l3))
#list хранит различные типы данных вместе
#но нам он не нравится т.к. медленная скорость обработки данных
"""
"""
a1=array.array('i',[1,2,3]) # 'i' - means we have ints in array
print(type(a1))
print(sys.getsizeof(a1))
#хранит типы только одного типа, уже лучше чем list, но все равно не самый лучщий
# focus on storage numpy better since it also focus on actions
"""

# Задание 1. Какие еще существуют коды типов?
# Задание 2. Напишите код, подобный приведенному выше, но с другим типом
"""a=np.array([1,2,3,4,5])
print(type(a),a)

#повышающее повышение типов
a=np.array([1.23,2,3,4,5])
print(type(a),a)

a=np.array([1.23,2,3,4,5], dtype=int)
print(type(a),a)

# многомерные  массивы

a= np.array([range(i,i+3) for i in [2,4,6]])
print(a,type(a))"""
"""
a=np.zeros(10, dtype=int)
print(a)
print(np.ones((3,5),dtype=float))
print(np.full((4,5),3.1415))
print(np.arange(0,20,2))
print(np.eye(4))"""
# Задание 3. Напишите код для создания массива с 5 значениями распоплагающимися через разные интервалы в диапазоне от 0 до 1
# Задание 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
# Задание 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1
# Задание 6. Напишите код для создания массива с 5 случайными целыми числами в от [0, 10)

### МАССИВЫ

"""np.random.seed(1)
x1=np.random.randint(10,size=3)
x2=np.random.randint(10,size=(3,2))
x3=np.random.randint(10,size=(3,2,1))
print(x1)
print(x2)
print(x3)

print(x1.ndim,x1.shape,x1.size)
print(x2.ndim,x2.shape,x2.size)
print(x3.ndim,x3.shape,x3.size)"""

#Индексы (с 0)
"""
a=np.array([1,2,3,4,5])
print(a[0])
print(a[-2])
a[1]=20
print(a)"""

"""a=np.array([[1,2],[3,4]])
print(a[0,0],a[-1,-1])
a[1,0]=100
print(a)"""

"""a=np.array([1,2,3,4])
b=np.array([1.0,2,3,4])
a[0]=10
print(a[0])
a[0]=10.123 # приведение к инту! тип данных зафиксирован!
print(a)"""

# Срез [s:f:st] default [0:shape:1]
"""
a=np.array([1,2,3,4,5,6])
print(a[0:3:1])# можно упростить
print(a[:3]) # упростили
print(a[3:]) #индекс больше 2
print(a[1:5])#середина
print(a[1:-1])#середина
print(a[1:6:2])#каждый второй(не с начала), но можно проще
print(a[1::2])

print(a[::-1])# отрицательный шаг - меняем начало и конец местами

# Задача 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

# Срез не копия массива, это скорее его кусочек, ссылка!
b=a[:3]
b[0]=100
print(a)"""
# Задача 8. Продемонстрируйте, как сделать срез-копию
"""
a=np.arange(1,13)
print(a)
print(a.reshape(2,6))
print(a.reshape(3,4)) # нельзя чтобы элементы не смогли распределиться(лишние или недостаток)
"""
#Задача 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

"""x=np.array([1,2,3])
y=np.array([4,5])
z=np.array([6])
print(np.concatenate([x,y,z]))"""
"""
x=np.array([1,2,3])
y=np.array([4,5,6])
r1 = np.vstack([x,y])
print(r1)
print(np.hstack([r1, r1]))
"""
# whiteboard

#Задача 10. Разберитесь, как работает метод dstack
#Задача 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit
#Вычисления с массивами
#Векторизированная операция - операция применяемая независимо к каждому элементу
"""
x=np.arange(10)
print(x)
print(x*2+1)
#универсальные функции
print(np.add(np.multiply(x,2),1))
"""
#- - / // ** %
# Задача 12. Привести пример использования всех универсальных функций, которые я привел

# np.abs sin cos exp log

"""x =np.arange(5)
y=np.empty(5)# подготовка места
print(np.multiply(x,10,out=y))

print(y)

x =np.arange(5)
y=np.empty(10)# подготовка места
print(np.multiply(x,10,out=y[::2]))

print(y)

y=np.zeros(10)# подготовка места
print(np.multiply(x,10,out=y[::2]))

print(y)"""

# Свертки
"""x = np.arange(1,5)
print(x)
print(np.add.reduce(x))
print(np.add.accumulate(x))"""
# Векторные произведения
x =np.arange(1,10)
print(np.add.outer(x,x))
print(np.multiply.outer(x,x))



#
#
