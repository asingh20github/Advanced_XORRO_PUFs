
import numpy as np
import sklearn
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
# You are allowed to import any submodules of sklearn as well e.g. sklearn.svm etc
# You are not allowed to use other libraries such as scipy, keras, tensorflow etc

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py
# DO NOT INCLUDE OTHER PACKAGES LIKE SCIPY, KERAS ETC IN YOUR CODE
# THE USE OF ANY MACHINE LEARNING LIBRARIES OTHER THAN SKLEARN WILL RESULT IN A STRAIGHT ZERO

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_predict etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( Z_train ):
################################
#  Non Editable Region Ending  #
################################
	data=Z_train
	data=data.astype(int)
	a=data[:,64:68]
	b=data[:,68:72]
	x=data[:,0:64]
	y=data[:,72]
	z = np.zeros(y.shape[0])
	a[:,0]=a[:,0]*8+a[:,1]*4+a[:,2]*2+a[:,3]*1
	b[:,0]=b[:,0]*8+b[:,1]*4+b[:,2]*2+b[:,3]*1
	lst=[]
	for i in range(0,16):
		temp=[]
		lst.append(temp)
		for j in range(0,16):
			help=[]
			lst[i].append(help)
	for i in range(y.size):
		if(a[i,0]>b[i,0]):
			c=a[i,0]
			a[i,0]=b[i,0]
			b[i,0]=c
			z[i] = 1-y[i]
		else:
			z[i]=  y[i]
		lst[a[i,0]][b[i,0]].append(i)
	model = [[LinearSVC(C=0.1) for k in range(16)] for k in range(16)]
	for j in range(16):
		for i in range(16):
			if(len(lst[i][j][:])!=0):
				d=[]
				o=[]
				k=lst[i][j][:]
				d = [[0 for j in range(64)] for i in range(len(k))]
				o =  [0] * len(k)
				for l in range(len(k)):
					d[l][:]=(x[k[l],:])
					o[l]=z[k[l]]
				model[i][j].fit(d,o)
				d.clear()
				o.clear()						 	 				

	# Use this method to train your model using training CRPs
	# The first 64 columns contain the config bits
	# The next 4 columns contain the select bits for the first mux
	# The next 4 columns contain the select bits for the second mux
	# The first 64 + 4 + 4 = 72 columns constitute the challenge
	# The last column contains the response
	
	return model					# Return the trained model


################################
# Non Editable Region Starting #
################################
def my_predict( X_tst,model ):
################################
#  Non Editable Region Ending  #
################################
	data=X_tst
	data=data.astype(int)
	pred=[None]*data.shape[0]
	a=data[:,64:68]
	b=data[:,68:72]
	x=data[:,0:64]
	g=[]
	a[:,0]=a[:,0]*8+a[:,1]*4+a[:,2]*2+a[:,3]*1
	b[:,0]=b[:,0]*8+b[:,1]*4+b[:,2]*2+b[:,3]*1
	lst=[]
	for i in range(16):
		temp1=[]
		lst.append(temp1)
		for j in range(16):
			help1=[]
			lst[i].append(help1)
	for i in range(data.shape[0]):
		if(a[i,0]>b[i,0]):
			c=a[i,0]
			a[i,0]=b[i,0]
			b[i,0]=c
			g.append(i)
		lst[a[i,0]][b[i,0]].append(i)
	for j in range(16):
		for i in range(16):
			if(len(lst[i][j][:])!=0):
				d=[]
				k=lst[i][j][:]
				d = [[0 for j in range(64)] for i in range(len(k))]
				for l in range(len(k)):
					d[l][:]=(x[k[l],:])
					#o[l]=y[k[l]]
				p=model[i][j].predict(d)	
				for z in range(len(k)):
					pred[k[z]]=p[z]
					d.clear()						 	 		
					
	for i in range(len(g)):
			pred[g[i]]=1-pred[g[i]]

	

	# # Use this method to make predictions on test challenges
	pred=np.array(pred)
	return pred

