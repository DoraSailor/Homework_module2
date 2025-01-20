import numpy as np
## 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок (транслирование)?
print("1)")
# метод 1
a=np.ones((3,2))
b=np.arange(3)
print(a+b.reshape((3,1)))
# метод 2
a=np.ones((3,2))
b=np.arange(2)
print(a+b)
# метод 3
a=np.ones((3,3))
b=np.arange(3)
print(a+b)

## 2. Пример для y. Вычислить количество элементов (по обеим размерностям), значения которых больше 3 и меньше 9
print("2)")
y=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum((3<y)*(y<9)))
print(np.sum((3<y)*(y<9),axis=0))
print(np.sum((3<y)*(y<9),axis=1))