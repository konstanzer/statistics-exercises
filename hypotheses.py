'''
For each, formulate a null & alternative hypothesis.
Give examples of type I and type II errors would look like.

    Has the network latency gone up since we switched internet service providers?
    H0 Latency means are equal before and after switch.
    H1 Latency means are not equal before and after switch.
    T1 RTN - latency means are equal, I say they are not
    T2 Do not RTN - latency means are not equal, I say they are

    Is the website redesign any good?
    H0 New and old website have same mean CTR
    H1 New website has higher mean CTR
    T1 RTN - New website has same or lower CTR, I say it has higher CTR 
    T2 Do not RTN - new website has higher CTR, I say it does not

    Is our television ad driving more sales?
    H0 Sales are the same before and after ad
    H1 Sales increase after ad
    T1 RTN - Ad has no effect, I say it increases sales
    T2 Do not RTN - Ad increased sales, I say it did not

----------------

A sample of 40 sales from office #1 has a mean of 90 days & a standard deviation of 15 days.
A sample of 50 sales from office #2 has a mean of 100 days & a standard deviation of 20 days.
Use a .05 alpha to determine if means are equal.

The Welch's t-test, unlike Student's t-test, does not assume the two populations (in this case the signed in and non-signed in users) from which the samples are drawn have the same variance. By specifying the equal_var argument to be False, ttest_ind becomes Welch's t-test effectively.

scipy.stats.ttest_ind(a, b, equal_var=False)

On the other hand, the Welch's t-test does assume that the two populations are normally distributed.

Using mpg dataset: Is there a difference in fuel-efficiency in cars from 2008 vs 1999? Are compact cars more fuel-efficient than the average car? Do manual cars get better gas mileage than automatic cars?
'''
import numpy as np
import scipy.stats as scs
from pydataset import data

mpg = data('mpg')
print(mpg.head(2))

a = mpg.hwy[mpg.year==2008]
b = mpg.hwy[mpg.year==1999]
print(np.mean(a), np.mean(b))
print(f"p-value: {scs.ttest_ind(a, b)[1]}")
print("There is no f-ing way we can reject the null with either city of highway mileage.\n")

a = mpg.hwy[mpg['class']=='compact']
b = mpg.hwy[mpg['class']!='compact']
print(np.mean(a), np.mean(b))
print(f"p-value: {scs.ttest_ind(a, b)[1]}")
print("Absolutely! Compact cars get better city and highway mileage.\n")

a = mpg.cty[mpg.trans.str.startswith('auto')]
b = mpg.cty[mpg.trans.str.startswith('manu')]
print(np.mean(a), np.mean(b))
print(f"p-value: {scs.ttest_ind(a, b)[1]}")
print("Indeed, yes, manual trans gets better city and highway mileage.\n")

'''
Use telco_churn data: Does tenure correlate with monthly charges? Total charges? What happens if you control for phone and internet service?
Use the employees database: Is there a relationship between how long an employee has been with the company and their salary? Is there a relationship between how long an employee has been with the company and the number of titles they have had?
Use the sleepstudy data: Is there a relationship between days and reaction time?
'''
import pandas as pd

telco = pd.read_csv('Kaggle_Telco.csv')
telco.replace(" ", 0, inplace=True) #damnnnnnn
telco = telco.astype({'TotalCharges': np.float})
print(telco.head(1))

res = scs.pearsonr(telco.tenure, telco.MonthlyCharges)
print(f"\ncorr. coeff: {res[0]}")
print(f"2-tailed p-value: {res[1]}. Monthly payments correlated with time.")

res = scs.pearsonr(telco.tenure, telco.TotalCharges)
print(f"\ncorr. coeff: {res[0]}")
print(f"2-tailed p-value: {res[1]}.  Total payments more correlated with time.")

print(telco.MultipleLines.value_counts()) #No is top (1 line)
print(telco.InternetService.value_counts()) #Fiber optic is top

fiber_oneline = telco[(telco.MultipleLines=='No') & (telco.InternetService=='Fiber optic')]
print(f"Only using {len(fiber_oneline)} people with fiber optic and 1 phone line.")
res = scs.pearsonr(fiber_oneline.tenure, fiber_oneline.MonthlyCharges)
print(f"\ncorr. coeff: {res[0]}")
print(f"2-tailed p-value: {res[1]}.  Correlation of time and monthly charges is higher when internet & phone service are unchanged.")
res = scs.pearsonr(fiber_oneline.tenure, fiber_oneline.TotalCharges)
print(f"\ncorr. coeff: {res[0]}")
print(f"2-tailed p-value: {res[1]}.  Correlation of time and total charges is almost 1.\n")

#employees
from env import host, username, password
def get_db_url(username, host, password, db): return f'mysql+pymysql://{username}:{password}@{host}/{db}'
url = get_db_url(username, host, password, 'employees')
query = """
        SELECT salary, DATEDIFF(now(),employees.hire_date) days
        FROM employees
        JOIN salaries USING(emp_no)
        WHERE salaries.to_date > now();
        """
#emps = pd.read_sql(query, url)
#print(emps.head())
#res = scs.pearsonr(emps.salary, emps.days)
#print(f"\ncorr. coeff: {res[0]}")
#print(f"2-tailed p-value: {res[1]}. Pos. correlation of days & salary\n")

query = """
        SELECT count(*) titles, DATEDIFF(now(),employees.hire_date) days
        FROM employees
        JOIN titles USING(emp_no)
        GROUP BY title.title;
        """
#emps = pd.read_sql(query, url)
#print(emps.head())
#res = scs.pearsonr(emps.titles, emps.days)
#print(f"\ncorr. coeff: {res[0]}")
#print(f"2-tailed p-value: {res[1]}. Pos. correlation of days & salary\n")

#sleep
sleep = data('sleepstudy')
print(sleep.head())
res = scs.pearsonr(sleep.Days, sleep.Reaction)
print(f"\ncorr. coeff: {res[0]}")
print(f"2-tailed p-value: {res[1]}. Yeah, days and reactions are positively correlated.")

'''
Is using a macbook independent from being a codeup student?
mac/student T | F
T          49  20
F          1   30

Make chi-square contingency table test for two mpg categorical variables. State your null and alternative hypotheses.

Use the data from the employees database: Is an employee's gender independent of whether an employee works in sales or marketing? (only look at current employees) Is an employee's gender independent of whether or not they are or have been a manager?
'''
observed = pd.DataFrame([[49, 20], [1, 30]], index=['T','F'], columns=['T','F'])
#H0 Macbook usage us unrelated to whether or not a person is a student.
#H1 Macbook usage is affected by student status.
print(observed)
chi2, p, degf, expected = scs.chi2_contingency(observed)
print(f"---\nExpected {expected}")
#a resounding RTN
print(f'chi^2, p = {chi2, p}')


query = """
        SELECT *
        FROM employees
        JOIN titles USING(emp_no)
        GROUP BY title.title;
        """
#emps = pd.read_sql(query, url)
#print(emps.head())
