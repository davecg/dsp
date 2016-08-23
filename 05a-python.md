# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

lists are mutable, tuples immutable.  

dictionary keys must be immutable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

```py
x = range(10) + range(0,10,2) #  list with non-unique numbers  
y = set(x) # removes non-unique values (also unordered)  

print len(x) # 15  
print len(y) # 10  
```

finding an element in a set is much faster since it is implemented as a hashtable.  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

creates a lambda function (shorthand for a one-line minifunction)
```py
mylist = ['xy','z','abc']  
print sorted(mylist, key=lambda x: len(x)) # ['z','xy','abc']  
print sorted(mylist) # ['abc','xy','z']  
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.
```py
mylist = [_**2 for _ in xrange(10) if _ % 2] # [1, 9, 25, 49, 81]  
myaltlist = map(lambda _:_**2,filter(lambda _:_ % 2,xrange(10)))  


myset = {_ for _ in xrange(10) if _ % 2} # {1, 3, 5, 7, 9}  
mydict = {_:_**2 for _ in xrange(10) if _ % 2} # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}  
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```py
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





