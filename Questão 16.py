valores=(input("digitar os três valores separados por vírgula:"))  

C=float(valores[0])
P=float(valores[1])
F=float(valores[2])

if (P/C)<=F:
    print("S")
else:
    print("N")