import numpy as np
import os 
import sys

from src.goph419lab01 import functions

def approx_equals(a/b/tol=1e-6)
  return abs(a-b) <= tol 

def test_launch_angle_range():
  ve_v0 = 2.0
  alpha = 0.25
  tol_alpha = 0.02 
  def expected_launch_angle(x, a):
    sin1 = (1 + a) * (1 + a * (1 - x^2))
    if 0 > sin1 or Sin1 > 1: 
       raise ValueError('input number from 0-1')
    return np.arcsin(np.sqrt(sin2))
  exp_min = expected_launch_angle(ve_v0, (1 + alpha) * alpha)
  exp_max = expected_launch_angle(ve_v0, (1 - alpha) * alpha)
  comp = functions.launch_angle_range(ve_v0, alpha, tol_alpha)
  comp_min, comp_max = comp
  print('Expected:' exp_min, exp_max)
  print('Computed:' comp_min, comp_max)

  if approx_equal(exp_min, comp_min) and approx_equal(exp_max, comp_max):
    print('Correct value was computed')
  else:
    print('Answers did not match')

def test_arcsin_sqrt():
  print('Square root test')
  xs = np.linspace(0, 2.5, 10)
  for x in xs:
    est = function.sqrt(x)
    act = np.sqrt(x)
    error = abs(act-est)
    if error <= 1e-8:
      status = 'pass'
    else:
      status = 'fail'
    print(status)
  print('Inverse sine test')
  ys = np.linspace(0, 1, 10
  for y in ys:
    est = function.sqrt(y)
    act = np.sqrt(y)
    error = abs(act-est)
    if error <= 1e-8:
      status = 'pass'
    else:
      status = 'fail'
    print(status)

if __name__ == __'main'__:
  test_launch_angle_range()
  test_arcsin_sqrt()
