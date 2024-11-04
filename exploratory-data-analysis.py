'''
 what we need to do
 1. drop data where current_salary == 1 AND salary_type == 1
 2. drop data where current_title == NaN
 3. dropd data where current_salary = NaN (df_blizzard_salary.dropna(subset=['status', 'current_salary'], how='any'))
 3. filter only status == full time employee
 4. adjust current_title string, sometimes the level of status is I othertimes is 1
 5. 2 caminhos no salary_type, podemos dropar os que são hora/semana ou calcular um valor aproximado de salário

'''

# %% [markdown]
# # **Blizzard Employee Voluntary Salary Exploratoy Data Analysis**

# %% [markdown]
# ## **Context**

# ------

# Blizzard Entertainment, Inc. is a prominent American video game developer and publisher located in Irvine, California, and operates as a subsidiary of Activision Blizzard. Established in 1991, the company is renowned for its creation of the influential MMORPG World of Warcraft (2004) and successful franchises such as Diablo, StarCraft, and Overwatch. Blizzard also runs Battle.net, an online gaming platform[1].
#
# In 2020, employees at Blizzard have taken steps to address concerns regarding wage disparities by circulating an anonymous spreadsheet detailing salaries and pay increases. This initiative reflects growing discontent within the company, particularly following a 2019 internal survey that revealed significant dissatisfaction with compensation among staff. With many employees feeling undervalued despite the company's financial success, this analysis aims to explore the salary data shared by employees to uncover patterns and insights related to compensation equity across different roles within Blizzard. By examining this data, we hope to shed light on the broader issues of wage disparity and employee satisfaction in the gaming industry[2].
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Blizzard_Entertainment_Logo_2015.svg/1200px-Blizzard_Entertainment_Logo_2015.svg.png" width="300" height="156.25">
#
# %% [markdown]
# ## **Objective**
# ------

# %% [markdown]
# ## **Dictionary**
#
# **Description**
#
# Employee generated anonymous survey of salary information [3, 4, 5].
#
# | column                      |  description                                       | 
# | :-----------------------:   |:-----------------------:                           |
# | timestamp                   |Time data was entered                               |
# | status                      |Specifies employment status                         |
# | current_title               |Current job title                                   |
# | current_salary              |Current salary (in USD)                             |
# | salary_type                 |Frequency with levels year, hour, week              |
# | percent_incr                |Raise given July 2020                               |
# | other_info                  |Other information submitted by employee             |
# | location                    |Current office of employment                        |
# | performance_rating          |Most recent review performance rating               |

# %% [markdown]
# ## **References**
#
# 1. [Wikipedia, 2024](https://en.wikipedia.org/wiki/Blizzard_Entertainment)
# 2. [Time, 2020](https://time.com/5875371/blizzard-wage-disaparities/)
# 3. [Bloomberg, 2020](https://www.bloomberg.com/news/articles/2020-08-03/blizzard-workers-share-salaries-in-revolt-over-wage-disparities)
# 4. [OpenInto, 2020](https://www.openintro.org/data/index.php?data=blizzard_salary)
# 5. [Kaggle, 2024](https://www.kaggle.com/datasets/mexwell/blizzard-employee-voluntary-salary-info)

# %% [markdown]
# ## **Exploratory Data Analysis**

# %% [markdown]
# ### **Understanding Variables**

# %% [markdown]
# #### **Libraries Import**

# %%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# %% [markdown]
# #### **Data Load**

# %%
# Read the CSV file containing Blizzard employee salary data
df_blizzard_salary = pd.read_csv('./data/blizzard_salary.csv')

# %% [markdown]
# #### **Dataframe infos**

# %%
# Display memory usage information of the DataFrame
df_blizzard_salary.info(memory_usage='deep')

# %%
df_blizzard_salary.shape

# %%
# Show the first few rows of the DataFrame for a quick overview
df_blizzard_salary.head()

# %%
df_blizzard_salary.columns

# %%
# Show the first few rows of the DataFrame for a quick overview
df_blizzard_salary.info()

# %%
df_blizzard_salary.dtypes

# %%
# Provide descriptive statistics
df_blizzard_salary.describe()


# %% [markdown]
# #### Categorical Variables

