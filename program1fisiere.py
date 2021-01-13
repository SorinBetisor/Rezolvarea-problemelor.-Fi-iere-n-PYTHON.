#1)	Din fişierul « numere.txt » se citesc două numere.
#  Afişaţi în fişierul « minim.txt » numărul cel mai mic. 
# Exemplu : Date de intrare : 44   32   Date de ieşire : 32.
with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    c=int(b)
else:
    c=int(a)
with open('minim.txt','w') as h:
    h.write(str(c))