def fizz_buzz (x):
  
  if (x % 3 == 0 and x % 5 != 0):
    return "Fizz"
    
  elif (x % 5 == 0 and x % 3 != 0):
    return "Buzz"
    
  elif (x % 5 == 0 and x % 3 == 0):
    return "FizzBuzz"
    
  elif (x % 5 != 0 and x % 3 != 0):
    return x
    
  else:
    pass