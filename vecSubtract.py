# vecSubtract subtracts the second vector from the first.
def vecSubtract(vector01, vector02):
  '''
  This function takes two vectors as its arguments and subtracts the second vector from the first vector giving a new vector from the two.
  '''
  if len(vector01) != len(vector02):
    #if the length of the two vectors don't equal each other the input is said to be invalid.
    print('invalid input')
    return None
  new = [] #since we want the answer to be in brackets instead of an integer.
  for i in range(len(vector01)):
    total = 0 #after the for i statement so it resets.
    total += vector01[i] - vector02[i]
    new.append(total) #adds the new total into the 'new' brackets
  return new

#test elements
vector01 = [5, 12]
vector02 = [-3, 4]
vector03 = [1, 1, 1]
vector04 = [1, 2]
print(vecSubtract(vector01, vector02))
#print(vecSubtract(vector03, vector04))
