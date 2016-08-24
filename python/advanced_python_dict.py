# -*- coding: utf-8 -*-

from __future__ import print_function,division
import pandas as pd
from collections import defaultdict
import re

data = pd.read_csv('faculty.csv')
data['short_title'] = data[' title'].apply(
	lambda x: re.sub(r'\s+\w{2}\s+Biostatistics\s*','',x)
	)
# lambda x: re.sub(r'^\s*(.*)\s+(\S+)\s*$',r'\2',x)

'''
Q6. Create a dictionary in the below format:

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

Print the first 3 key and value pairs of the dictionary:

'''

q6_dict = defaultdict(list)
q7_dict = {}

for idx,row in data.iterrows():
	name,title,degree,email = row[['name','short_title',' degree',' email']]
	first,last = re.findall(r'^\s*(.*)\s+(\S+)\s*$',name)[0]
	q6_dict[last].append([degree,title,email])
	q7_dict[(first,last)] = [degree,title,email]

print('Q6')
for key in sorted(q6_dict.keys())[:3]:
	print(key,q6_dict[key])

'''

Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

Print the first 3 key and value pairs of the dictionary:

'''

# Including middle names/initials/etc as part of first name field.
# This is usually how things are done for citations, e.g. "Smith, J.A.".

print('Q7')
for key in sorted(q7_dict.keys())[:3]:
	print(key,q7_dict[key])

#Q8. It looks like the current dictionary is printing by first name. Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

print('Q8')
for key in sorted(q7_dict.keys(),key=lambda x: x[1])[:3]:
	print(key,q7_dict[key])