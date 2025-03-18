# Create an array and print it.
import numpy as np

# array = np.array([10, 20, 30, 40, 50])
# print("1D Array:", array)

# y = np.array([[1,2],[3,4],[5,6]])
# print("2D Array:", y)

# z = np.zeros([2,3])
# print("Zeros Array:", z)

# o = np.ones([2,2])
# print("Ones Array:", o)

# e = np.eye((2,2))
# print("Identity Matrix:", e)


# Take two matrix as input and add it as a result using numpy with exception handlig.
try:
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    c = a + b
    print("Addition of two matrix is:", c)
except ValueError:
    print("Matrix Addition not possible")
    print("Matrix dimensions should be: ")
    print("Provided matrices are:", a, b)
    print("Their dimensions are:", a.shape, b.shape)
except Exception as e:
    print("error occurred:", str(e))
    print("The provided matrices are:", a, b)
finally:
    print("Program executed successfully")
    print("Matrix dimensions are:", a.shape, b.shape)
    print("Provided matrices are:", a, b)
    print("Addition of two matrix is:", c)
    print("Program executed successfully")

    # matrix multiplication 
    