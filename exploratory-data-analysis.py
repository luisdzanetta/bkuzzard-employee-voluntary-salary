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
max_salary = df_blizzard_salary['current_salary'] == df_blizzard_salary['current_salary'].max()
min_salary = df_blizzard_salary['current_salary'] == df_blizzard_salary['current_salary'].min()

greater_than_avg = df_blizzard_salary['current_salary'] > df_blizzard_salary['current_salary'].mean()
lower_than_avg = df_blizzard_salary['current_salary'] <= df_blizzard_salary['current_salary'].mean()

# %%
df_blizzard_salary[min_salary]

# %%
df_blizzard_salary['status'].value_counts()

# %%
df_blizzard_salary['current_title'].value_counts()

# %%
df_blizzard_salary['salary_type'].value_counts()

# %%
df_blizzard_salary['location'].value_counts()

# %%
df_blizzard_salary['performance_rating'].value_counts()

# %%
