#%%
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("=====CALCULATOR=====""\n1.Addition""\n2.Subtraction""\n3.Multiplication""\n4.Division""\nAnyother no. to exit")
choice= int(input("ENTER your choice: " ))
while 0<choice<5:
    num_1= float(input("ENTER a no.: "))
    num_2= float(input("ENTER another no.: "))
    if choice==1:
        print(add(num_1,num_2))
    elif choice==2:
        print(sub(num_1,num_2))
    elif choice==3:
        print(mul(num_1,num_2))
    elif choice==4:
        print(div(num_1,num_2))
    choice= float(input("ENTER your choice: "))
if choice!=1 or 2 or 3 or 4:
    print("Exiting...")        
#%%   
def f(a,b):
    a=a.split(" ")
    b=b.split(" ")
    c= int(a[0])-int(b[0])
    d= int(a[1])-int(b[1])
    dist= ((d*2)+(c*2))*0.5
    return(round(dist,2))       
x= input("ENTER 1st point: ")  
y= input("ENTER 2nd point: ")
print(f(x,y))
#%%
import sys
def f(a):
    a=a.split(" ")
    if len(a)>3:
        print("error")
        sys.exit()
    b= (int(a[0])*2)+(int(a[2])*1)
    return(b)
a= input("ENTER THE no. of wins,loose,draw(space separated): ")
print("THE point of THE team is: ",f(a))
#%%
import sys
def f(a):
    a=list(a)
    r=[]     
    for i in a:  
        if i=='T':
            r.append('U')
        elif i=='G':
            r.append(i)
        elif i=='A':
            r.append(i)
        elif i=='C':
            r.append(i)
        else:
            print("INVALID SEQUENCE")
            sys.exit()
    r= "".join(r)
    return(r)                         
d = input("ENTER THE DNA SEQUENCE:\n")
print("THE RNA SEQUENCE is: \n"+f(d))
#%%
def f(a):
    a=list(a)
    A=0
    T=0
    G=0
    C=0
    for i in a:
        if i=='A':
            A+=1
        elif i=='T':
            T+=1    
        elif i=='G':
            G+=1
        elif i=='C':
            C+=1
        else:
            print("INVALID SEQUENCE")
            sys.exit()  
    print("A:",A,"\nT:",T,"\nG:",G,"\nC:",C)
seq= input("ENTER THE DNA SEQUENCE: \n")
f(seq)
#%%
a= input("ENTER: ")
b= a.split(" ")
for i in range(0,len(b)):
    j=i+1
    while j<len(b):
        if b[i] == b[j]:  #duplicate 
            del b[j]
        j= j+1
b.sort()
print(" ".join(b))
#%%
lst= [2,6,'a','b','s',45,'x']
d= {2:1,'q':'c','x':67}
for i in d:
    for j in lst:
        if j==i:
            print(d[i])





    
