# Name : MOHAMMAD HAMZAH AKHTAR
# Roll Number : 2018051	
# Section : A
# Group : 3
from matplotlib import pyplot as plt
from math import *
from matplotlib import patches

def scaling(x,y,s_parameter):
	scale_matrix = [] ; final_x = [] ; final_y = [] ; coordinates = [] ; co_ord =0
	for i in range(2):
		list = []
		if i==0:
			list.append(int(s_parameter[i]))
			list.append(0)
		else :
			list.append(0)
			list.append(int(s_parameter[i]))
		scale_matrix.append(list)
	length = len(x)
	for i in range(length):
		matrix = [] ; temp_coord = []
		matrix.append(x[i]) ; matrix.append(y[i])
		for j in scale_matrix :
			co_ord=0
			for k in range(2):
				co_ord = co_ord + (j[k]*matrix[k])
			temp_coord.append(co_ord)
		coordinates.append(temp_coord)
	for i in range(len(coordinates)):
		final_x.append(coordinates[i][0]) ; final_y.append(coordinates[i][1])
	return final_x,final_y

def rotation(x,y,theta): 
	theta=radians(int(theta))
	rotation_matrix = [] ; final_x = [] ; final_y = [] ; coordinates = [] ; co_ord =0
	for i in range(2):
		list = []
		if i == 0:
			list.append(cos(theta))
			list.append(-sin(theta))
		else :
			list.append(sin(theta))
			list.append(cos(theta))
		rotation_matrix.append(list)
	length = len(x)
	for i in range(length):
		matrix = [] ; temp_coord = []
		matrix.append(x[i]) ; matrix.append(y[i])
		for j in rotation_matrix :
			co_ord = 0
			for k in range(2):
				co_ord = co_ord + (j[k]*matrix[k])
			temp_coord.append(co_ord)
		coordinates.append(temp_coord)
	for i in range(len(coordinates)):
		final_x.append(coordinates[i][0]) ; final_y.append(coordinates[i][1])
	return final_x,final_y

def translation(x,y,t_parameter):
	final_x = [] ; final_y = [] ; translate_matrix=[] ; coordinates =[]
	for i in range(3):
		matrix=[]
		if i==0:
			matrix.append(1);matrix.append(0);matrix.append(int(t_parameter[0]))
		elif i==1:
			matrix.append(0);matrix.append(1);matrix.append(int(t_parameter[1]))
		elif i==2:
			matrix.append(0);matrix.append(0);matrix.append(1)
		translate_matrix.append(matrix)
	for i in range(len(x)):
		matrix = [] ; temp_coord = []
		matrix.append(x[i]) ; matrix.append(y[i]) ; matrix.append(1)
		for j in translate_matrix :
			co_ord = 0
			for k in range(3):
				co_ord = co_ord + (j[k]*matrix[k])
			temp_coord.append(co_ord)
		coordinates.append(temp_coord)
	for i in range(len(coordinates)):
		final_x.append(coordinates[i][0]) ; final_y.append(coordinates[i][1])
	return final_x,final_y

def ellipse_rotation(X,Y,theta):
	final_x,final_y=rotation(X,Y,theta)
	x=(final_x[0]+final_x[500])/2 ; y=(final_y[250]+final_y[750])/2
	a=abs(final_x[0]-x) ; b=abs(final_y[250]-y)
	return x,y,a,b,final_x,final_y

def ellipse_translation(X,Y,t_parameter):
	final_x,final_y = translation(X,Y,t_parameter)
	x=(final_x[0]+final_x[500])/2 ; y=(final_y[250]+final_y[750])/2
	a=abs(final_x[0]-x) ; b=abs(final_y[250]-y)
	return x,y,a,b,final_x,final_y

def e_plot(x,y,a,b):
	X=[] ; Y=[]
	for i in range(1000):
		theta=(2*pi*i)/1000
		x1=x+(a*cos(theta))
		y1=y+(b*sin(theta))
		X.append(x1);Y.append(y1)
	return X,Y

def ellipse_scaling(X,Y,s_parameter):
	final_x,final_y = scaling(X,Y,s_parameter)
	x=(final_x[0]+final_x[500])/2 ; y=(final_y[250]+final_y[750])/2
	a=abs(final_x[0]-x) ; b=abs(final_y[250]-y)
	return x,y,a,b,final_x,final_y

plt.ion()
figure = input()
if(figure == "polygon"):
#	Takes input two lists of equal length one having all the x-coordiantes and the other having y-coordinates
	X = list(map(int,input().split()))
	Y = list(map(int,input().split()))
	ans = [""]
	while (ans[0] != "quit"):
		ans = input()
		ans = ans.split()
		if ans[0]=='S':
			X,Y = scaling(X,Y,ans[1:])
		elif ans[0]=='R':
			X,Y = rotation(X,Y,ans[1])
		elif ans[0]=='T':
			X,Y = translation(X,Y,ans[1:])
		x=list(X) ; x.append(X[0]) 
		y=list(Y) ; y.append(Y[0])
		print(X,Y)
		plt.plot(x,y)

elif(figure == "disc"):	
#	Input in the form centre(x,y)  major-axis-length(a) minor-axis-length(b)
	disc_values = list(map(int,input().split()))
	x=disc_values[0] ; y = disc_values[1] ; a = disc_values[2] ; b = disc_values[2]
	X,Y = e_plot(x,y,a,b)
	ans = [""]
	while (ans[0] != "quit"):
		plt.plot(X,Y)
		ans = input()
		ans = ans.split()
		if ans[0]=='S':
			x,y,a,b,X,Y = ellipse_scaling(X,Y,ans[1:])
		elif ans[0]=='R':
			x,y,a,b,X,Y = ellipse_rotation(X,Y,ans[1])
		elif ans[0]=='T':
			x,y,a,b,X,Y = ellipse_translation(X,Y,ans[1:])
		print(x,y,a,b)
		
plt.show()