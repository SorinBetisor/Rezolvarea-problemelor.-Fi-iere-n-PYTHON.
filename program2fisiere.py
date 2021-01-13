#2)	Se dau două numere.
#  Să se înmulţească cel mai mare cu doi şi cel 
# mai mic cu trei şi să se afişeze rezultatele. Exemplu :
#  date de intrare
#  « numere.txt »: 3  7 
#  date de ieşire « produs.txt »: 9  14
with open('numere.txt','r') as f:
    a=f.readline(
    )
    b=f.readline()
if int(a)>int(b):
    d1=int(a)*2
    d2=int(b)*3
else:
    d1=int(b)*2
    d2=int(a)*3
with open('produs.txt','w') as h:
    h.write(str(d1))
    h.write(
    "\n"
    )
    h.write(str(d2))