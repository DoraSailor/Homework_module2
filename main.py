import numpy as np
import pandas as pd

# Pandas - расширение Numpy (структурированные массивы) Строки и Столбцы индексируются метками,
# а не только числовыми значениями

# Series, DataFrame, Index

#Series

#data=pd.Series([0.25,0.5,0.75,1])
#print(data)
#print(type(data))
#
#print(data.values)
#print(type(data.values))
#
#
#print(data.index)
#print(type(data.index))

#data=pd.Series([0.25,0.5,0.75,1],index=['a','b','c','d'])
#
#print(data)
#print(data['a'])
#print(data['b':'d'])
#print(type(data.index))

#data=pd.Series([0.25,0.5,0.75,1],index=[1,10,7,'d'])
#print(data)
#print(data[1])

#print(data[10:'d'])

# population_dict={
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }
# population=pd.Series(population_dict)
# print(population)
# print(population['city_4'])
# print(population['city_4':'city_5'])

# Для создания SERIES МОЖНО ИСПОЛЬЗОВАТЬ
#Списки питона и массивы нампи
#скалярные значения
#Словари
# 1 привести различные сспособы задания объектов Series

# DataFrame - двумерный массив с явно определенными индексами. Последовательность "согласованных" объектов Series
# population_dict={
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }
# area_dict={
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# population=pd.Series(population_dict)
# area=pd.Series(area_dict)
#
#
# print(population)
# print(area)
#
# states=pd.DataFrame({
#     'population1': population,
#     'area1': area
# })
# print(states)
# print (states.values)
# print (states.index)
# print (states.columns)
#
# print (type(states.values))
# print (type(states.index))
# print (type(states.columns))
#
# print (states['area1'])

# DataFrame. Способы создания
# Через объекты Series;
# Списки словарей;
# Словари объектов Series;
# Двумерный массив NumPy;
# Структурированный массив NumPy.
# 2. Привести различные способы создания объектов типа DataFrame

# Index -способ организации ссылки на данные объектов Series и DataFrame. Index -неизменяем и упорядочен, является мультимножеством (могут быть повторяющиеся значения)

# ind = pd.Index([2,3,5,7,11])
# print (ind[1])
# print (ind[::2])
#
# # ind[1] = 5 # Не изменится И выдаст ошибку
#
# # Index следует соглашениям объекта set (Python)
# indA = pd.Index([1,2,3,4,5])
# indB = pd.Index([2,3,4,5,6])
# print(indA.intersection(indB)) # Пересечение массивов

# Выборка данных из Serias
# как словарь
# data=pd.Series([0.25,0.5,0.75,1],index=['a','b','c','d'])
# print('a' in data)
# print('z' in data)
#
# print(data.keys())
#
# print(list(data.items()))
#
# data['a']=100
# data['z']=1000
# print(data)

# # как одномерный массив
# data=pd.Series([0.25,0.5,0.75,1],index=['a','b','c','d'])
# print(data['a':'c'])
# print(data[0:2])
# print(data[(data>0.5)&(data<1)])
# print(data[['a','d']])
#
# data=pd.Series([0.25,0.5,0.75,1],index=[1,3,10,15])
#
# print(data[1])
# print(data.loc[1])
# print(data.iloc[1])

# Выборка данных из DataFrame
# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }
# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# pop = pd.Series(
#     {
#         'city_1': 1001,
#         'city_2': 1002,
#         'city_3': 1003,
#         'city_4': 1004,
#         'city_5': 1005,
#     })
# area = pd.Series(
#     {
#         'city_1': 9991,
#         'city_2': 9992,
#         'city_3': 9993,
#         'city_4': 9994,
#         'city_5': 9995,
#     })

# data=pd.DataFrame({'area1':area,'pop1':pop})
# print (data)
# print (data['area1'])
# print (data.area1)
#
# print (data.pop1 is data['pop1'])
# print (data.pop is data['pop1'])


# data['new']=data['area']
# data['new']=data['area']/data['pop1]
#print(data)


#Двумерный NumPy-массив

# data= pd.DataFrame({'area1':area,"pop1":pop})
#
# print(data)
# print(data.values)
# print(data.T)
# print(data['area1'])
# print(data.values[0:3])

# Атрибуты индексаторы
# print(data)
# print(data.iloc[:3,1:2])
# print(data.loc[:'city_4', 'pop1':"pop"])
# print(data.loc[data['pop']>1002, ['area1','pop']])

# data.iloc[0,2]=99999

# print(data)

# rng=np.random.default_rng()
# s=pd.Series(rng[1,2,10])
#
# print(s)
# print(np.exp(s))
#
# pop = pd.Series(
#     {
#         'city_1': 1001,
#         'city_2': 1002,
#         'city_3': 1003,
#         'city_41': 1004,
#         'city_51': 1005,
#     })
# area = pd.Series(
#     {
#         'city_1': 9991,
#         'city_2': 9992,
#         'city_3': 9993,
#         'city_42': 9994,
#         'city_52': 9995,
#     })
# data=pd.DataFrame({'area1':area,'pop1':pop})
# print(data)

#Nan - Not a Number

## 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы
## вместо NaN было установлено значение 1.


# dfA = pd.DataFrame(rng.integers(0,10,(2,2)),columns=['a','b'])
# dfB = pd.DataFrame(rng.integers(0,10,(3,3)),columns=['a','b','c'])
#
# print(dfA)
# print(dfB)
#
# print(dfA+dfB)


# rng = np.random.default_rng(1)
# #
# A=rng.integers(0,10,(3,4))
# # print(A)
# # print(A[0])
# # print(A-A[0])
# #
# df =pd.DataFrame(A,columns=['a','b','c','d'])
# print(df)
# print(df.iloc[0])
# print(df-df.iloc[0])
# print(df.iloc[0,::2])
# print(df-df.iloc[0,::2])

# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам, а по столбцам



# Отсутствующие значения, NA - значения: NaN, null, -9999999

# pandas. Два способа хранения отсутствующих значений
# индикаторы Nan, None
# null

# None - объект (накладные расходы). Не работает с сумированием, минимумам и др. агрегирующими операторами.

# val1 =np.array([1,2,3])
# print(val1.sum())
#
# # val1 =np.array([1,None,2,3]) # не работает
# print(val1.sum())
#
# val1 =np.array([1,np.nan,2,3])
# print(val1)
# print(val1.sum())
# print(np.sum(val1))
# print(np.nansum(val1))

# x=pd.Series(range(10),dtype=int)
# print(x)
# x[0] = None
# x[1] = np.nan
# print (x)
#
# x1=pd.Series(['a','b','c'])
# print(x1)
# x1[0]=None
# x1[1]=np.nan
# print(x1)
#
# x2=pd.Series([1,2,3,np.nan,None, pd.NA])
# print(x2)

# x3=pd.Series([1,2,3,np.nan,None, pd.NA],dtype='Int32')
# print(x3)
#
# print(x3.isnull())
# print(x3[x3.isnull()])
# print(x3[x3.notnull()])
#
# print(x3.dropna())
#
df =pd.DataFrame([
    [1,2,3,np.nan,None,pd.NA],
    [1,2,3,None,5,6],
    [1,np.nan,3,None,np.nan,6]
])
print(df)
# print(df.dropna())
# print('dddddd')
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))

# how
# all -все NA
# any - хотя бы одно NA
# thresh = x остается если присутствует минимум х непустых
print (df.dropna(axis = 1, how = 'all'))
print (df.dropna(axis = 1, how = 'any'))
print (df.dropna(axis = 1, thresh = 2))
## 5. На примере объектов DataFrame продемонстрировать использование методов ffill() и bfill()






