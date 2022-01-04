import pandas as pd
import matplotlib
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")

# Find duplicates and drop them
df.duplicated().sum()
df = df.drop_duplicates()

# Find missing values and replace with highest frequency value
df.isnull().sum()
df['WorkLoc'].isnull().sum()
df['WorkLoc'].value_counts()
v = df['WorkLoc'].value_counts()[0]
df['WorkLoc'] = df['WorkLoc'].fillna('Office')

# Normalising data and adding a new normalised column
def normalisecomp(row):
    if row['CompFreq'] == 'Monthly':
        v = row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        v = row['CompTotal'] * 52
    else:
        v = row['CompTotal']
    return v

df['NormalizedAnnualCompensation'] = df.apply(normalisecomp, axis = 1)

# Data visualisation using SQL queries in Python
import sqlite3
conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection

# histogram of ConvertedComp
QUERY = """
SELECT ConvertedComp 
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
df.hist()

# box plot of Age
QUERY = """
SELECT Age 
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
df.boxplot()

# scatter plot of Age and WorkWeekHrs
QUERY = """
SELECT Age, WorkWeekHrs
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
df.plot.scatter(x = 'Age', y = 'WorkWeekHrs')

# bubble plot of WorkWeekHrs and CodeRevHrs, use Age column as bubble size
QUERY = """
SELECT Age, WorkWeekHrs, CodeRevHrs
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
df.plot.scatter(x = 'WorkWeekHrs', y = 'CodeRevHrs', s = 'Age')

# pie chart of the top 5 databases that respondents wish to learn next year
QUERY = """
SELECT DatabaseDesireNextYear, COUNT(DatabaseDesireNextYear) as Count
FROM DatabaseDesireNextYear
GROUP BY DatabaseDesireNextYear
ORDER BY Count DESC
"""
df = pd.read_sql_query(QUERY,conn).head()
df.plot.pie(y = 'Count', autopct='%1.1f%%', labels = df['DatabaseDesireNextYear'])

# stacked chart of median WorkWeekHrs and CodeRevHrs for the age group 30 to 35
QUERY = """
SELECT WorkWeekHrs, CodeRevHrs
FROM master
WHERE Age > 30 and Age < 35
"""
df = pd.read_sql_query(QUERY,conn)
df[['WorkWeekHrs','CodeRevHrs']].plot(kind='bar', stacked=True)