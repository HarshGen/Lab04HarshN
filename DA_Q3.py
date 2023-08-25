import pandas as pd
file_path = "C:\\Users\\Administrator\\Downloads\\Employee_list.csv"
df = pd.read_csv(file_path)
sorted_df = df.sort_values(by='Age', ascending=True)
first_5_younger = sorted_df.head(5)
output_path = "C:\\Users\\Administrator\\Downloads\\New_Data.csv"
first_5_younger.to_csv(output_path, index_label='Employee ID')
print(first_5_younger)
