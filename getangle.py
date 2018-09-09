import math

def checkaxis(M):
  if(M[0][2] == 0 and M[1][2] == 0 and M[2][2] == 1 and M[2][0] == 0 and M[2][1] == 0):
    return 'z'
  if(M[0][1] == 0 and M[1][0] == 0 and M[1][1] == 1 and M[1][2] == 0 and M[2][1] == 0):
    return 'y'
  if(M[0][0] == 1 and M[0][1] == 0 and M[0][2] == 0 and M[1][0] == 0 and M[2][0] == 0):
    return 'x'
  else: return False


def getangle(M):
  if(len(M) is not 3 or len(M[0]) is not 3):
    raise ValueError('Matrix not 3X3')
  axis = checkaxis(M)
  if(not axis): return False
  angle = 0 
  if(axis == 'x'):
    angle = math.degrees(math.acos(M[1][1]))
  if(axis == 'y'):
    angle = math.degrees(math.acos(M[0][0]))
  if(axis == 'z'):
    angle = math.degrees(math.acos(M[0][0]))
  return float("{0:.2f}".format(angle)) , axis

