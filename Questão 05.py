x1=(float (input("inserir valor de x1:")))   #ponto p1 
y1=(float (input("inserir valor de y1:")))       
x2=(float (input("inserir valor de x2:")))   #ponto p2
y2=(float (input("inserir valor de y2:")))

d=((x2-x1)**2+(y2-y1)**2)**(1/2)      #Equação da distância de pontos bidimensionais
print(round(d,4))