from inverse import *
from isOrthogonal import *
from arctan import *

# assignment 1

m = [[-0.7078, 0.2855, 0.6461, 3],[-0.5806, 0.2858, -0.7824, 3], [-0.4023, -0.9140, -0.0365, 3], [0,0,0,1]]

n = inverse(m)

print(isOrthogonal(m,n))

#assignment 2 

# def arctan(y,x): return degrees
