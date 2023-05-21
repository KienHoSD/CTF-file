import numpy as np 
v = [2,6,3]
w = [1,0,0]
u = [7,7,2]
vectorv=np.array(v)
vectorw=np.array(w)
vectoru=np.array(u)
result1 = 3*(2*vectorv-vectorw)
result2 = 2*vectoru
result= result1.dot(result2)
print(result)