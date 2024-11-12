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
from matplotlib.ticker import FuncFormatter

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

sns.histplot(data=df_blizzard_salary,
             x=df_blizzard_salary['status'],
             hue=df_blizzard_salary['status'],
             palette='viridis')

plt.title('Employment Status (Contract Type)')
plt.xlabel('Employment Status')

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

sns.barplot(x=top_titles.values,
            y=top_titles.index,
            hue=top_titles.index,
            palette='viridis',
            errorbar=None)

axs.bar_label(axs.containers[0], fontsize=10)

plt.title('Employment Title')
plt.xlabel('Count') 

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

sns.histplot(data=df_blizzard_salary,
             x=df_blizzard_salary['salary_type'],
             hue=df_blizzard_salary['salary_type'],
             palette='viridis')

plt.title('Salary Type')
plt.xlabel('Salary Type')

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

sns.histplot(data=df_blizzard_salary,
             y=df_blizzard_salary['location'],
             hue=df_blizzard_salary['location'],
             palette='viridis',
             legend=False)

plt.title('Employment Office Location')
plt.xlabel('Location')

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

sns.histplot(data=df_blizzard_salary,
             x=df_blizzard_salary['performance_rating'],
             hue=df_blizzard_salary['performance_rating'],
             palette='viridis',
             legend=False)

plt.title('Performance Rating Review')
plt.xlabel('Performance Rating')

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

sns.histplot(df_blizzard_salary['current_salary'],
             kde = True)

axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Current Salary Histogram')
plt.xlabel('Current Salary (USD)')

plt.show()

# %%
# Create a new DataFrame containing only employees whose salary type is annual
df_current_salary_year = df_blizzard_salary[df_blizzard_salary['salary_type'] == 'year'].copy()

# %%
# Visualization of current salary distribution for annual salaries using a histogram
fig, axs = plt.subplots(1, 1, figsize = (10, 5))

sns.histplot(df_current_salary_year['current_salary'],
             kde = True)

axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Current Salary Histogram')
plt.xlabel('Current Salary (USD)')

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
axs[0].set_xlabel('Current Salary (USD)')
axs[0].xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

sns.violinplot(x=df_current_salary_year['current_salary'], ax=axs[1])
axs[1].set_title('Current Salary (Filtered by Year)')
axs[1].set_xlabel('Current Salary (USD)')
axs[1].xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

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
plt.xlabel('Salary Raise (%)')

plt.show()

# %% [markdown]
# ### **Data Cleaning and Curation**
# ##### Treatment of current_title

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
colunas = ['timestamp', 'status', 'current_title', 'adjusted_title',
           'current_salary', 'salary_type', 'percent_incr', 'other_info',
           'location', 'performance_rating']

df_blizzard_salary_act = df_blizzard_salary_act.reindex(colunas, axis=1)

# %%
df_blizzard_salary_act.head()

# %%
# Function to Replace Terms Using Regex
def replace_terms(DataFrame, columns, replacements):
    for col in columns:
        for oldvalue, newvalue in replacements.items():
            DataFrame[col] = DataFrame[col].str.replace(oldvalue, newvalue, regex=True)

# Substitution Dictionary
replacements_title = {
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
    r'\bqa\b(?!\s\w)': 'qa analyst',
}

# Applying Replacements
replace_terms(df_blizzard_salary_act, ['adjusted_title'], replacements_title)

# %%
# Check specific adjusted titles
df_blizzard_salary_act[df_blizzard_salary_act['adjusted_title'].str.contains(r".*qa.*", na=False)]['adjusted_title']

# ##### Treatment of location

# %%
# Convert all location entries to lowercase
df_blizzard_salary_act['location'] = df_blizzard_salary_act['location'].str.lower()
df_blizzard_salary_act['location'].value_counts()

# %%
# Drop rows where 'location' is 'laid off 3/16'
df_blizzard_salary_act = df_blizzard_salary_act.drop(df_blizzard_salary_act[df_blizzard_salary_act['location'] == 'laid off 3/16'].index)

# %%
# Substitution Dictionary
replacements_location = {
    # Non-standardized location
    r'.*los angeles center studios.*': 'los angeles',
    r'.*work from home - virginia*': 'virginia',
}

# Applying Replacements
replace_terms(df_blizzard_salary_act, ['location'], replacements_location)

# %% [markdown]
# ##### Treatment of performance_rating

