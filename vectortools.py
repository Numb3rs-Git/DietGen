from math import sqrt


def dotproduct(a, b):
  if len(a) != len(b):
    return None
  else:
    s = 0
    for i in range(len(a)):
      s += a[i] * b[i]
    return s


def magnitude(vect):
  return sqrt(dotproduct(vect, vect))


def cosine(a, b):
  return dotproduct(a, b) / (magnitude(a) * magnitude(b))
  

def scale(vect, k):
  newVect = []
  for i in vect:
    newVect.append(i / float(k))
    
    
def addVectors(a, b):
  if len(a) != len(b):
    return None
  else:
    newVect = []
    for i in range(len(a)):
      newVect.append(a[i] + b[i])
      
def vectorSum(vectors):
  vect = []
  for i in range(len(vectors[0])):
    s = 0
    for j in range(len(vectors)):
      s += vectors[j][i]
    vect.append(s)
  return vect