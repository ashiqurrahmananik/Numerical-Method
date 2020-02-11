import math
def f(x):
	return x**3-0.165*x**2+3.993*10**-4
def main():
	print("Enter xl:")
	x=input()
	print("Enter xu:")
	y=input()
	print("ite:")
	ite=input()
	c=0
	num=1
	if(f(x)*f(y))<0:
		print("The Boundary is valid")
		while(ite>0):
			c=c+1
			z=(y*f(x)-x*f(y))/f(x)-f(y)
			if(f(x)*f(z))<0:
				y=z
			elif(f(x)*f(z))>0:
				x=z
			elif(f(x)*f(z))==0:
				print("stop Algo")
			if(c==1):
				print num," ","%.5f"%z,"	","N/A"
			if(c>=2):
				err=abs((z-old)/z)*100
				print num," ","%.5f"%z,"	","%.2f"%err,"%"
			old=z
			num=num+1
			ite=ite-1
	else:
		print "The Boundary Is not valid"
if __name__=="__main__":
	main()
