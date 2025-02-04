import numpy as np

import pandas as pd
# # 1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
index=pd.MultiIndex.from_tuples(index)
pop = pd.Series(population, index = index)

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)
print(pop_df)
pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_1)
# в примере изначально всё было правильно во взятии среза,
# просто при инициизации DataFrame индекс был взят не как мульти индекс а как список кортежей
# поэтому и не работал примернана на занятии, здесь же все приведено для мультииндекса и работает как надо


print(2)
# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 
index=pd.MultiIndex.from_product(
    [['city_1','city_2'],
    [2010,2020]],
    names=['city','year'])
columns=pd.MultiIndex.from_product(
    [['person_1','person_2','person_3'],
     ['job_1','job_2']],
    names=['worker','job']
)
rng=np.random.default_rng(1)
data=rng.random((4,6))
data_df=pd.DataFrame(data,index=index,columns=columns)
print(data_df)
print(data_df.loc[::2])
print(data_df.loc[:,::2])
print(data_df.loc["city_1",("person_1","job_2")::2])
print("так же можно использовать:")
print(data_df.loc[(slice(None),2020),(slice(None),slice(None))])
print(data_df.loc[(slice(None),slice(None)),(slice(None),"job_1")])
print(data_df.loc[("city_1",slice(None)),(slice(None),"job_2")])
print(3)
# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng=np.random.default_rng(1)
data=rng.random((4,6))
data_df=pd.DataFrame(data,index=index,columns=columns)
print(data_df)
# 
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice
print(data_df.loc[:,['person_1','person_3']])
print(data_df.loc['city_1','person_1':'person_2'])

idx = pd.IndexSlice
print(data_df.loc[idx[:,2020],idx[:,"job_2"]])

print(4)
#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])
#
# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))

# Документация сказала что он применим лишь для DataFrames поэтому вот пример для них:
ser1 = pd.DataFrame(np.array([['a', 'b', 'c'],[11,22,33],[1.11,2.22,3.33]]).T, index=[1,2,3],columns=["char",'int','float'])
ser2 = pd.DataFrame(np.array([['d', 'e', 'f'],[44,55,66],[4.44,5.55,6.66]]).T, index=[4,5,6],columns=["char",'int','double'])

print (pd.concat([ser1, ser2], join='outer'))
print (pd.concat([ser1, ser2], join='inner'))
