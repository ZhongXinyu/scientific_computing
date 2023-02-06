import numpy as np

Lmatrix = np.array([[1/np.sqrt(2),1/np.sqrt(3),1/np.sqrt(6)],[1/np.sqrt(2),-1/np.sqrt(3),-1/np.sqrt(6)],[0,1/np.sqrt(3),-2/np.sqrt(6)]])
Imatrix = np.array([[1,0,0],[0,2,0],[0,0,3]])
print (np.dot(Lmatrix,np.dot(Imatrix,Lmatrix.transpose())))
Lmatrix2 = np.array([[1/2,0,np.sqrt(3)/2],[0,1,0],[-np.sqrt(3)/2,0,1/2]])
