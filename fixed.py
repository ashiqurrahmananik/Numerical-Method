import math
def f(x):
	return math.exp(-x)
def main():
	print"Enter xi:"
	xi=input()
	print"Enter ite:"
	ite=input()
	while(ite>0):
		r=f(xi)
		err=math.fabs((r-xi)/r)*100
		print "%.5f"%r,"  ","%.2f"%err
		xi=r
		ite=ite-1
if __name__=="__main__":
	main()
