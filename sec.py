import math
def f(x):
	return-2*x**6-1.5*x**4+10*x+2
def main():
	print "Enter xi:"
	a=input()
	print "Enter xi-1"
	b=input()
	print "ite:"
	ite=input()
	while(ite>0):
		h=a-(f(a)*(a-b))/float(f(a)-f(b))
		err=math.fabs((h-a)/h)*100
		print "%.5f"%h,"  ","%.2f"%err
		b=a
		a=h
		ite=ite-1

if __name__=="__main__":
	main()