# %%
#
print(df_blizzard_salary['status'].unique())
print('')
print(df_blizzard_salary['current_title'].unique())
print('')
print(df_blizzard_salary['salary_type'].unique())
print('')
print(df_blizzard_salary['location'].unique())
print('')
print(df_blizzard_salary['performance_rating'].unique())


# %%
print(df_blizzard_salary['status'].value_counts())
print('')
print(df_blizzard_salary['current_title'].value_counts())
print('')
print(df_blizzard_salary['salary_type'].value_counts())
print('')
print(df_blizzard_salary['location'].value_counts())
print('')
print(df_blizzard_salary['performance_rating'].value_counts())

# %%
# Status & Salary Type
fig, axs = plt.subplots(1, 2, figsize = (10, 5))

sns.histplot(df_blizzard_salary['status'], ax=axs[0])
axs[0].set_title('Employment Status')

sns.histplot(df_blizzard_salary['salary_type'], ax=axs[1])
axs[1].set_title('Payment Frequency')

plt.show()

# %%
# Location x salary
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, y=df_blizzard_salary['location'])
plt.title('Employment Office Location')

plt.show()

# %%
# Interessante, não tem pessoa com as faixas mais altas de salário fora de irvine
# Location x salary
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['current_salary'], 
             y=df_blizzard_salary['location'],
             hue=df_blizzard_salary['location'],
             legend=False)
plt.title('Current Salary by Employement Office Location')

plt.show()

# %%
# Performance
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['performance_rating'])
plt.title('Performance Rating Review')

plt.show()

# %%
# Interessante, não tem pessoa com top e developing nas faixas mais altas de salário
# Performance x salary
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['current_salary'], 
             y=df_blizzard_salary['performance_rating'],
             hue=df_blizzard_salary['performance_rating'],
             legend=False)
plt.title('Current Salary by Performance Rating')

plt.show()

# %% [markdown]
# #### Numerical Variables


# %%
fig, axs = plt.subplots(1, 2, figsize = (10, 5))

sns.histplot(df_blizzard_salary['current_salary'], kde = True, ax=axs[0])
axs[0].set_title('Current Salary Histogram')

sns.histplot(df_blizzard_salary['percent_incr'], kde = True, ax=axs[1])
axs[1].set_title('Raise given (%) Histogram')

plt.show()


# %%
df_blizzard_salary['current_salary'].hist(bins=50)

# %%
df_blizzard_salary['percent_incr'].hist(bins=50)














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
df_blizzard_salary[['performance_rating']].value_counts()

# %%
# Count occurrences of each performance rating in the DataFrame
df_blizzard_salary[['other_info']].value_counts()

# %%
df_blizzard_salary.sort_values(by='current_salary', ascending=False)


# %%
df_blizzard_salary[['current_title']] == 'Game Master'

# %%
df_blizzard_salary['current_title'].nunique()

# %%
df_blizzard_salary.describe()

# %%
df_blizzard_salary['percent_incr'].max()

# %%
df_blizzard_salary['other_info'][df_blizzard_salary['timestamp'] == '7/31/20 18:07']

# %%
df_blizzard_salary['other_info'].iloc[450]

# %%
df_blizzard_salary['current_title_0'] = df_blizzard_salary['current_title'].str.split(' ').str[0]
df_blizzard_salary['current_title_1'] = df_blizzard_salary['current_title'].str.split(' ').str[1]
df_blizzard_salary['current_title_2'] = df_blizzard_salary['current_title'].str.split(' ').str[2]
df_blizzard_salary['current_title_3'] = df_blizzard_salary['current_title'].str.split(' ').str[3]


# %%
df_blizzard_salary
# %%
df_blizzard_salary['current_title_3'].value_counts()

# %%
df_blizzard_salary.isna().sum()

# %%
df_blizzard_salary.dropna(subset=['status', 'current_salary'])

# %%
df_blizzard_salary['current_title'].unique()
# %%

df_blizzard_salary.groupby(['current_title'])['current_salary'].mean().sort_values(ascending=False)

# %%
(df_blizzard_salary.groupby(['current_title'])
    .agg({
        'current_salary':'mean',
        'current_title':'count'})
    .sort_values(by='current_salary', ascending=False)
    .rename(columns={
        'current_salary':'salary_mean',
        'current_title':'title_count'})
    .reset_index())

# %%
df_blizzard_salary



# %% [markdown]
# ### **Data Cleaning and Curation**

# %% [markdowm]
# ### **Exploring Relationships Between Variables**
