from multiply import *
from takeApprox import *

def isOrthogonal(M , MI):
  k = multiply(M , MI)
  I = takeApprox(k)
  print(I)
  for i in range(4):
    for j in range(4):
      if(i == j):
        if(I[i][j] is not 1):
          # print("yo")
          return False
      if(i is not j):
        if(I[i][j] is not 0):
          print(i,j,0)
          return False
  
  return True
