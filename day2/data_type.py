def data_type (x):

  if type (x) == str:
    return len (x)

  elif type (x) == type (None):
    return 'no value'

  elif type (x) == bool:
    return x

  elif type (x) == int:
    if x < 100:
      return "less than 100"
    elif x > 100:
      return "more than 100"
    elif x == 100:
      return "equal to 100"
    else:
      pass

  elif type (x) == list:
    if len (x) >= 3:
      return x[2]
    else:
      return None

  else:
    pass