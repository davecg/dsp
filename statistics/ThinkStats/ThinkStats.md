
# Problem Sets

* 2-4-cohens_d
* 3-1-actual_biased
* 4-2-random_dist
* 5-1-blue_men
* 6-1-household_income
* 7-1-weight_vs_age
* 8-2-sampling_dist
* 8-3-scoring
* 9-2-resampling


```python
%matplotlib inline
from __future__ import division
import numpy as np
import pandas as pd
import os, os.path
code_dir = '/Users/dave/Desktop/metis/prework/ThinkStats2/code'
os.chdir(code_dir)
```


```python
# 2-4-cohens_d

import nsfg
import thinkstats2
import thinkplot
import math
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
def CohenEffectSize(g1,g2):
    d = g1.mean() - g2.mean()
    pooled_var = (len(g1)*g1.var() + len(g2)*g2.var())/(len(g1)+len(g2))
    return d/math.sqrt(pooled_var)


print "## 2.4 Cohen's d"
for col in ('prglngth','totalwgt_lb'):
    print('* {}: {}'.format(col,CohenEffectSize(firsts[col],others[col])))
```

    ## 2.4 Cohen's d
    * prglngth: 0.0288790446544
    * totalwgt_lb: -0.0886729270726



```python
# 3-1-actual_biased
import chap01soln
resp = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh,label='Actual')
bias_pmf = pmf.Copy(label='observed')
for x,p in pmf.Items():
    bias_pmf.Mult(x,x)

print('## 3-1-actual_biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,bias_pmf])
thinkplot.Show(xlabel='numbers of kids per household',ylabel='PMF')
print('PMF: {}'.format(pmf.Mean()))
print('Biased PMF: {}'.format(bias_pmf.Mean()))
```

    ## 3-1-actual_biased



![png](output_3_1.png)


    PMF: 1.02420515504
    Biased PMF: 2.46186052597



    <matplotlib.figure.Figure at 0x115542b90>