# %%
# Convert all performance_rating entries to lowercase
df_blizzard_salary_act['performance_rating'] = df_blizzard_salary_act['performance_rating'].str.lower()
df_blizzard_salary_act['performance_rating'].value_counts()

# %%
# Substitution Dictionary
replacements_performance_rating = {
    # Non-standardized location
    r'.*developing.*': '1-developing',
    r'.*successful.*': '2-successful',
    r'.*high.*': '3-high',
    r'.*top.*': '4-top',
}

# Applying Replacements
replace_terms(df_blizzard_salary_act, ['performance_rating'], replacements_performance_rating)

# %% [markdown]
# ##### Treatment of current_salary
# To estimate the salary of users who reported hourly/weekly wages, the following formula was used:
# Annual Salary = Hourly Rate × Hours per Week × Weeks per Year

# %%
# Create a new column 'adjusted_salary'
df_blizzard_salary_act['adjusted_salary'] = df_blizzard_salary_act['current_salary']

colunas = ['timestamp', 'status', 'current_title', 'adjusted_title', 'current_salary', 'adjusted_salary', 'salary_type',
       'percent_incr', 'other_info', 'location', 'performance_rating']

df_blizzard_salary_act = df_blizzard_salary_act.reindex(colunas, axis=1)

# %%
# Function to Adjust Salary Based on Type
def adjust_salary(row):
    if row['salary_type'] == 'year':
        return row['current_salary']
    elif row['salary_type'] == 'weekly':
        return row['current_salary'] * 52
    elif row['salary_type'] == 'hour':
        return row['current_salary'] * 40 * 52
    else:
        return 0.0
    
pd.options.display.float_format = '{:,.2f}'.format

df_blizzard_salary_act['adjusted_salary'] = df_blizzard_salary_act.apply(adjust_salary, axis=1)

# %%
# Check adjusted salaries
df_blizzard_salary_act = df_blizzard_salary_act.drop(df_blizzard_salary_act[(df_blizzard_salary_act['adjusted_salary'] < 100)].index)

df_blizzard_salary_act = df_blizzard_salary_act.dropna(subset=['adjusted_salary'])

# %%
# 
df_blizzard_salary_vf = df_blizzard_salary_act

# %% [markdown]
# #### **Exploring Relationships Between Variables**

# %%
# Calculate top/bottom average salary
top_10_salaries = df_blizzard_salary_vf.groupby(['adjusted_title'])['adjusted_salary'].mean().sort_values(ascending=False).nlargest(10)

bottom_10_salaries = df_blizzard_salary_vf.groupby(['adjusted_title'])['adjusted_salary'].mean().sort_values(ascending=False).nsmallest(10)

top_salary = df_blizzard_salary_vf.groupby(['adjusted_title'])['adjusted_salary'].mean().sort_values(ascending=False).nlargest(1)

bottom_salary = df_blizzard_salary_vf.groupby(['adjusted_title'])['adjusted_salary'].mean().sort_values(ascending=False).nsmallest(1)

# %%
# Visualization of top salaries by job title
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.barplot(x=top_10_salaries.values,
            y=top_10_salaries.index,
            hue=top_10_salaries.index,
            palette='viridis',
            errorbar=None)

axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Top 10 Salaries by Job Title')
plt.xlabel('Adjusted Salary')
plt.ylabel('Job Title')

plt.show()

# %%
#Visualization of bottom salaries by job title
fig, axs = plt.subplots(1, 1, figsize = (8, 5))

sns.barplot(x=bottom_10_salaries.values,
            y=bottom_10_salaries.index,
            hue=bottom_10_salaries.index,
            palette='viridis',
            errorbar=None)

plt.title('Bottom 10 Salaries by Job Title')

plt.show()

# %%
# Calculate the percentage difference between top and bottom salary
delta_top_bottom = ((top_salary[0] / bottom_salary[0]) - 1) * 100

# Format the output
formatted_output = f"The difference between the lowest and highest salary is {delta_top_bottom:.2f} %"
print(formatted_output)

# %% [markdown]
# In the top 5 salaries, there are 3 positions within the software engineering function.
# Let's check the performance and average increment for employees with "software engineer" in their title.
# We note that the average increment for software engineers is higher than for those who are not.

