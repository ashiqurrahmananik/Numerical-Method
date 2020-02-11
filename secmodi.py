import math
def f(x):
	return math.exp(-x)-x
def main():
	print "Enter xi:"
	a=input()
	print "Enter constant:"
	d=input()
	print "ite:"
	ite=input()
	while(ite>0):
		x=a-(a*d*f(a)/f(a+d*a)-f(a))
		err=math.fabs((x-a)/x)*100
		print"%.5f"%x," ","%.2f"%err
		a=x
		ite=ite-1
if __name__=="__main__":
	main()
