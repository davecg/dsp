# Matrix Algebra
# coding: utf-8

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


