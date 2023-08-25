import pandas as pd
file_path = "C:\\Users\\Administrator\\Downloads\\Employee_list.csv"
df = pd.read_csv(file_path)
print("Column Names:", df.columns)
index_column_name = 'Empid'
df.set_index(index_column_name, inplace=True)
print(df)
filtered_df = df[(df['Age'] >= 29) & (df['Age'] <= 40)]
employee_names = filtered_df['Name']
print("Employee names with age between 29 and 40:")
print(employee_names)
