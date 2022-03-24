# This script reads 'Finances - Expense Tracking.csv' and plots total amount spent per category in a pie chart.
import pandas as pd
import matplotlib.pyplot as plt

# Reads csv file
csv_path = "Finances - Expense Tracking.csv"
finances_df = pd.read_csv(csv_path)

# Removes leading spaces from all columns
finances_df.columns = finances_df.columns.str.strip()

for col in finances_df.columns:
    finances_df[col] = finances_df[col].str.lstrip('$ ')
    finances_df[col] = finances_df[col].str.replace(',', '')

expenses_df = finances_df.iloc[:, 3:14]

for col in expenses_df.columns:
    expenses_df[col] = pd.to_numeric(expenses_df[col])

total_column = expenses_df.sum(axis=1)
finances_df['Total'] = total_column

total_value = finances_df['Total'].sum(axis=0)

finances_df['%'] = (total_column/total_value) * 100

finances_category = finances_df.groupby('Category').sum()
finances_category = finances_category.sort_values('Total')

labels = finances_category.index
# print(labels)

plt.pie(finances_category['%'], labels=labels, autopct='%1.1f%%')
plt.show()
