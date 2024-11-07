# %% [markdown]
# # **Blizzard Employee Voluntary Salary Exploratoy Data Analysis**
#
# ---

# %% [markdown]
# ## **Context**
# Blizzard Entertainment, Inc. is a prominent American video game developer and publisher located in Irvine, California, and operates as a subsidiary of Activision Blizzard. Established in 1991, the company is renowned for its creation of the influential MMORPG World of Warcraft (2004) and successful franchises such as Diablo, StarCraft, and Overwatch.
# Blizzard also runs Battle.net, an online gaming platform [1].
#
# In 2020, employees at Blizzard have taken steps to address concerns regarding wage disparities by circulating an anonymous spreadsheet detailing salaries and pay increases. This initiative reflects growing discontent within the company, particularly following a 2019 internal survey that revealed significant dissatisfaction with compensation among staff. With many employees feeling undervalued despite the company's financial success,
# this analysis aims to explore the salary data shared by employees to uncover patterns and insights related to compensation equity across different roles within Blizzard.
# By examining this data, we hope to shed light on the broader issues of wage disparity and employee satisfaction in the gaming industry [2].
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Blizzard_Entertainment_Logo_2015.svg/1200px-Blizzard_Entertainment_Logo_2015.svg.png" width="300" height="156.25">
#

# %% [markdown]
# ## **Objective**
# 

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
# 6. [Ellow, 2024](https://ellow.io/contract-work-vs-full-time-employment/)

# %% [markdown]
# ## **Exploratory Data Analysis**

# %% [markdown]
# #### **Libraries Import**

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fuzzywuzzy import process

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
# Check the dimensions of the DataFrame
df_blizzard_salary.shape

# %%
# Show the first few rows for a quick overview
df_blizzard_salary.head()

# %%
# List all column names
df_blizzard_salary.columns

# %%
# Show detailed information including non-null counts and data types
df_blizzard_salary.info()

# %%
# Display data types of each column
df_blizzard_salary.dtypes

# %%
# Provide descriptive statistics for numerical columns
df_blizzard_salary.describe()

# %% [markdown]
# ### **Understanding Variables**

# %% [markdown]
# #### **Categorical Variables**

# %%[markdown]
# **Status**
#
# The 'status' column has two contract options: Full Time Employee and Contractor
# Full Time Employee refers to conventional employment (similar to CLT in Brazil), while Contractor resembles freelance work. [6]

# %%
# This displays unique employment statuses
print(df_blizzard_salary['status'].unique())

# %%
# Visualization of employment status distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['status'])
plt.title('Employment Status (Contract Type)')

plt.show()

# %%[markdown]
# **Current Title**
#
# The Current Title column represents employee job titles with 202 unique values.
# Notable inconsistencies include:
# 1. Lack of standardization in job levels (e.g., I vs. 1).
# 2. Inconsistencies in seniority descriptors (e.g., Sr. vs. Senior).
# 3. Non-standardized job titles (e.g., 'Customer Support Specialist Game Master' vs 'Game Master').
# 4. Incomplete entries (e.g., 'Senior 1', 'X', or 'Can't say').

# %%
# This counts occurrences of each job title
print(df_blizzard_salary['current_title'].value_counts())

# %%
# Get the top 20 most common job titles
top_titles = df_blizzard_salary['current_title'].value_counts().nlargest(20)

# %%
# Sort the DataFrame by current title
df_blizzard_salary_sorted = df_blizzard_salary.sort_values(by='current_title')

print(df_blizzard_salary_sorted['current_title'].unique())

# %%
# Visualization of job title distribution using a bar plot
fig, axs = plt.subplots(1, 1, figsize = (8, 10))

sns.barplot(x=top_titles.values, y=top_titles.index, errorbar=None)
axs.bar_label(axs.containers[0], fontsize=10)
plt.title('Employment Title')

plt.show()

# %%[markdown]
# **Salary Type**
#
# In Salary Type, there are three methods for calculating salary: annually, weekly, and hourly.
# Different calculation methods impact the values in 'current_salary', necessitating standardization.

# %%
# This counts occurrences of each salary type
print(df_blizzard_salary['salary_type'].value_counts())

# %%
# Visualization of salary type distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['salary_type'])
plt.title('Salary Type')

plt.show()

