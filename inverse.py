from rotation import *
from getangle import *
from transpose import *
from multiply import *
from isOrthogonal import *

def negative(M):
  N = []
  for i in M:
    row = []
    for j in i:
      row.append(-j)
    N.append(row)
  return N

def inverse(M):
  if(len(M) is not 4 or len(M[0]) is not 4):
    raise ValueError('Matrix not 4X4')
  
  MI = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
  # extract rotational matrix
  R = [[0,0,0],
       [0,0,0],
       [0,0,0]]
  for i in range(3):
    for j in range(3):
      R[i][j] = M[i][j]

  # extract translation matrix
  P = [[M[0][3]],
       [M[1][3]],
       [M[2][3]]]
  
  #calc inverse of the rotation
  RI = transpose(M)

  #negative RI
  P = negative(P)

  #calc positional component 
  PI = multiply(RI,P)
  
  # putting values of R-transpose in new matrix
  for idx, i in enumerate(RI):
    for jdx, j in enumerate(i):
      MI[idx][jdx] = RI[idx][jdx]
  
  # putting values of -(R-transpose * P) in new matrix
  MI[0][3] = PI[0][0]
  MI[1][3] = PI[1][0]
  MI[2][3] = PI[2][0]
  MI[3][3] = 1

  return(MI)









