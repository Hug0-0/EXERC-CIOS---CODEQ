
A=round(float(input("Digite valor A: ")),1)  #Notas com uma casa após a vírgula
B=round(float(input("Digite valor B: ")),1)  #onde A, B e C são notas de 0 a 10 para os valores de entrada
C=round(float(input("Digite valor C: ")),1)

def mediapond(A,B,C):               #definindo a média ponderada como função
    return ((2*A+3*B+5*C)/(2+3+5))  #fórmula da média ponderada

print ("MÉDIA =",round(mediapond(A,B,C),1))  