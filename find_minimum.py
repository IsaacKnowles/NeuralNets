import sys
import random


def get_prediction(b,x):
	prediction = sum([x[i]*b[i] for i in range(len(b))])	
	return(prediction)

def get_error(b,x,y):
	if len(b) == len(x) and len(b) > 0:
		prediction = get_prediction(b,x)
		return(y - prediction)
	else:
		print('x and/or b are empty or non-conformable')



def cost_gradient(b,x,idx,y):  # generalizing the basic linear form
	inner = get_error(b,x,y)
	return( -2 * x[idx] * inner)

def cost(b,x,y):
	error = get_error(b,x,y)
	return(error**2)


if __name__ == '__main__':
	b =[1,2,3]
	x=[1,4,5]
	y = 0
	#print(get_error(b,x,y))

	y = get_prediction(b,x)

	b = [random.random()  for i in range(len(b))]
	print(y)
	#print(cost(a,b1,x1,b2,x2,y))
	#print(cost_gradient_a(a,b1,x1,b2,x2,y))
	#print(cost_gradient_b1(a,b1,x1,b2,x2,y))
	#print(cost_gradient_b2(a,b1,x1,b2,x2,y))
	#print("y is " + str(y))
	print("Start: " + ','.join([str(p) for p in b]))
	print(cost(b,x,y))
	gamma = 0.001
	for i in range(500):
		new_b = []
		for p in range(len(b)):
			#print(p)
			new_b.append(b[p] - gamma*cost_gradient(b,x,p,y))
			#print(cost(b,x,y))
		b = new_b
		#print(cost(b,x,y))
		#print(new_b)
		#print(b)
		#if i % 5 == 0: 	
			#print(b)
			#print(cost(b,x,y))	
	print("Final: " + ','.join([str(p) for p in b]))
	print(cost(b,x,y))
	

