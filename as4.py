import math
#question1
print('QUESTION 1:')
valuem=float(input('ENTER THE VALUE OF M:'))
x = [3,2,4,1,9,8,6,0]
def mpower(doc):
    y=[]
    for i in doc:
        k=i**valuem
        y.append(k)
    print('THE NEW LIST IS', y)
    print('THE SUM OF THE LIST IS:',sum(y))
#testing out the function
mpower(x)
#question2
print('QUESTION 2:')
def maxm(m,n):
    if m>n:
        print('THE LARGER NUMBER IS:', m)
    elif n>m:
        print('THE LARGER NUMBER IS:', n)
    else:
        print('TRICK QUESTION, BOTH ARE EQUAL ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ')
m1=float(input("ENTER A NUMBER:"))
n1=float(input('ENTER ANOTHER NUMBER:'))
#testing out
maxm(m1,n1)
#question3
print('QUESTION 3:')
k=0
def suml(i,n):
    z=[]
    for i in range(1,n+1):
        s=i/(i+1)
        z.append(s)
    print('THE REQUIRED SUM , UPTO',k,'IS', sum(z))
#testing out
i=0
for k in range(1,21):
    suml(i,k)
#question4
print('QUESTION 4:')
def facto(h):
   if h<0:
       print('INVALID INPUT')
       return('NO FACTORIAL EXISTS FOR NEGATIVE NUMBERS')
   elif h == 1:
       return h
   else:
       return h*facto(h-1)
#testing out
for i in range(1,8+1):
    print('THE FACTORIAL OF',i,'IS:',facto(i))
#question5
print('QUESTION 5:')
from math import *
def sin2theta(b):
    b=b*2
    return('THE REQUIRED SINE VALUE IS:', sin(b*pi/180))
#testing out
for q in range(91):
    print('FOR', q , "DEGREE", sin2theta(q))
#question6
print('QUESTION 6:')
import math             
def logr(x):
    return (math.log(x)) / (1+math.log(x))
num=0.1
while num <2.1  :
    print('THE REQUIRED VALUE IS',logr(num))
    num=num+0.1
#question7
print('QUESTION 7:')
print('THE REQUIRED STRONG NUMBERS LESS THAN 1000000 ARE:', end='')
for i in range(1,10**6+1):
    x=i
    y=0
    while x>0:
        y=y+factorial(int(x%10))
        x=x//10
    if i == y:
        print('\n',i, '\n')
#question 8
print('QUESTION 8:')
listinput=[]
while True:
    inputk=int(input('ENTER A NON ZERO INTEGER:'))
    if inputk == 0:
        break
    else:
        listinput.append(inputk)
print('THE LIST IS:', sorted(listinput))
print('THE AVERAGE OF THE NUMBERS IS:', sum(listinput)/len(listinput))
#question 9
print('QUESTION 9:')
listnums=[i for i in range(1,101)]
listnumsquare=[]
for i in listnums:
    listnumsquare.append(i)
    listnumsquare.append(i**2)
print('THE REQUIRED LIST IS:',listnumsquare)
#question 10
print('QUESTION 10:')
def nthfibo(n):
    fiblist=[]
    n1, n2 = 1, 1
    count = 0
    while count<n+1:
        fiblist.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print('THE REQUIRED VALUE IS:', fiblist[n-1])
x=int(input('ENTER VALUE OF n FOR nTH FIBONACCI SERIES TERM:'))
nthfibo(x)
