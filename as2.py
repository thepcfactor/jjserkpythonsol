print("\033[1;31;40m -:RESPECTED SIRS AND T.A's, PLEASE RUN THE PROGRAM IN WINDOWS POWERSHELL TO SEE INTERESTING COLOURED OUTPUTS:- \n")
print("\033[1;32;40m THE SOLUTION TO THE ASSIGNMENT OF CS1101 BEGINS HERE \n")
print('\033[1;33;40m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
print('QUESTION 1) \n')
x='PRIYAM' #q1
for i in range(1,16): #q1
    print(i,')',x,'\n') #q1
print("\033[1;32;40m QUESTION 2)\n")
for i in range (1,46): #q2
    if i%3==0: #q2
        print(i,')',x) #q2
    else: #q2
        print('.') #q2
print("\033[1;33;40m QUESTION 3)\n")
y= 'abcdefghijkl' #q3
for i in range(0,12): #q3
    print (y[i:]) #q3
print("\033[1;32;40m QUESTION 4)\n") 
m=[0, 3, 1, 2, 8, 9, 0, 4, 7] #q4
n=[0, -1, -3, -4, 3, 8, 9, 11, -2] #q4
def maximum(l): #q4
    Max = l[0] #q4
    for num in l: #q4
        if Max < num: #q4
            Max = num #q4
    return Max #q4
print('HIGHEST NUMBER IN FIRST LIST IS:', maximum(m)) #q4
print('HIGHEST NUMBER IN SECOND LIST IS:', maximum(n),'\n') #q4
print("\033[1;33;40m QUESTION 5)\n")
o=[0, 3, 1, 2, 8, 9, 0, 4, 7]
p=[0, -1, -3, -4, 3, 8, 9, 11, -2]
def maximum(l): #q5
    Max = l[0] #q5
    for num in l: #q5
        if Max < num: #q5
            Max = num #q5
    return Max #q5
def minimum(l): #q5
    Min = l[0] #q5
    for num in l: #q5
        if Min > num: #q5
            Min = num #q5
        
    return Min #q5
print('HIGHEST NUMBER IN FIRST LIST IS:', maximum(o),'POSITION:', o.index(maximum(o))) #q5
print('HIGHEST NUMBER IN SECOND LIST IS:', maximum(p),'POSITION:', p.index(maximum(p)),'\n') #q5
print('LOWEST NUMBER IN FIRST LIST IS:', minimum(o),'POSITION: 0') #q5
print('LOWEST NUMBER IN SECOND LIST IS:', minimum(p),'POSITION:', p.index(minimum(p)),'\n') #q5
if max(o)==maximum(o):  #q5
    print('YES THE OUTPUTS ARE EQUAL FOR MAX OF FIRST LIST')  #q5
else:  #q5
    print('NO THEY ARE NOT EQUAL')  #q5
if max(p)==maximum(p):   #q5
    print('YES THE OUTPUTS ARE EQUAL FOR MAX OF SECOND LIST')  #q5
else:  #q5
    print('NO THEY ARE NOT EQUAL')  #q5
if min(p)==minimum(p):  #q5
    print('YES THE OUTPUTS ARE EQUAL FOR MIN OF FIRST LIST')  #q5
else:  #q5
    print('NO THEY ARE NOT EQUAL')  #q5
if min(o)==minimum(o):  #q5
    print('YES THE OUTPUTS ARE EQUAL FOR MIN OF SECOND LIST \n')  #q5
else:  #q5
    print('NO THEY ARE NOT EQUAL')  #q5
print("\033[1;32;40m QUESTION 6)\n") #q6 
name=input('ENTER YOUR NAME:') #q6
year=input('ENTER YEAR OF JOINING:') #q6
newyear=year[2:] #q6
course=input('ENTER COURSE ID:') #q6
iden=input('ENTER STUDENT ID:') #q6
email=[name,newyear,course,iden] #q6
print('YOUR IISER KOLKATA MAIL ADDRESS IS:','-'.join(email),'@iiserkol.ac.in \n' ) #q6
print("\033[1;33;40m QUESTION 7)\n")
str1= '123' #q7
str2= '234'  #q7
str3= '456'  #q7
f1=float(str1)  #q7
f2=float(str2)  #q7
f3=float(str3)  #q7
print('THE SUM OF THE NUMBERS IS:', f1+f2+f3)  #q7
print('THE PRODUCT OF THE NUMBERS IS:', f1*f2*f3)  #q7
print('THE AVERAGE OF THE NUMBERS IS:', (f1+f2+f3)/3,'\n')  #q7
print("\033[1;32;40m QUESTION 8)\n")
lst=[] #q8
for n in range(5): #q8
    numbers = int(input('ENTER THE NUMBER:')) #q8
    lst.append(numbers) #q8
print("Sum of elements in given list is :", sum(lst),'\n') #q8
print("\033[1;36;40m QUESTION 9)\n")
lst1=[]
for n in range(10): #q9
    numbers = int(input('ENTER THE MARKS RECIEVED:')) #q9
    lst1.append(numbers) #q9
lst1.sort(reverse=True)  #q9
print('THE DESCENDING LIST IS, BEFORE GRACE MARKS:', lst1)  #q9
lst1.sort(reverse=True)  #q9
for i in lst1:  #q9
    if i<45:  #q9
        i=i+5  #q9
fail=[]  #q9
for n in lst1:  #q9
    if n<50:  #q9
        fail.append(n)  #q9
print('THE NUMBER OF FAILURES IS, EVEN AFTER GRACE MARKS:',len(fail),'\n')  #q9
print("\033[1;32;40m QUESTION 10)\n")
numbers=[] #q10
for n in range(10): #q10
    numbers1 = int(input('ENTER THE NUMBER:')) #q10
    numbers.append(numbers1) #q10
print('THE SORTED LIST IS:', sorted(numbers)) #q10
y=sorted(numbers)
print('THE NEW NUMBERS ARE, WITHOUT THE PREVIOUS MAX AND MIN:', y[1:9]) #q10


        











print("\033[1;36;40m ======END OF ASSIGNMENT===== \n")
