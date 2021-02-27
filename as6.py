print('QUESTION 1)')
givenlist =[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened_list = []
def flatten_list(givenlist):
    for element in givenlist:
        if type(element) == list:
            flatten_list(element)
        else:
            flattened_list.append(element)
flatten_list(givenlist)
print(flattened_list)
print('QUESTION 2)')
R= int(input("ENTER THE NO. OF ROWS: "))
C= int(input("ENTER THE NO. OF COLUMNS: "))
a=[]
b= []
for i in range(1,R+1):
    for j in range(1,C+1):
        x= input("ENTER ELEMENT AT ROW %d "%i+"COLUMN %d "%j)
        b.append(x)
    a.append(b)
    b=[]
print("NESTED LIST:",a)
for i in a:
    print(" ".join(i))
print('QUESTION 3)')
def repbuster(x):
    return list(set(x))
list1= [3, 7, 13, 9, 7, 5, 13, 17, 23, 17, 7, 29]
list2= ["A", "E", "E", "O", "A"]
print('THE LISTS WITHOUT REPETATIONS ARE:' ,repbuster(list1),',',repbuster(list2))
print('QUESTION 4)')
randomtext = input('ENTER SOME TEXT:')
output = ''
i = 0
while i < len(randomtext):
        if i + 1 < len(randomtext):
                output = output + randomtext[i + 1]
                output = output + randomtext[i]
        i = i + 2
print ('GIVEN TEXT:' + randomtext)
print ('THE ODD EVEN INTERCHANGED TEXT IS:' + output)
print('QUESTION 5)')
import re
i=0
stringin=input(str('ENTER THE STRING INPUT:'))
for i in range(20):
    stringout = re.sub(r"\([^()]*\)","", stringin)
    stringout = re.sub(r"\([^()]*\)","", stringout)
    i=i+1
print('THE TEXT WITHOUT CHARACTERS IN PARENTHESES IS:',stringout)
print('QUESTION 6)')
rangex=int(input('ENTER THE RANGE OF THE NUMBERS (N):'))
even,odd= [],[]
for i in range(rangex):
    inpdig=int(input('ENTER THE NUMBER:'))
    if inpdig%2==0:
        even.append(inpdig)
    else:
        odd.append(inpdig)
print('THE NUMBER OF ODD NUMBERS ARE:', len(odd))
print('THE NUMBER OF EVEN NUMBERS ARE:', len(even))
print('QUESTION 7)')
rangex=int(input('ENTER THE NUMBER OF TERMS UPTO WHICH YOU WANT SUMMATION:'))
n = 3
variablefactor = n
sum = 0
for i in range(rangex):
   sum += variablefactor
   variablefactor = variablefactor * 10 + n
print(sum)

    
