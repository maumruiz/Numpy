import numpy as np

x = np.array([1.0,2.,3.1])
print x

print "x[2] = " + str(x[2])

y = np.array([-1.0,-2.,2.9])
print "x = " + str(x) + " -- y = " + str(y)
print "x + y = " + str(x + y)

# Numpy range
a = np.arange(15)
print ("a = np.arange(15) = " + str(a))

b = np.arange(10,30,5)
print ("b = np.arange(10,30,5) = " + str(b))

print "a.shape = " + str(a.shape)
print "a.ndim = " + str(a.ndim)
print "a.dtype.name = " + str(a.dtype.name)
print "a.itemsize = " + str(a.itemsize)
print "a.size = " + str(a.size)
print "type(a) = " + str(type(a))

