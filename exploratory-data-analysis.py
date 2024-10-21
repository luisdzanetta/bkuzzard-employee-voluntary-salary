# %%
# Import necessary libraries for data manipulation
import pandas as pd

# %%
# Read the CSV file containing Blizzard employee salary data
df_blizzard_salary = pd.read_csv('./data/blizzard_salary.csv')

# %%
# Display the DataFrame to check the contents
df_blizzard_salary

# %%
# Show the first few rows of the DataFrame for a quick overview
df_blizzard_salary.head()

# %%
# Get the shape of the DataFrame (number of rows and columns)
df_blizzard_salary.shape

# %%
# Display memory usage information of the DataFrame
df_blizzard_salary.info(memory_usage='deep')

# %%
# List all column names in the DataFrame
df_blizzard_salary.columns

# %%
# Provide descriptive statistics for the 'current_salary' column
df_blizzard_salary['current_salary'].describe()

# %%
# Identify rows with the maximum and minimum current salary
max_salary = df_blizzard_salary['current_salary'] == df_blizzard_salary['current_salary'].max()
min_salary = df_blizzard_salary['current_salary'] == df_blizzard_salary['current_salary'].min()

# %%
# Create boolean masks for salaries greater than and less than or equal to the average salary
greater_than_avg = df_blizzard_salary['current_salary'] > df_blizzard_salary['current_salary'].mean()
lower_than_avg = df_blizzard_salary['current_salary'] <= df_blizzard_salary['current_salary'].mean()

# %%
# Identify employees with a current salary less than or equal to $1000
lower_than_1k = df_blizzard_salary['current_salary'] <= 1000

# %%
# Create a new DataFrame containing only employees with a salary less than or equal to $1000
lower_than_1k_slice = df_blizzard_salary[lower_than_1k].copy()

# %%
# Display the filtered DataFrame for salaries less than or equal to $1000
lower_than_1k_slice

# %%
# Create a boolean mask for employees whose salary type is 'year'
lower_than_1k_year = lower_than_1k_slice['salary_type'] == 'year'

# %%
# Count occurrences of each salary type among employees earning less than or equal to $1000
lower_than_1k_year.value_counts()

# %%
# Display all employees with a current salary less than or equal to $1000
df_blizzard_salary[lower_than_1k]

# %%
# Count occurrences of each status in the DataFrame
df_blizzard_salary['status'].value_counts()

# %%
# Count occurrences of each job title in the DataFrame
df_blizzard_salary['current_title'].value_counts()

# %%
# Count occurrences of each salary type in the DataFrame
df_blizzard_salary['salary_type'].value_counts()

# %%
# Count occurrences of each location in the DataFrame
df_blizzard_salary['location'].value_counts()

# %%
# Count occurrences of each performance rating in the DataFrame
df_blizzard_salary['performance_rating'].value_counts()