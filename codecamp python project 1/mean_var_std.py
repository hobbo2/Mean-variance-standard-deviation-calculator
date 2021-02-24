import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')

  else:
    arr = np.array(list).reshape(3,3)

    mean = [arr.mean(axis = 0).tolist(),
               arr.mean(axis = 1).tolist(),
               arr.mean().tolist()]


    VAR = [arr.var(axis = 0).tolist(),
              arr.var(axis = 1 ).tolist(),
              arr.var().tolist()]

    STD = [arr.std(axis = 0).tolist(),
              arr.std(axis = 1).tolist(),
              arr.std().tolist()]

    MAX = [arr.max(axis = 0).tolist(),
              arr.max(axis = 1).tolist(),
              arr.max().tolist()]

    Min =[arr.min(axis = 0).tolist(),
              arr.min(axis = 1).tolist(),
              arr.min().tolist()]

    Sum = [arr.sum(axis=0).tolist(),
              arr.sum(axis=1).tolist(),
              arr.sum().tolist()]


    calculations = {
            'mean': mean ,
            'variance': VAR,
            'standard deviation': STD,
            'max': MAX,
            'min': Min,
            'sum': Sum

        }
  return calculations