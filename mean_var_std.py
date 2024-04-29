import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list)
    arr.resize((3, 3))
    calculations = {
  'mean': [],
  'variance': [],
  'standard deviation': [],
  'max': [],
  'min': [],
  'sum': []
  }
    calculations['mean'].append(arr.mean(axis=0).tolist())
    calculations['mean'].append(arr.mean(axis=1).tolist())
    calculations['mean'].append(arr.mean().tolist())
    calculations['variance'].append(arr.var(axis=0).tolist())
    calculations['variance'].append(arr.var(axis=1).tolist())
    calculations['variance'].append(arr.var().tolist())
    calculations['standard deviation'].append(arr.std(axis=0).tolist())
    calculations['standard deviation'].append(arr.std(axis=1).tolist())
    calculations['standard deviation'].append(arr.std().tolist())
    calculations['max'].append(arr.max(axis=0).tolist())
    calculations['max'].append(arr.max(axis=1).tolist())
    calculations['max'].append(arr.max().tolist())
    calculations['min'].append(arr.min(axis=0).tolist())
    calculations['min'].append(arr.min(axis=1).tolist())
    calculations['min'].append(arr.min().tolist())
    calculations['sum'].append(arr.sum(axis=0).tolist())
    calculations['sum'].append(arr.sum(axis=1).tolist())
    calculations['sum'].append(arr.sum().tolist())
    #function returns the dictionary at the end
    return calculations