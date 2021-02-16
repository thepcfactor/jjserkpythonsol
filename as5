print('QUESTION 1:')
lowerlim = int(input("ENTER LOWER LIMIT"))  
upperlim = int(input("ENTER UPPER LIMIT"))
x=lowerlim
if lowerlim>upperlim:
    print('ENTERED REVERSE...CHANGING...')
    lowerlim=upperlim
    upperlim=x
primes=[]  
for num in range(lowerlim,upperlim + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           primes.append(num)
print('THE PRIMES ARE:', primes,'\n')  
print('QUESTION 2:')
import math
x=float(input('ENTER VALUE FOR WHICH exp VALUE IS TO BE CALCULATED:(you may enter π as per question or any value you wish):'))
tol=float(input('ENTER TOLERANCE:'))
sum,term=1,1
n=1
while term>tol:
    sum = sum+term
    term=term*(x/n)
    n=n+1
print('THE CALCULATED VALUE IS', sum, ',AND THE ACTUAL VALUE IS', math.exp(x),"AND THE DIFFEENCE IS", abs(sum-math.exp(x)),"AND THE NUMBER OF TERMS IS", n)
print('QUESTION 3:')
from math import sin,pi
tol = 10**(-4)
x= pi/2
y=0
z=x
n=0
while abs(z)>tol:
    n=n+1
    y=y+z
    z=z*(-x**2/((2*n)*((2*n)+1)))    
print("NO.OF TERMS USED:",n,"\nCOMPUTED VALUE:",y,"\nACTUAL VALUE:",sin(x),"\nABSOLUTE DIFFERENCE:",abs(y-sin(x)))
print('\n QUESTION 4:')
a="A"
b=" "
for i in range(1,11):
    print((b*(10-i))+(a*2*i))
print('\n QUESTION 5:')
print("ENTER THE SIDE LENGTHS SERIALLY:")
X = float(input('FIRST LENGTH:'))
Y = float(input('SECOND LENGTH:'))
Z = float(input('THIRD LENGTH:'))
def valid(a,b,c):
    if ((a + b > c) and (a + c > b) and (b + c > a)) :
        print("THE TRIANGLE CAN BE CONSTRUCTED")
    else :
	    return('INVALID LENGTHS FOR SIDES OF A TRIANGLE' )
valid(X,Y,Z)
print('QUESTION 6:')
from math import*
def f(x,n):
    result=0
    for i in range(1,n+1):
        result+=((-1)**(i+1))*(x**((2*i)-1))/((2*i)-1)
    return result
diff=1
x= 1/sqrt(3) #as tanh(1/root(3))=π /6 )
n=0
while diff>0.001:
    n=n+1
    diff= abs(pi-(6*f(x,n)))   
print("NO. OF TERMS:",n,"\nEXACT VALUE:",pi,"\nCOMPUTED VALUE:",6*f(x,n),"\nABSOLUTE DIFFERENCE",diff)
print('\n QUESTION 7:')
def iter(x):
    return x**(9/10)
n=0
x=iter(10)
while x>2:
    n=n+1
    print(n,"th ITERATION:",x)   
    x=iter(x)
print("NUMBER OF ITERATIONS REQUIRED:",n)
