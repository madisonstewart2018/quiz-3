import math
#normalize takes half of the infinity norm and mulitplies it by the origninal vector.
def normalize(vector):
  '''
  This function takes a vector as its argument and finds its infinity norm. It is then divided into one and multiplied by the origninal vector.
  '''
  new = [] #this is used as the new brackets for the answer.
  max_vector = vector[0] #equal to the vector in the first position.
  for i in vector:
    if abs(i) > max_vector: #finds the biggest value in vector.
      max_vector = abs(i)
  for j in range(len(vector)): #multilpying the scalar found above by the vector.
    total = 0 #after the for statement so it resets.
    total += vector[j] * (1 / max_vector)
    new.append(total) #adds the total found above to the bracket 'new'
  return new

#test
vector01 = [1, 2, 3, 4]
vector02 = 10
print(normalize(vector01))
#print(normalize(vector02))
