# Matrix Algebra
# coding: utf-8

# See iPython Notebook for output (or run script).

# In[1]:

import sympy
sympy.init_printing(use_latex=True)


# In[2]:

A = sympy.Matrix([[1,2,3],[2,7,4]])
B = sympy.Matrix([[1,-1],[0,1]])
C = sympy.Matrix([[5,-1],[9,1],[6,0]])
D = sympy.Matrix([[3,-2,-1],[1,2,3]])
u = sympy.Matrix([6,2,-3,5]).T
v = sympy.Matrix([3,5,-1,4]).T
w = sympy.Matrix([1,8,0,5])


# In[3]:

#1. Matrix Dimensions
for i,x in enumerate((A,B,C,D,u,w),start=1):
    print('#1.{}:'.format(i))
    sympy.pprint(x.shape)


# In[4]:

#2. Vector Operations
for i,x in enumerate((
        u+v,
        u-v,
        6*u,
        u.dot(v),
        u.norm(),
    ),start=1):
    print('#2.{}: '.format(i))
    sympy.pprint(x)


# In[5]:

#3. Matrix Operations
for i,x in enumerate((
        'not defined', # A + C,
        A - C.T,
        C.T + 3*D,
        B * A,
        'not defined', # B * A.T,
        'not defined', # B * C,
        C * B,
        B**4,
        A * A.T,
        D.T * D,
    ),start=1):
    print('#3.{}:'.format(i))
    sympy.pprint(x)

'''
Output:

#1. Matrix Dimensions

#1.1:
(2, 3)
#1.2:
(2, 2)
#1.3:
(3, 2)
#1.4:
(2, 3)
#1.5:
(1, 4)
#1.6:
(4, 1)

#2. Vector Operations

#2.1: 
[9  7  -4  9]
#2.2: 
[3  -3  -2  1]
#2.3: 
[36  12  -18  30]
#2.4: 
51
#2.5: 
√74

#3. Matrix Operations

#3.1:
not defined
#3.2:
⎡-4  -7  -3⎤
⎢          ⎥
⎣3   6   4 ⎦
#3.3:
⎡14  3  3⎤
⎢        ⎥
⎣2   7  9⎦
#3.4:
⎡-1  -5  -1⎤
⎢          ⎥
⎣2   7   4 ⎦
#3.5:
not defined
#3.6:
not defined
#3.7:
⎡5  -6⎤
⎢     ⎥
⎢9  -8⎥
⎢     ⎥
⎣6  -6⎦
#3.8:
⎡1  -4⎤
⎢     ⎥
⎣0  1 ⎦
#3.9:
⎡14  28⎤
⎢      ⎥
⎣28  69⎦
#3.10:
⎡10  -4  0 ⎤
⎢          ⎥
⎢-4  8   8 ⎥
⎢          ⎥
⎣0   8   10⎦

'''