```python
## 4-2-random_dist
import random
data = [random.random() for _ in xrange(1000)]
pmf = thinkstats2.Pmf(data,)
cdf = thinkstats2.Cdf(data,)
print('## 4-2-random_dist')
thinkplot.Pmf(pmf)
thinkplot.Show(ylabel='PMF',xlabel='value')
thinkplot.Cdf(cdf)
thinkplot.Show(ylabel='CDF',xlabel='value')
print 'Distribution is uniform'
```

    ## 4-2-random_dist


    /Users/dave/anaconda/lib/python2.7/site-packages/matplotlib/axes/_axes.py:519: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
      warnings.warn("No labelled objects found. "



![png](output_4_2.png)



![png](output_4_3.png)


    Distribution is uniform



    <matplotlib.figure.Figure at 0x116f35f10>



```python
## 5-1-blue_men
import scipy.stats
lower,upper = scipy.stats.norm.cdf(
        [177.8,185.42],
        loc=178,
        scale=7.7,
)
print('## 5-1-blue_men')
print('{0:0.1%}'.format(upper - lower))
```

    ## 5-1-blue_men
    34.3%



```python
# [Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)
import hinc
import hinc2

hinc_df = hinc.ReadData()
hinc_log_sample = hinc2.InterpolateSample(hinc_df,log_upper=6.0)


hinc_cdf = thinkstats2.Cdf(hinc_log_sample)


print '## 6-1-household_income'
hinc_output = {}
hinc_output['median'] = hinc_cdf.Value(0.5)
hinc_output['mean'] = thinkstats2.RawMoment(hinc_log_sample,1)
hinc_var = thinkstats2.CentralMoment(hinc_log_sample,2)
hinc_std = math.sqrt(hinc_var)
hinc_output['skewness'] = thinkstats2.CentralMoment(hinc_log_sample,3)/(hinc_std ** 3)
hinc_output["Pearson's skewness"] = 3*(hinc_output['mean'] - hinc_output['median'])/hinc_std
for k,v in sorted(hinc_output.items()):
    print '{}: {:0.4}'.format(k,v)

print 'Fraction below mean: {:0.2%}'.format(hinc_cdf[hinc_output['mean']])
print 'Increasing the upper bound increases the mean more than it increases the median, increasing skewness.'
```

    hinc.py:51: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      df[0][0] -= 1
    hinc2.py:33: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      df.log_lower[0] = 3.0
    hinc2.py:36: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      df.log_upper[41] = log_upper


    ## 6-1-household_income
    Pearson's skewness: -0.3379
    mean: 4.658
    median: 4.709
    skewness: -0.6414
    Fraction below mean: 45.06%
    Increasing the upper bound increases the mean more than it increases the median, increasing skewness.



```python
#preg = nsfg.ReadFemPreg()
print '## 7-1-weight_vs_age'
preg = preg.dropna(subset=['totalwgt_lb','agepreg'])
thinkplot.Scatter(preg.totalwgt_lb,preg.agepreg)
thinkplot.Show(xlabel='totalwgt_lb',ylabel='agepreg')
totalwgt_lb_cdf = thinkstats2.Cdf(preg.totalwgt_lb)
agepreg_cdf = thinkstats2.Cdf(preg.agepreg)
thinkplot.Scatter(thinkstats2.Jitter([int(totalwgt_lb_cdf[_]*100) for _ in preg.totalwgt_lb],1),
                  thinkstats2.Jitter([int(agepreg_cdf[_]*100) for _ in preg.agepreg],1))
thinkplot.Show(xlabel='totalwgt_lb %ile',ylabel='agepreg %ile')
for method in ('pearson','spearman'):
    print "{}'s: {}".format(method,preg.totalwgt_lb.corr(preg.agepreg,method=method))
print 'Not correlated.'
```

    ## 7-1-weight_vs_age



![png](output_7_1.png)



![png](output_7_2.png)


    pearson's: 0.0688339703541
    spearman's: 0.0946100410966
    Not correlated.



    <matplotlib.figure.Figure at 0x123a8b550>



```python
from estimation import RMSE, MeanError

print '## 8-2-sampling_dist'

def expon_sample(n=10,lam=2):
    xs = np.random.exponential(1.0/lam,n)
    L = 1/np.mean(xs)
    return L

l_estimates = [expon_sample() for _ in xrange(1000)]
#l_pmf = thinkstats2.Pmf(l_estimates)
l_cdf = thinkstats2.Cdf(l_estimates)
thinkplot.Cdf(l_cdf)
thinkplot.Show(ylabel='CDF')
print 'Standard error: {:0.4}'.format(RMSE(l_estimates,2.))
print 'Confidence interval: [{:0.4},{:0.4}]'.format(l_cdf.Value(0.10),l_cdf.Value(0.90))

def std_error_vs_n(n,lam=2,repeats=1000):
    l_estimates = [expon_sample(n,lam) for _ in xrange(repeats)]
    return RMSE(l_estimates,lam)

n_s = [2**_ for _ in xrange(2,10)]
errors = [std_error_vs_n(n) for n in n_s]
thinkplot.Plot(n_s,errors)
thinkplot.Show(ylabel='RMSE',xlabel='n')
```

    ## 8-2-sampling_dist



![png](output_8_1.png)


    Standard error: 0.7824
    Confidence interval: [1.459,3.21]



![png](output_8_3.png)



    <matplotlib.figure.Figure at 0x10410b250>



```python
print '## 8-3-scoring'

def game(lam=2.,time=1):
    goals = 0
    while time > 0:
        time -= np.random.exponential(1/lam)
        if time > 0:
            goals += 1
    return goals

def multiple_games(repeats=10000,lam=2,time=1,display=False):
    simulations = [game(lam,time) for _ in xrange(repeats)]
    cdf = thinkstats2.Cdf(simulations)
    if display:
        print('RMSE: {}'.format(RMSE(simulations,lam)))
        print('Mean Error: {}'.format(MeanError(simulations,lam)))
        print('Confidence interval:[{},{}]'.format(cdf.Value(0.1),cdf.Value(0.9)))
        thinkplot.Cdf(cdf)
        thinkplot.Show(ylabel='CDF')
    return RMSE(simulations,lam)

multiple_games(display=True)
print 'Does not appear to be biased.'
errors = [multiple_games(lam=lam) for lam in xrange(1,20)]
thinkplot.Plot(range(1,20),errors)
thinkplot.Show(xlabel='lambda',ylabel='RMSE')
print 'RMSE increases with Lambda'
```

    ## 8-3-scoring
    RMSE: 1.39857069896
    Mean Error: 0.0122
    Confidence interval:[0,4]



![png](output_9_1.png)


    Does not appear to be biased.



![png](output_9_3.png)


    RMSE increases with Lambda



    <matplotlib.figure.Figure at 0x120e0d590>



```python
# 9-2-resampling

import first
from hypothesis import DiffMeansPermute

class DiffMeansResample(DiffMeansPermute):
    def RunModel(self):
        group1 = np.random.choice(self.pool,self.n,replace=True)
        group2 = np.random.choice(self.pool,self.m,replace=True)
        return group1,group2

lives, firsts, others = first.MakeFrames()

print '## 9-2-resampling'
for col in ['prglngth','totalwgt_lb']:
    data = firsts[col].dropna().values,others[col].dropna().values
    ht = DiffMeansResample(data)
    ht_permute = DiffMeansPermute(data)
    pvalue = ht.PValue()
    pvalue_permute = ht_permute.PValue()
    print('{}: {} ({})'.format(col,pvalue,pvalue_permute))
print('Resampling vs permutation does not change results much.')
```

    ## 9-2-resampling
    prglngth: 0.174 (0.168)
    totalwgt_lb: 0.0 (0.0)
    Resampling vs permutation does not change results much.

