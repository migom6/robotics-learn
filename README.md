# robotics-learn

 A library of useful fuctions required in robotics

#### Inverse a transformation matrix exploiting it's structure

```python
from inverse import *
input_matrix = [[-0.7078, 0.2855, 0.6461, 3],
                [-0.5806, 0.2858, -0.7824, 3], 
                [-0.4023, -0.9140, -0.0365, 3], 
                [0,0,0,1]]
inversed_matrix = inverse(m)
```

#### Check if a matrix is orthogonal using it's inversed matrix

```python
from isOrthogonal import *
isOrthogonal(input_matrix, inversed_matrix)
```

#### Finding angle in degrees using y-coordinate and x-coordinate

```python
from arctan import *
arctan(y, x)
```

#### Get angle in degrees from rotational matrix 3X3

```python
from getangle import *
getangle(rot_matrix)
```

#### Multiply two matrices

```python
from multiply import *
multiply(matrix_A, matrix_B)
```



## Clone this repo https://github.com/migom6/robotics-learn.git

To run assignment 1 and assignment 2 
`python test.py`

