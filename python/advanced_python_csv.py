# -*- coding: utf-8 -*-

from __future__ import print_function,division
import pandas as pd
from advanced_python_regex import q3_results

emails = pd.Series(q3_results,name='emails')

emails.to_csv('emails.csv',index=False)