# %%[markdown]
# **Location**
#
# In Location, employees recorded their base allocations with some inconsistencies:
# - Variations in city names (e.g., 'Los Angeles Center Studios' vs 'Los Angeles').
# - Case sensitivity issues (e.g., 'Versailles' vs 'versailles').

# %%
# This counts occurrences of each location entry
print(df_blizzard_salary['location'].value_counts())

# %%
# Visualization of location distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, y=df_blizzard_salary['location'])
plt.title('Employment Office Location')

plt.show()

# %%[markdown]
# **Performance Rating**
#
# In **Performance Rating**, we have the classification of the last performance evaluation of employees, considering (from worst to best performance):
# 1. 'developing'
# 2. 'successful'
# 3. 'high'
# 4. 'top'

# %%
# This counts occurrences of each performance rating entry
print(df_blizzard_salary['performance_rating'].value_counts())

# %%
# Visualization of performance ratings distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary, x=df_blizzard_salary['performance_rating'])
plt.title('Performance Rating Review')

plt.show()

# %% [markdown]
# #### **Numerical Variables**

# %%[markdown]
# **Current Salary**
#
# In this variable, we have the amounts declared by employees in USD. 
# As noted in the Salary Type variable, the declared amount can be annual, weekly, or hourly. 
# The histogram shows a large number of values close to zero, which does not make much sense when considering annual salaries. 
# Therefore, it will be necessary to standardize the salaries of these employees to a common basis for meaningful comparison.

# %%
# Visualization of current salary distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (10, 5))

sns.histplot(df_blizzard_salary['current_salary'], kde = True)
plt.title('Current Salary Histogram')

plt.show()

# %%
# Create a new DataFrame containing only employees whose salary type is annual
df_current_salary_year = df_blizzard_salary[df_blizzard_salary['salary_type'] == 'year'].copy()

# %%
# Visualization of current salary distribution for annual salaries using a histogram
fig, axs = plt.subplots(1, 1, figsize = (10, 5))

sns.histplot(df_current_salary_year['current_salary'], kde = True)
plt.title('Current Salary Histogram')

plt.show()

# %%
# Display the smallest current salaries
smallest_salaries = df_blizzard_salary['current_salary'].nsmallest(20)
smallest_salaries_year = df_current_salary_year['current_salary'].nsmallest(20)

print(smallest_salaries)
print(smallest_salaries_year)

# %%
# Sort and display current titles with their salary type and current salary
print(df_blizzard_salary[['current_title', 'salary_type', 'current_salary']].sort_values)
print(df_current_salary_year[['current_title', 'salary_type', 'current_salary']].sort_values)

# %%
# Visualization of current salary distributions using violin plots
fig, axs = plt.subplots(1, 2, figsize = (20, 5))

sns.violinplot(x=df_blizzard_salary['current_salary'], ax=axs[0])
axs[0].set_title('Current Salary')

sns.violinplot(x=df_current_salary_year['current_salary'], ax=axs[1])
axs[1].set_title('Current Salary (Filtered by Year)')

plt.show()

# %%[markdown]
# **Current Salary**
#
# In this variable, we have the percentage increase that employees received in 2020.

# %%
# Display the normalized value counts of percentage increases
df_blizzard_salary['percent_incr'].value_counts(normalize=True)*100

# %%
# Provide descriptive statistics for the percentage increase
df_blizzard_salary['percent_incr'].describe()

# %%
# Visualization of salary raise distribution using a histogram
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.histplot(data=df_blizzard_salary['percent_incr'])
plt.title('Salary Raise (%)')

plt.show()

# %% [markdown]
# ### **Data Cleaning and Curation**
# ##### tratamento do current_title

# %%
# act = adjusted current title
# Create a copy of the original DataFrame for adjustments
df_blizzard_salary_act = df_blizzard_salary.copy()

# Drop rows where 'current_salary' is NaN
df_blizzard_salary_act = df_blizzard_salary_act.dropna(subset=['current_salary'])

# Drop rows where 'current_title' is NaN
df_blizzard_salary_act = df_blizzard_salary_act.dropna(subset=['current_title'])

# Create a new column 'adjusted_title' with lowercase titles
df_blizzard_salary_act['adjusted_title'] = df_blizzard_salary_act['current_title'].str.lower()

