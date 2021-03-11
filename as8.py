#Question 1

RNA=input('Enter the RNA sequence:')
print('Codons are:',end='')
for i in range(0,len(RNA),3):
    print(RNA[i:i+3],end=' ')
print()

#Question 2

sgc={'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'STOP','UAG':'STOP','UGU':'C','UGC':'C','UGA':'STOP','UGG':'W','CUU':'L','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
RNA=input('Enter RNA sequence for knowing the amino acid syn from it:')
peptide=''
for i in range(0,len(RNA),3):
    codon=RNA[i:i+3]
    if sgc[codon]=='STOP':
        break
    else:
        peptide+=sgc[codon]
print(peptide)
        

#Question 3

import math
r=eval(input('Enter the radius:'))
vol=4/3*math.pi*r**3
print('1st decimal place: %.1f'%(vol))
print('2nd decimal place: %.2f'%(vol))
print('3rd decimal place: %.3f'%(vol))
print('4th decimal place: %.4f'%(vol))

#Question 4

n=eval(input('Enter a NUMBER:'))
try:
    print('Square root=%.3f'%(n**0.5))
except:
    print('NUMBER is negative. Square root doesnt exist in real domain.')
