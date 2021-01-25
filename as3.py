#q1
#summation of nᵗʰ power

print("\033[1;31;40m -:RESPECTED SIRS AND T.A's, PLEASE RUN THE PROGRAM IN WINDOWS POWERSHELL TO SEE INTERESTING COLOURED OUTPUTS:- \n")
print("\033[1;32;40m THE SOLUTION TO THE ASSIGNMENT OF CS1101 BEGINS HERE \n")
print('\033[1;33;40m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
print('QUESTION 1) \n')
list1=[]
n1=int(input('Enter upto which number you want integers to be summed up to the nᵗʰ power:'))
n2=int(input('Enter the value of the power (n):'))
for i in range(n1+1):
    x=i**n2
    list1.append(x)
print(sum(list1))
#q1-verification
print('square-summation/cube-verification')
list1=[]
n1=int(input('Enter upto which number you want integers to be summed up to the nᵗʰ power:'))
n2=int(input('Enter the value of the power (n):'))
if n2==2:
    print('The required square sum by verified mathematical formula:', (1/6)*n1*(n1+1)*(2*n1+1))
elif n2==3:
    print('The required sum of cubes by verified mathematical formula:', (1/4)*(n1**2)*(n1+1)**2)
print("\033[1;32;40m QUESTION 2) \n")
#q2
list2=[]
a=0
b=1
r1=int(input('Enter upto which range you want your list:'))
for i in range(r1):
    list2.append(b)
    list2.append(a)
    b+=2
print('The required list is:',list2)
print("\033[1;33;40m QUESTION 3) \n")
#q3
list3=[]
def squaresum(n) : 
    ssm = 0
    for i in range(1, n+1) : 
        ssm = ssm + (i * i)       
    return ssm 
r2=int(input('Enter upto which range you want your list:'))
for i in range(r2+1):
    list3.append(squaresum(i))
print("The list of squared sums is, upto the integer you typed in, consisting upto the integer's squared sum, the following",list3)
print("\033[1;32;40m QUESTION 4) \n")
#q4
terms = int(input("Upto how many terms do you want to generate the fibonacci series? "))
n1, n2 = 1, 1
count = 0
if terms <= 0:
   print("Please enter a positive integer:")
elif terms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("The required Fibonacci sequence is:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("\033[1;33;40m QUESTION 5) \n")
#q5
import math
t=float(input('Enter a positive integer:'))
while t < 0:
    t=float(input('Invalid input,',t,'enter a positive integer:'))
else:
    print('The required square root is:',math.sqrt(t))
print("\033[1;32;40m QUESTION 6) \n")
#q6
name=input('Enter your name:')
age=input('Enter you age:')
tuple1=(name,age)
print('The required tuple is:', tuple1)
print("\033[1;33;40m QUESTION 7) \n")
#q7
list2=[]
for i in range(10):
    name=input('Enter student name:')
    age=input('Enter you age:')
    list2.append(name)
    list2.append(age)
tuple2=tuple(list2)
print('The required tuple is:',tuple2)
print("\033[1;32;40m QUESTION 8) \n")
#q8
mn=str(input('Enter your mobile number:'))
for i in range(0,10):
    if str(i) in str(mn):
        print('True,contains:',i)
    else:
        print("False, doesnt contain:",i)
print("\033[1;33;40m QUESTION 9) \n")
#q9
listx=[]
inputx=int(input('Enter range upto which roll no. is to be considered:'))
for i in range(inputx):
    inputy=input('Enter complete student id :')
    listx.append(int(inputy[4:]))
print('Total class list is',listx)
#using list comprehension
grpa=[x for x in listx if x<150]
grpb=[x for x in listx if x>=150 ]
print('Group A is',grpa)
print('Group B is',grpb)
print("\033[1;32;40m QUESTION 10) \n")
#q10
farenheit=[0,25,50,75,100]
print('My farenheit list is:', farenheit,'⁰F')
celcius=[(5/9)*(x-32) for x in farenheit]
print('The corresponding celcius list is:',celcius,'⁰C')
print("\033[1;33;40m QUESTION 11) \n")
#q11
cs1101=float(input('Enter CS1101 marks:'))
ch2201=float(input('Enter CH2201 marks:'))
cs3201=float(input('Enter CS3201 marks:'))
cs3202=float(input('Enter CS3202 marks:'))
ls2201=float(input('Enter LS2201 marks:'))
marks=(cs1101,ch2201,cs3201,cs3202,ls2201)
listz=list(marks)
listy=[]
for i in listz:
    if i<50 :
        i=i+5
        listy.append(i)
    else:
        listy.append(i)
marks=tuple(listy)
print('The new tuple after grace marks is:', marks)
print("\033[1;36;40m ======END OF ASSIGNMENT===== \n")

    
