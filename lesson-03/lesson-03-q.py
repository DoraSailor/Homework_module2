import numpy as np
import pandas as pd
# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари
data=pd.Series([0.25,0.5,0.75,1])
print('list')
print(data)

data=pd.Series(np.array([0.25,0.5,0.75,1]))
print("np.array")
print(data)

data=pd.Series(111)
print("scalar")
print(data)

print('dictionary')
data = pd.Series(
    {
        'city_1': 9991,
        'city_2': 9992,
        'city_3': 9993,
        'city_4': 9994,
        'city_5': 9995,
    })
print(data)

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

print("через объекты Series")
print(pd.DataFrame(data))
print(" списки словарей")
dictionary1={'a':'A','b':'B'}
dictionary2={'a1':'A1','b1':'B1'}
print(pd.DataFrame([dictionary1,dictionary2]))


print("словари объектов Series")
population_dict={
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005,
}
area_dict={
    'city_1': 9991,
    'city_2': 9992,
    'city_3': 9993,
    'city_4': 9994,
    'city_5': 9995,
}
population=pd.Series(population_dict)
area=pd.Series(area_dict)
print(pd.DataFrame({'population1': population,'area1': area}))
print("двумерный массив NumPy")
print(pd.DataFrame(np.array([[1,2],[3,4]])))
print("структурированный массив Numpy")
data = np.array([('Max',27),('Lola',8),('Alexa',18)],dtype={'names':('name','age'),"formats":('U10','i4')})
print(pd.DataFrame(data))
# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
dictionary1={'a':'A','b':'B'}
dictionary2={'a1':'A1','b1':'B1'}
print(pd.DataFrame([dictionary1,dictionary2]).fillna(1))

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng(1)
A=rng.integers(0,10,(3,4))
df =pd.DataFrame(A,columns=['a','b','c','d'])
print(df)
print(df.iloc[:,0])
print((df.T-df.iloc[:,0]).T)
print(df.iloc[::2,0])
print((df.T-df.iloc[::2,0]).T)
# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
print(pd.DataFrame([dictionary1,dictionary2]).ffill(axis=0))
print(pd.DataFrame([dictionary1,dictionary2]).ffill(axis=1))
print(pd.DataFrame([dictionary1,dictionary2]).bfill(axis=0))
print(pd.DataFrame([dictionary1,dictionary2]).bfill(axis=1))

