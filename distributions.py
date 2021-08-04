#simulate and/or calculate
from math import e, factorial
import scipy.stats as scs
import matplotlib.pyplot as plt
import numpy as np

print("\nPois(lambda)")
#lambda = E(X) = Var(X)
lambd = 2
#pmf
def pmf(x): return (lambd**x * e**-lambd)/factorial(x)
k = range(10)
plt.plot(k, list(map(pmf, k)))
plt.savefig('poisson.png')

#prob. k == 0 = .135
print(pow(e, -lambd))
print(scs.poisson.pmf(k=0, mu=2))
#prob. k > 2 = .323
print(scs.poisson.sf(k=2, mu=2))
#prob. k > 0 = .865
print(scs.poisson.sf(k=0, mu=2))
print(1-.135) #from no. 1

print("\nN ~ 3, 0.3")
mu, sigma = 3., .3
def pdf(x): return scs.norm.pdf(x, mu, sigma)
x = np.linspace(mu-2, mu+1)
plt.plot(x, list(map(pdf, x)))
plt.savefig('normal.png')

#ppf is inverse of cdf
def ppf(x): return scs.norm.ppf(x, mu, sigma)
print(ppf(.95)) #top 5% 3.49
print(ppf(.15)) #15th percentile 2.69
print(ppf(.3)) #yes
print(scs.norm.cdf(3.5, mu, sigma)) #.952
#why is pdf over 1 sometimes?
#it's not a probability, AUC still adds up to 1
plt.clf()

print("\nBinomial")
ctr = .02
n = 4326
k = 97
print(scs.binom.sf(k, n, ctr)) #.118

r = scs.binom.rvs(n, ctr, size=5000)
plt.hist(r, bins=30)
plt.savefig('binomial.png')
plt.clf()

#getting one right
print("\nGeometric")
p = .01
x = 60
print(scs.geom.cdf(x, p)) #.453
print(1-(1-p)**x)

r = scs.geom.rvs(p, size=5000)
plt.hist(r, bins=100)
plt.savefig('geometric.png')
plt.clf()

#looking for a single success therefore geometric again
p, students = .03, int(66*.9)
print(scs.geom.cdf(students, p))
print(scs.geom.sf(2*students, p))
print(scs.geom.sf(5*students, p))

print("\nN ~ 30, 6")
mu, sigma = 15*2, 3*2 #minutes
#P(X <= 35) acc. for 25 min. needed
r = scs.norm.rvs(loc=mu, scale=sigma, size=5000)
plt.hist(r, bins=20)
plt.savefig('normal2.png')
plt.clf()
# cdf means "less than or equal to"
print(scs.norm.cdf(35, mu, sigma)) #.798


#employees db 
mu, sigma = 72012, 17310

x = list(range(int(mu-sigma*3), int(mu+sigma*3)))
#probs = [scs.norm.pdf(i, mu, sigma) for i in x]
#plt.plot(x, probs)
#plt.savefig('normal3.png')

#model
print(scs.norm.cdf(60000, mu, sigma)) #.244
print(scs.norm.sf(95000, mu, sigma)) #.092
print(scs.norm.cdf(80000, mu, sigma) - scs.norm.cdf(65000, mu, sigma)) #.335
print(scs.norm.ppf(.95, mu, sigma)) #100,484

#data, queries in sequel ace
print("\nLess than 60K: .271")
print("More than 95K: .109")
print("65K-80K: .325")
print("95th percentile: 104228")


