import pandas as pd
file_path = "C:\\Users\\Administrator\\Downloads\\Employee_list.csv"
df = pd.read_csv(file_path)
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print(df)
