import numpy as np
c=300000000.0
v=0.87*c
B=np.sqrt(1.0/(1-(v*v/(c*c))))
print(B)
