def transpose(M):
  a = [[0,0,0],
      [0,0,0],
      [0,0,0]]
  for i in range(0,3):
    for j in range(0,3):
      a[j][i] = M[i][j]
  return a
      

