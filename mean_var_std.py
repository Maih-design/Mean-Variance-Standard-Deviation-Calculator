import numpy as np
import panda as pd

def calculate(input):
  if len(input) != 9:
    raise ValueError( "List must contain nine numbers.")
  m = np.array(input).reshape(3,3)

  output = {
    'mean': [m.mean(axis=0), m.mean(axis=1), m.mean()],
  'variance': [m.var(axis=0), m.var(axis=1), m.var()],
  'standard deviation': [m.std(axis=0), m.std(axis=1), m.std()],
  'max': [m.max(axis=0), m.max(axis=1), m.max()],
  'min': [m.min(axis=0), m.min(axis=1), m.min()],
  'sum': [m.sum(axis=0), m.sum(axis=1), m.sum()]
  }
  return output
