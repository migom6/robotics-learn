def takeApprox(matrix):
  m = []
  for i in matrix:
    ar = []
    for j in i:
      j = float("{0:.0f}".format(j))
      ar.append(int(j))
    m.append(ar)
  return m
