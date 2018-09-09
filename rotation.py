import math
def rotation(degrees, axis):
  radians = math.radians(degrees)
  a = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
  if(axis == 'z'):
    a[0][0] , a[0][1], a[0][2] = math.cos(radians) , -math.sin(radians) , 0 
    a[1][0] , a[1][1], a[1][2] = math.sin(radians) , math.cos(radians) , 0 
    a[2][0] , a[2][1], a[2][2] = 0 , 0 , 1 

  if(axis == 'y'):
    a[0][0] , a[0][1], a[0][2] = math.cos(radians) , 0 , math.sin(radians) 
    a[1][0] , a[1][1], a[1][2] = 0 , 1 , 0 
    a[2][0] , a[2][1], a[2][2] = -math.sin(radians) , 0 , math.cos(radians) 

  if(axis == 'x'):
    a[0][0] , a[0][1], a[0][2] = 1 , 0 , 0 
    a[1][0] , a[1][1], a[1][2] = 0 , math.cos(radians) , -math.sin(radians)
    a[2][0] , a[2][1], a[2][2] = 0 , math.sin(radians) , math.cos(radians) 

  return a 
