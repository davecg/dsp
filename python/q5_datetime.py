import datetime

def date_diff(start,stop,fmt):
    # This same function will be used for later problems.
    diff = datetime.datetime.strptime(stop,fmt) - datetime.datetime.strptime(start,fmt)
    return diff.days


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'    
date_fmt = '%m-%d-%Y'  
print date_diff(date_start,date_stop,date_fmt) # 937  

####b)  
date_start = '12312013'  
date_stop = '05282015'  
date_fmt = '%m%d%Y'
print date_diff(date_start,date_stop,date_fmt) # 513  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_fmt = '%d-%b-%Y'
print date_diff(date_start,date_stop,date_fmt) # 7850  
