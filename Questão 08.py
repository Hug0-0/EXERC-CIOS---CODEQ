a=round(float(input("inserir valor de a")),1)
b=round(float(input("inserir valor de b")),1)
c=round(float(input("inserir valor de c")),1)

delta=b**2-4*a*c
R1=(-(delta**0.5)-b)/(2*a)
R2=((delta**0.5)-b)/(2*a)
if delta < 0:
    print("Impossível calcular")
elif a == 0:   #comparação exige duas igualdades
    print("Impossível calcular")
else:          #condições restantes
    print("R1 =",round(R1,5))
    print("R2 =",round(R2,5))
   