#5)	Afişaţi tabla înmulţirii cu numărul n. 
# Exemplu: pentru n=5, se va afişa pe verticală 1x5=5
#   2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr, în fişierul 
# « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.
with open('numar.txt','r') as f:
    a=f.readline(
    )
a=int(a)
n=a
x=10
with open('inmultire.txt','w') as h:
    for i in range(x):
        h.write(str(i))
        h.write("*")
        h.write(str(a))
        h.write("=")
        h.write(str(i*a))
        h.write("\n")


