import pandas as pd
from data import data

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)


print('ЗАДАЧА 1')

# 1.1
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print('\n1.1 Series:')
print(s)

# 1.2
df = pd.DataFrame(data)
print('\n1.2 DataFrame:')
print(df)

# 1.3
print('\n1.3 Первые строки:')
print(df.head())
print('\nПоследние строки:')
print(df.tail())
print('\nИнформация о типах данных:')
df.info()
print('\nСтатистика:')
print(df.describe())


print('\n\nЗАДАЧА 2')

# 2.1
print('\n2.1 name и salary сотрудников из IT:')
print(df[df['department'] == 'IT'][['name', 'salary']])

# 2.2
print('\n2.2 Первые 3 строки и 2 столбца (iloc):')
print(df.iloc[:3, :2])

# 2.3
print('\n2.3 Зарплата выше 70000:')
print(df[df['salary'] > 70000])

# 2.4
df['total_comp'] = df['salary'] + df['bonus'].fillna(0)
print('\n2.4 Новый столбец total_comp:')
print(df)

# 2.5
df = df.drop(columns='hire_date')
print('\n2.5 После удаления hire_date:')
print(df)


print('\n\nЗАДАЧА 3')

# 3.1
print('\n3.1 Количество пропусков в столбцах:')
print(df.isnull().sum())

# 3.2
df['salary'] = df['salary'].fillna(df.groupby('department')['salary'].transform('mean'))
print('\n3.2 salary после заполнения средним по отделу:')
print(df[['name', 'department', 'salary']])

# 3.3
df['bonus'] = df['bonus'].fillna(0)
print('\n3.3 bonus после заполнения нулём:')
print(df[['name', 'bonus']])

# 3.4
df['total_comp'] = df['salary'] + df['bonus']
df = df.dropna(subset=['salary'])
print('\n3.4 После удаления строк с пропуском в salary:')
print(df)
print('Размер таблицы:', df.shape)
print('Пропусков осталось:')
print(df.isnull().sum())


print('\n\nЗАДАЧА 4')

# 4.1
print('\n4.1 Средняя зарплата по отделам:')
print(df.groupby('department')['salary'].mean())

# 4.2
result = df.groupby('department').agg({'salary': 'mean', 'bonus': 'max', 'name': 'count'})
result = result.rename(columns={'salary': 'avg_salary', 'bonus': 'max_bonus', 'name': 'employees'})
print('\n4.2 Средняя зарплата, максимальный бонус и число сотрудников:')
print(result)

# 4.3
pivot = df.pivot_table(index='department', values='salary', aggfunc='mean')
print('\n4.3 Сводная таблица:')
print(pivot)

# 4.4
pivot = pivot.sort_values('salary', ascending=False)
print('\n4.4 Отделы по средней зарплате (по убыванию):')
print(pivot)


print('\n\nЗАДАЧА 5')

# 5.1
managers = pd.DataFrame({
    'department': ['IT', 'HR', 'Finance'],
    'manager': ['Oliver', 'Paula', 'Victor']
})
print('\n5.1 managers:')
print(managers)

# 5.2
df_merged = df.merge(managers, on='department', how='left')
print('\n5.2 После left join:')
print(df_merged)

# 5.3
new_row = pd.DataFrame({
    'name': ['Ian'],
    'department': ['IT'],
    'salary': [95000],
    'bonus': [7000],
    'total_comp': [102000],
    'manager': ['Oliver']
})
df_new = pd.concat([df_merged, new_row])
print('\n5.3 После concat (индекс пока не сброшен):')
print(df_new)

# 5.4
df_new = df_new.reset_index(drop=True)
print('\n5.4 После сброса индекса:')
print(df_new)


print('\n\nЗАДАЧА 6')

# 6.1
print('\n6.1 Топ-3 по total_comp:')
print(df.sort_values('total_comp', ascending=False).head(3)[['name', 'department', 'total_comp']])

# 6.2
print('\n6.2 Средняя зарплата и средний бонус по отделам:')
print(df.groupby('department')[['salary', 'bonus']].mean())

# 6.3
high_salary = df['salary'] > 75000
print('\n6.3 Доля сотрудников с зарплатой выше 75000 по отделам:')
print(high_salary.groupby(df['department']).mean())
