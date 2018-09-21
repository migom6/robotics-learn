def arctan(y,x):
  arg = y/x
  if(x > 0):
    return degrees(atan(arg))
  if( x < 0 and y >=0 ):
    return degrees(atan(arg) + 3.14)

  if( x < 0 and y < 0 ):
    return degrees(atan(arg) - 3.14)

  if( x == 0 and y > 0 ):
    return degrees(3.14/2)

  if( x == 0 and y < 0 ):
    return degrees(-3.14/2)
    
  if( x == 0 and y == 0 ):
    return 'undefined'

