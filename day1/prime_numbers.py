from math import sqrt

def prime (x):
  
  if x < 0:
    return "Sorry! Prime numbers are positives"
    
  elif x < 2:
    return "Sorry! Prime numbers are greater than 1"
    
  elif x == 2:
    return True
    
  elif type(x) == float:
    return "Sorry, Prime numbers are whole"

  elif x == None:
    return "Please make an entry"
    
  elif x % 2 == 0 or x % sqrt (x) == 0:
    return False
  
  else:
    return True

