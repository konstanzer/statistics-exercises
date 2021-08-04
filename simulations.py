from math import factorial as f

#I prefer algebra when it's easy.
#6 doubles, 36 pairs
print(6/36)

#8 coins, 3 heads = 8C3 / sample space = .219
print( f(8)/(f(5)*f(3)) / 2**8 )

#8 coins, 4+ heads
coins = 8
space = 2**coins
prob = 0

for n in [4,5,6,7,8]:
	prob += f(coins)/(f(n)*f(coins-n))
prob /= space
# .634
print(prob)

#billboards -> .0625
print(.25**2)

import numpy as np
print("\nsnack attack")
#does it mean after they leave Friday?
#can extra poptarts accumulate?
#dicrete variable, they're arent partial purchases!
n = 10000
t = np.round(np.random.normal(3,1.5,n),0)
t[t<0]=0.
t = t.reshape(2000,5)
t = np.sum(t,axis=1)
t = 17-t
#good enough for government work ~.14
print(np.sum(t>0)/n)

print("\nhts. simulation")
m1, m2 = 178, 170
s1, s2 = 8, 6
n = 5000
men = np.random.normal(m1,s1,n)
women = np.random.normal(m2,s2,n)
#taller woman -> .21
print(np.sum(men<women)/n)

from scipy.stats import norm
#theoretically, P(A-B) < 0
#A-B ~ N(muA-muB, varA-varB) ~ N(8, sqrt(28))
print(norm.cdf(0, 8, np.sqrt(28))) #not the same

print("\ngeometric distribution")
#my anaconda don't
prob = 249/250
#.818 -> .670 -> 1-.548 -> .165
print(prob**450)

#pmf: (1-p)^(k-1)*p
#cdf: 1 - (1-p)^k
p = 1/250 #prob. of success (failed installation)
k = 150
prob = 1 - (1-p)**k
print(1-prob)

print("\nfood truck")
#no food -> .0267 prob.
print(.3**3)
#.9998 prob. a truck+ in a wk.
print(1 - .3**7)

print("\nbirthday paradox")
def prob(folks):
	days, prob = 365, 1
	#this calculates the probability that the next person
	#does not share a bday with all the previous ones
	for f in range(folks):
		prob *= (days-f)/days
	return 1-prob
print(prob(23))
print(prob(20))
print(prob(40))

folks = 40
n = 10000
matches = 0
samples = np.random.randint(1,366,folks*n).reshape(n,folks)

for s in samples:
	for ix, x in enumerate(s):
		if x in s[ix+1:]:
			matches += 1
			break
print(f"Prob. of a match is {matches/n}")



print('\nextra credit')
#which is likely to be higher:
#rolling 6 4-sided dice or 4 6-sided dice?
#4-sided avg. = 2.5 x 6 = 15 <- this guy wins
#6-sided avg. = 3.5 x 4 = 14

space = 6**3
#3 of a kind: 111
three=1/space
#Pair: 11X, 1X1, X11 where X = 2-6
pair=(3*5)/space
#Once: 1XX, X1X, XX1 where X = 2-6
once=(3*5**2)/space

exp_payout = 3*three + 2*pair + once
#lose 50 cents of every $1
print(three, pair, once, exp_payout)




