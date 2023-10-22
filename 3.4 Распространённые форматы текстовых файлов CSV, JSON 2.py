'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными: Crimes.csv
'''
import csv
import pandas as pd

df = pd.read_csv('Crimes.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Date'].dt.year == 2015]
columns_to_keep = ['Date', 'Primary Type']
df = df[columns_to_keep]
unique_values = df['Primary Type'].value_counts()
print(unique_values)
