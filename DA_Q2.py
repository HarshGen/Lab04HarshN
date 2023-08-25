import pandas as pd

def compare_profession(dataframe):
    profession_salary_sum = dataframe.groupby('Profession')['Salary'].sum()
    engineer_salary = profession_salary_sum.get('Engineer', 0)
    doctor_salary = profession_salary_sum.get('Doctor', 0)
    total_salary = engineer_salary + doctor_salary
    engineer_percentage = (engineer_salary / total_salary) * 100
    doctor_percentage = (doctor_salary / total_salary) * 100
    result_df = pd.DataFrame({
        'Profession': ['Engineer', 'Doctor'],
        '% of total Salary': [engineer_percentage, doctor_percentage]
    })

    return result_df
file_path = "C:\\Users\\Administrator\\Downloads\\Employee_list.csv"
df = pd.read_csv(file_path)
result = compare_profession(df)
print(result)
