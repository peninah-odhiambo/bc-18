any_word = "olly olly in come free"
ninah = "When one adds 2 and when one adds 2 one gets 4"

def words(word):
  
  """This will return a dictionary with the key as word and the value as the count"""
  
  string_dict = {}
  
  list_of_words = word.split()
  
  #This indicates the words in the string.
  #The method split creates a list from the string
  
  for word in list_of_words:

    if word.isdigit():
      word = int(word)

    if word in string_dict:
      string_dict[word] += 1
      #For the words in the dictionary a value of +1 will be applied
    else:
      string_dict[word] = 1
  
  return string_dict

print words(any_word)
print words(ninah)