A=round(float(input("Digite valor A: ")),2) #Valores de A, B e C a definir
B=round(float(input("Digite valor B: ")),2)
C=round(float(input("Digite valor C: ")),2)

def tri(A,C):     #cálculos das áreas
    return ((A*C)/2)
pi=3.14159
def cir(C):
    return (pi*(C**2))
def tra(A,B,C):
    return (((B+A)*C)/2)
def qua(B):
    return (B**2)
def ret(A,B):
    return (B*A)

print ("Área do triângulo =",round(tri(A,C),2))   #print dos resultados
print ("Área do círculo =",round(cir(C),2))
print ("Área do trapézio =",round(tra(A,B,C),2))
print ("Área do quadrado =",round(qua(B),2))
print ("Área do retângulo =",round(ret(A,B),2))