# Percentage increase for software engineers
software_engineer_incr_mean = df_blizzard_salary_vf.groupby([df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')])['percent_incr'].mean()
software_engineer_incr_mean_df = software_engineer_incr_mean.reset_index()
software_engineer_incr_mean_df.columns = ['is_software_engineer', 'percent_incr']

plt.bar(software_engineer_incr_mean_df['is_software_engineer'].astype(str),
        software_engineer_incr_mean_df['percent_incr'],
        color=['grey', 'green'])

plt.title('Average Percent Increase by Software Engineers')
plt.xlabel('Is Software Engineer')
plt.ylabel('Percent Increase')

plt.show()

# %%
# Calculate the normalized distribution of ratings for both groups
software_engineer_performance_rating = df_blizzard_salary_vf.groupby([df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')])['performance_rating'].value_counts(normalize=True).unstack(fill_value=0)

# Rename the indices for better readability
software_engineer_performance_rating.index = ['is_not_software_engineer', 'is_software_engineer']

# Reset the index to facilitate use in Seaborn
performance_df = software_engineer_performance_rating.reset_index().melt(id_vars='index', var_name='performance_rating', value_name='proportion')
performance_df.columns = ['type', 'performance_rating', 'proportion']

# %%
# Set the style of the plot
sns.set_theme(style="whitegrid")

# Create the bar plot
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(data=performance_df,
                       x='performance_rating',
                       y='proportion',
                       hue='type',
                       palette='viridis')

# Add title and axis labels
plt.title('Distribution of Performance Rating: Software Engineers vs Non Software Engineers')
plt.xlabel('Performance Rating')
plt.ylabel('Proportion')

# Add labels above the bars with correct alignment
for p in bar_plot.patches:
    height = p.get_height()  
    bar_plot.annotate(f"{height:.2%}", 
                      (p.get_x() + p.get_width() / 2., height), 
                      ha='center', va='bottom')

# Display the plot
plt.legend(title='Title Type')

plt.show()

# %%
# For those labeled as "developing," most are early career and "in test":
print(df_blizzard_salary_vf.loc[
    df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer') & 
    (df_blizzard_salary_vf['performance_rating'] == '1-developing'), 
    ['adjusted_title', 'current_salary', 'performance_rating', 'percent_incr']])

# %%
# Calculate the average salary for software engineers in each job title category
df_blizzard_salary_vf.groupby([df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')])['adjusted_salary'].describe()

# %%
# Calculate the number of software engineers in each job title category
print(df_blizzard_salary_vf[df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')]['adjusted_title'].value_counts())

# %% [markdown]
# ##### Salary Comparison with Market Data
# How do Blizzard salaries compare to market rates?
# I tried to find salary ranges for software engineers in the United States in 2020:
#
# Software engineer salary range by year of experience [x].
#
# | Job Level/Title                            |  Years of Experience           | Base Salary Range
# | :-----------------------:                  |:-----------------------:       |:-----------------------: 
# | Entry/Junior-level software engineer       | 0-3                            | $60-100k
# | Mid-level software engineer                | 3-5                            | $80-130k
# | Senior software engineer                   | 5-7                            | $100-140k
# | Principal sofware engineer                 | 7+                             | $130-200k

# %%
# Create a new column 'software_engineer_group'
df_blizzard_salary_vf['software_engineer_group'] = df_blizzard_salary_vf['adjusted_title']

# Order of columns in the DataFrame
colunas = ['timestamp', 'status', 'current_title', 'adjusted_title', 'software_engineer_group',
       'current_salary', 'adjusted_salary', 'salary_type', 'percent_incr',
       'other_info', 'location', 'performance_rating']

df_blizzard_salary_vf = df_blizzard_salary_vf.reindex(colunas, axis=1)

# %%
# Function to Adjust Salary Based on Type
def software_engineer_group(row):
    if row['software_engineer_group'] == 'associate software engineer' or row['software_engineer_group'] == 'associate software engineer in test':
        return '1_se_entry'
    elif row['software_engineer_group'] == 'software engineer' or row['software_engineer_group'] == 'software engineer in test':
        return '2_se_mid'
    elif row['software_engineer_group'] == 'senior software engineer' or row['software_engineer_group'] == 'senior software engineer in test i' or row['software_engineer_group'] == 'senior software engineer i' or row['software_engineer_group'] == 'senior software engineer ii':
        return '3_se_senior'
    elif row['software_engineer_group'] == 'principal software engineer i' or row['software_engineer_group'] == 'principal software engineer':
        return '4_se_principal'
    else:
        return 'other_title'
    
df_blizzard_salary_vf['software_engineer_group'] = df_blizzard_salary_vf.apply(software_engineer_group, axis=1)

# %% [markdown]
# When comparing salaries between Blizzard's software engineering titles and those found in online research, we have the following results:
# 
# **Entry / Junior level Software Engineer:**
# - The lowest reported salary for entry-level employees at Blizzard is higher than found online (79k vs. 60k [+31.67%]).
# The highest value matches what was found online (100k vs. 100k [+0%]).
# 
# **Mid-level Software Engineer:**
# - For mid-level positions, Blizzard's lowest salary is 25% higher than found online (100k vs. 80k [+25.00%]),
# and the highest is similar (~137k vs. 130k [+5.38%]).
#
# **Senior Software Engineer:**
# - At the senior level, Blizzard's lowest salary is also higher by 20% (120k vs. 100k [+20.00%]).
# However, at the upper limit, the difference is nearly 30% (180k vs. 140k [+28.57%]).
#
# **Principal Software Engineer:**
# - The principal software engineer role shows the largest discrepancy at the lower limit (186k vs. 130k [+43.08%]). At the upper range, the difference is smaller (216k vs. 200k [+8.00%]).
    
# %%
# Describe salary distribution by software engineer title
df_blizzard_salary_vf.groupby(df_blizzard_salary_vf['software_engineer_group'])['adjusted_salary'].describe()

# %%
# Visualization of current salary distributions using violin plots
fig, axs = plt.subplots(1, 1, figsize = (15, 10))

axs = sns.boxplot(y=df_blizzard_salary_vf['adjusted_salary'],
                  x=df_blizzard_salary_vf['software_engineer_group'],
                  fill=False)

axs.axhline(60000, color='red', linestyle='--', linewidth=1)
axs.text(2.8, 61000, 'Internet lower range Entry/Junior Software Engineer', ha='left')

axs.axhline(80000, color='red', linestyle='--', linewidth=1)
axs.text(2.8, 81000, 'Internet lower range Mid-level Software Engineer', ha='left')

axs.axhline(100000, color='red', linestyle='--', linewidth=1)
axs.text(2.8, 101000, 'Internet lower range Senior Software Engineer', ha='left')

axs.axhline(130000, color='red', linestyle='--', linewidth=1)
axs.text(2.8, 131000, 'Internet lower range Principal Software Engineer', ha='left')

plt.title('Distribution of Current Salaries by Software Engineer Title')
plt.xlabel('Software Engineer Title')
plt.ylabel('Adjusted Salary')

plt.show()

# %%
# Histogram of software engineer salaries by location
se_filtered = df_blizzard_salary_vf[df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')]

fig, axs = plt.subplots(1, 1, figsize = (12, 5))

sns.histplot(data=se_filtered,
             x='adjusted_salary', 
             y='location',
             hue='location',
             multiple='stack',
             palette='viridis',
             cbar=True,
             legend=False)

axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Software Engineer Salary by Employement Office Location')
plt.xlabel('Adjusted Salary')
plt.ylabel('Office Location')

plt.show()

# %%
# Histogram of software engineer salaries by performance rating
se_filtered = df_blizzard_salary_vf[df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer')]
se_filtered = se_filtered.sort_values(by='performance_rating', ascending=False)

fig, axs = plt.subplots(1, 1, figsize = (12, 5))

sns.histplot(data=se_filtered,
             x='adjusted_salary', 
             y='performance_rating',
             hue='performance_rating',
             multiple='stack',
             palette='viridis',
             cbar=True,
             legend=False)

axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Software Engineer Salary by Performance Rating')
plt.xlabel('Adjusted Salary')
plt.ylabel('Performance Rating')

plt.show()

# %%
# Correlation between salary and performance rating
filtered_data = df_blizzard_salary_vf[df_blizzard_salary_vf['adjusted_title'].str.contains(r'software engineer', case=False)]
filtered_data = filtered_data.sort_values('performance_rating')

fig, axs = plt.subplots(1, 1, figsize=(12, 5))

sns.histplot(
    data=filtered_data,
    x='adjusted_salary', 
    y='performance_rating',
    hue='performance_rating',
    multiple='stack',
    palette='viridis',
    cbar=True,
    legend=False
)

# Formatando o eixo X para abreviar em milhares (k)
axs.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

plt.title('Current Salary by Employment Office Location')
plt.xlabel('Adjusted Salary')
plt.ylabel('Performance Rating')

plt.show()

# %%