# scalarVecMulti takes a scalar and a vector and returns the scalar * vector product
def scalarVecMulti(scalar, vector):
  '''
  This function uses the arguments scalar and vector. It takes each element of the vector and multiplies each by the scalar, giving us a 'new' vector.
  '''
  new = [] #this will be the new vectors brackets
  for i in range(len(vector)): #for i in range(3) so from 0 to 2.
    total = 0 # total is after i, so it resets or it would reset the total to the first element and add to the second... making it [10, 30, 60] instead.
    total += vector[i] * scalar
    new.append(total) #adds the total inside of the brackets of 'new'.
  return new

scalar01 = 10
vector01 = [1, 2, 3]
scalar02 = [1, 2, 3]
vector02 = 10
scalar03 = 'it'
vector03 = 'word'

print(scalarVecMulti(scalar01, vector01))
#print(scalarVecMulti(scalar02, vector02))
#print(scalarVecMulti(scalar03, vector03))
