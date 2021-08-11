import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
from scipy import stats


roll  = stats.randint(1, 7)


plt.hist(roll.rvs(100000), bins= [1,2,3,4,5,6,7], align = 'left', width = 0.9)
plt.title('Uniform Population distribution')


roll.rvs(100000).mean()


# get data from pydataset
df = data('tips')


df.head()


# pandas crosstab to make a 'contingency' table
observed = pd.crosstab(df.smoker, df.time)


# Set our alpha
alpha = 0.05


# chi2_contingency returns 4 different values




print('Observed\n')
print(observed.values)
print('---\nExpected\n')
print(expected.astype(int))
print('---\n')
print(f'chi^2 = {chi2:.4f}')
print(f'p     = {p:.4f}')


if p < alpha:
    print('We reject the null')
else:
    print("we fail to reject the null")


# get your data
df = pd.read_csv("https://gist.githubusercontent.com/ryanorsinger/6ba2dd985c9aa92f5598fc0f7c359f6a/raw/b20a508cee46e6ac69eb1e228b167d6f42d665d8/attrition.csv")


# check the head
df.head()


# check shape of the dataframe
df.shape


# Check for which columns are discrete/categorical?
df.nunique()


# look at # of categories in Attrition column
observed=pd.crosstab(df.Attrition, df.Department)
observed


# look at # of categories in business travel

stats.chi2_contingency(observed)


# Crosstab Attrition vs Business Travel




# Set our alpha

alpha = ?


# .chi2_contingency returns 4 different values




print('Observed\n')
print(observed.values)
print('---\nExpected\n')
print(expected.astype(int))
print('---\n')
print(f'chi^2 = {chi2:.4f}')
print(f'p     = {p:.4f}')


null_hypothesis = "Attrition and Business Travel are independent"

if p < alpha:
    print("We reject the hypothesis that", null_hypothesis)
else:
    print("We fail to reject the null hypothesis")




# how many categories we have in 'Department' column? (hint: value_counts())



# crosstab for observed values between Attrition and Depts



# use stats.chi2_contingency test 







