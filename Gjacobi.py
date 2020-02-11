import math

def jacobi(X,Y,Z,P,ite):
	itee = 0
	while (itee<ite):
		print "After ", itee+1, ":"

		xm = ((6+Y-(2*Z))/(10+0.000000))
		E1 = abs(((xm-X)/xm)*100)

		print "Root X1 = ", "%.6f"%xm
		print "Error of X1 = ", "%.2f"%E1, "%"

		ym = ((25+X+Z-(3*P))/(11+0.000000))
		E2 = abs(((ym-Y)/ym)*100)

		print "Root X2 = ", "%.6f"%ym
		print "Error of X2 = ", "%.2f"%E2, "%"

		zm = ((-11-(2*X)+Y+P)/(10+0.000000))
		E3 = abs(((zm-Z)/zm)*100)

		print "Root X3 = ", "%.6f"%zm
		print "Error of X3 = ", "%.2f"%E3, "%"

		pm = ((15-(3*Y)+Z)/(8+0.000000))
		E4 = abs(((pm-P)/pm)*100)

		print "Root X4 = ", "%.6f"%pm
		print "Error of X4 = ", "%.2f"%E4, "%"
		
		X = xm
		Y = ym
		Z = zm
		P = pm

		if ((E1>E2)&(E1>E3)&(E1>E4)):
			print "\t\t\t", "The Error is = ", "%.2f"%E1
		elif ((E2>E1)&(E2>E3)&(E2>E4)):
			print "\t\t\t", "The Error is = ", "%.2f"%E2
		elif ((E3>E1)&(E3>E2)&(E3>E4)):
			print "\t\t\t", "The Error is = ", "%.2f"%E3
		else:
			print "\t\t\t", "The Error is = ", "%.2f"%E4

		itee+=1

def main():
	p = input ("X1 = ")
	q = input ("X2 = ")
	r = input ("X3 = ")
	s = input ("X4 = ")
	ite = input ("Iteration = ")

	jacobi(p,q,r,s,ite)

if __name__ == "__main__":
	main()
