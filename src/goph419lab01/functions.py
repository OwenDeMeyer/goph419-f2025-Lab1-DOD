def factorial(n):
   return 1 if n == 0 else n * factorial(n - 1)

def sqrt(a):
"""This will use five base point to generalize it, so any number from 0-0.75 will be 0.5 and then we set a sqrt number to this value, for example. 
Parameters are (a) which represents the number we are finding the square root for from 0-2.5
----------
Returns y, which will be the square root of the number inputted
-------
"""
input (a)
if a<0 or a>2.5
  raise ValueError('Input number from 0-2.5')
if x ==0:
  return 0.0
if x ==0:
  return 1.0

 
term = a
result = term
# implementation of positive square root
# (using Taylor series)
return y

def arcsin(a):
"""Description of function.
Parameters Input number 'a' to compute arcsin for, must be between 0-1
----------
Returns the result after the while loop is completed
-------
"""
if a<0 or a>1:
  raise ValueError('Input number from 0-1')

term = a #first term
result = term 
old_result = float('inf') #to force the loop to run at least once
n = 1 

cond = 1e-9 #condition for 8 significant figures

while abs(result - old_result) > cond:

  denom = (n**2) * (factorial(2*n) / ((factorial(n))**2))
  term = ((2*a)**(2*n)) / denom
  old_result = result 
  result += term
  n += 1
  y = (result*0.5)**0.5 
# implementation of arcsin
# (using the series from Borwein and Chamberlain 2007)
return y

def launch_angle_range(ve_v0, alpha, tol_alpha):
"""Description of function.
Parameters
----------
Returns
-------
"""
# ...
# your implementation here should call on your
# functions implementing Equations (17) and (18)
# ...
return phi_range


