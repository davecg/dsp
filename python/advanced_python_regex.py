# -*- coding: utf-8 -*-

from __future__ import print_function,division
import pandas as pd
import re
from collections import Counter
from operator import add

data = pd.read_csv('faculty.csv')


def counter(series,split=False,clean=lambda x: x,skip_empty = True):
	count = Counter()
	for item in series.values:
		if split:
			for sub_item in item.split():
				if skip_empty and sub_item == '':
					continue
				count[clean(sub_item)] += 1
		else:
			if skip_empty and item == '':
				continue
			count[clean(item)] += 1
	return count


#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

q1_results = counter(
				data[' degree'],
				split=True,
				clean=lambda x: x.strip().lower().replace('0','').replace('.','')
				)

print(q1_results)

# Counter({'phd': 31, 'scd': 6, 'mph': 2, 'ms': 2, '': 1, 'md': 1, 'ma': 1, 'bsed': 1, 'jd': 1})

#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor

# Fixing typo for 'Assistant Professor is Biostatistics'

q2_results = counter(
					data[' title'],
					clean=lambda x: re.sub(r'\bis\b','of',x)
					)

print(q2_results)

#Q3. Search for email addresses and put them in a list. Print the list of email addresses.

q3_results = data[' email'].values

print(q3_results)

#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

q4_data = counter(
				data[' email'],
				clean=lambda x: re.sub(r'^.*\@([A-Za-z\.]+).*',r'\1',x)
				)

# if you really just want the domains and not their counts too...
q4_results = q4_data.keys()

print(q4_results)
