#dot takes two vectors and multiplies them together and then adds the two products to give an integer
def dot(vector01, vector02):
  '''
  This function brings together to vectors and returns the dot product of the two by taking the range of the first vector as the range of both and then mulitplying the two vectors beofre adding the two products together. If the vectors are not valid lists than the code prints 'invalid input'.
  '''
  if len(vector01) != len(vector02): #if length of the first vector does not equal the length of the second, it is not a valid input. Therefore returns 'invalid input'
    print('invalid input')
    return None
  total = 0 #used before the for statement so it does not reset and therefore uses the first amount and adds to the next to get the integer.
  for i in range(len(vector01)): #i in range(2) so from 0 to 1
    total += vector01[i] * vector02[i] #multiplies the two vector elements from the range and then adds the two products together.
  return total

#testing elements
vector01 = [1, 2, 3]
vector02 = [1, 2, 3]
vector03 = [1, 2, 3]
vector04 = [1, 2]
print(dot(vector01, vector02))
#print(dot(vector03, vector04))
