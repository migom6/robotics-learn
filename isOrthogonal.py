from multiply import *

def isOrthogonal(M , MI):
  I = multiply(M, MI)
  print(I)
  for i in range(4):
    for j in range(4):
      if(i == j):
        if(I[i][j] is not 1):
          print("yo")
          return False
      if(i is not j):
        if(I[i][j] is not 0):
          print(i,j,0)
          return False
  
  return True

# m = [[1, 0, 0, -3],
# [0, 0.8660254037844387, 0.49999999999999994, -4.098076211353316],
# [0, -0.49999999999999994, 0.8660254037844387, -1.0980762113533162],
# [0, 0, 0, 1]]
# n = [[1, 0, 0, 3], [0, 0.8660254037844387, -0.49999999999999994, 3 ], [0, 0.49999999999999994, 0.8660254037844387,3],[0,0,0,1]]

# print(isOrthogonal(m, n))