# Reorder columns in the DataFrame
colunas = ['timestamp', 'status', 'current_title', 'adjusted_title', 'current_salary', 'salary_type',
       'percent_incr', 'other_info', 'location', 'performance_rating']

df_blizzard_salary_act = df_blizzard_salary_act.reindex(colunas, axis=1)


# %%
# Function to Replace Terms Using Regex
def replace_terms(DataFrame, columns, replacements):
    for col in columns:
        for oldvalue, newvalue in replacements.items():
            DataFrame[col] = DataFrame[col].str.replace(oldvalue, newvalue, regex=True)

# Substitution Dictionary
replacements = {
    # Drop Incomplete entries
    r'\bx\b': '',
    r'\bposition in ii tier\b': '',
    r".*can't say \(loss of anonimity\).*": '',
    r'\bchoose not to disclose\b': '',
    r'\bsenior i\b': '',

    # Inconsistencies in seniority descriptors
    r'\bsr\.': 'senior',
    r'\bsenor': 'senior',

    # Lack of standardization in job levels
    r'\b1': 'i',
    r'\b2': 'ii',

    # Non-standardized job titles
    r'.*senior software egr i\.\-.*': 'senior software engineer i',
    r'.*associate pm \(my range is on the same scale as pm, but not my actual title\)*': 'associate pm',
    r'.*principle*': 'principal',
    r'.*3d artist\(character\)*': '3d artist (character artist)',
    r'.*ui \/ux designer*': 'ui/ux designer',
    r'.*associate software development engineer in test*': 'associate software developer engineer in test',
    r'.*qa*': 'qa analyst',
}

# Applying Replacements
replace_terms(df_blizzard_salary_act, ['adjusted_title'], replacements)

# %%
# Check specific adjusted titles
df_blizzard_salary_act[df_blizzard_salary_act['adjusted_title'].str.contains(r".*qa.*", na=False)]['adjusted_title']





















# %%

def replace_terms(DataFrame, columns, replacements):
    for col in columns:
        for oldvalue, newvalue in replacements.items():
            DataFrame[col] = DataFrame[col].str.replace(oldvalue, newvalue, regex=True)


# %%
replacements = {
    r'\bx\b': '',
    r'\bposition in II tier\b': '',
    r"\bcan't say \(loss of anonimity\)\b": '',
    r'\bchoose not to disclose\b': '',
    r'\bsr\.\b': 'senior',
    r'\bsenor\.\b': 'senior',
    r'senior software egr 1\.\-\.': 'senior software engineer',
    r'\b1\b': 'i',
    r'\b2\b': 'ii',
    r'\b3\b': 'iii'
}

# %%
# Aplicar todas as substituições de uma vez
df_blizzard_salary_current_status_adjusted = replace_terms(df_blizzard_salary_current_status_adjusted, ['current_title'], replacements)

# %%
print(df_blizzard_salary_current_status_adjusted)



# %%
print(df_blizzard_salary_current_status_adjusted['current_title'].unique())
# print(df_blizzard_salary['current_title'].value_counts())

# %%
print(df_blizzard_salary.isnull().sum())
print(df_blizzard_salary_current_status_adjusted.isnull().sum())









# %%
# Status & Salary Type
df_blizzard_salary.groupby(['salary_type'])['current_salary'].mean().sort_values(ascending=False)


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

'''
Aqui talvez seja legal adicionar a ordem de grandeza. Entendi que é (do menor para o maior):
- developing
- successful
- high
- top
'''

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




'''
Para estimar quanto ganha por ano esses colaboradores que recebem por semana/hora

Média por semana = 1625*52(weeks by year) = 84,500.00
Média por hora = 30.29 * 2,080(hours by year) = 63,0003.20

'''



'''
 what we need to do
 1. drop data where current_salary == 1 AND salary_type == 1
 2. drop data where current_title == NaN
 3. dropd data where current_salary = NaN (df_blizzard_salary.dropna(subset=['status', 'current_salary'], how='any'))
 3. filter only status == full time employee
 4. adjust current_title string, sometimes the level of status is I othertimes is 1
 5. 2 caminhos no salary_type, podemos dropar os que são hora/semana ou calcular um valor aproximado de salário

'''






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





# %% [markdowm]
# ### **Exploring Relationships Between Variables**
