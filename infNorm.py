import math
#infNorm finds the largest element in a the vector
def infNorm(vector):
  '''
  this function takes a vector as its argument and returns its largest element. It does this by taking every element in the list and compares them until the largest is found.
  '''
  max_vector = vector[0] #uses the first element in the list
  for i in vector:
    if abs(i) > max_vector: #goes through the vector until it finds the element biggest compared to vector[0]
      max_vector = abs(i) #the biggest element found in line before
  return (max_vector)

#test
vector01 = [-30, -1, 0, 1, 20]
vector02 = 10
print(infNorm(vector01))
#print(infNorm(vector02))
