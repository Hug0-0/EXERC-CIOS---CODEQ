Bp=float(input("número de bolinhas que possui Bp:"))  #Bp = bolas que possui
G=float(input("quantidade de galhos da árvore nova G:"))  #galhos da nova árvore

if G/2==int():
    B1=(G/2)     #B1 é a quantidade de bolas necessárias na árvore nova
else:
    B1=int(G/2)

B2=B1-Bp    #B2 é a quantidade de bolas que Amélia precisa comprar
if B2>0:
    print("Falta(m)",int(B2),"bolinha(s)")
else:
    print("Amélia tem todas as bolinhas!")