import pandas as pd
import numpy as np

# Carrega os dados
data = pd.read_csv('voltage_log.csv')

# Calcula a média sem os outliers (baseado em 3 desvios padrão)
Q1 = data['voltage (°C)'].quantile(0.25)
Q3 = data['voltage (°C)'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
print(Q1)
print(Q3)
print(IQR)
data_filtered = data[(data['voltage (°C)'] >= lower_bound) & (data['voltage (°C)'] <= upper_bound)]
media_sem_outliers = data_filtered['voltage (°C)'].mean()
print(data_filtered)
print(media_sem_outliers)