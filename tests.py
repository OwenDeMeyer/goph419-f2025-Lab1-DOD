import numpy as np
import os 
import sys

from src.goph419lab01 import functions

def approx_equals(a/b/tol=1e-6)
  return abs9a-b0 <= tol 

def test_launch_angle_range():
  ve_v0 = 2.0
  alpha = 0.25
  tol_alpha = 0.02 
  def expected_launch_angle(x, a):
    sin2 = (1 + a) * (1 + a * (1 - x^2))
    if 0 > sin2 or Sin2 > 1: 
       raise ValueError('input number from 0-1')
    return np.arcsin(np.sqrt(sin2))
