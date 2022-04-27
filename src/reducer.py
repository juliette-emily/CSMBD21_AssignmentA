def reduce_func(x,y):
	""" Simple sum reducer, 2 args """
	return x+y

def reduce_func_tuple(z):
	""" Simple sum reducer, 1 tuple arg """
	k,v=z
	return (k, sum(v))