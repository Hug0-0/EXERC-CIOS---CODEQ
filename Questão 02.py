pi = 3.14159
raio=round(float(input("Digite valor raio: ")),2)  #Para o valor do raio com duas casas decimais
#float: ponto flutuante       
#round: (,2)dupla precisão
def area(raio):   #função para o cálculo da área
    return pi*(raio**2)
  
print ("A =",round(area(raio),4))   #inserir o raio a se calcular a área