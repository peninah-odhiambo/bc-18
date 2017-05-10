def find_max_min (points):

  output = []
  min_value = points [0]
  max_value = points [1]
  
  for value in points:
    if value < min_value:
      min_value = value
    elif value > max_value:
      max_value = value
      
  if min_value == max_value:
    output.append(len (points))
    
    return output

  else:
    output.insert (0,min_value)
    output.insert (1,max_value)
    
    return output

numbers = [100,100]
print find_max_min (numbers)


numbers = [1,2,4,5,2,1]
print find_max_min (numbers)


