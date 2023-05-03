N=float(input("Inserir um valor para o número do funcionário N"))
H=float(input("Inserir um valor para o número de horas trabalhadas H"))
V=float(round((input("Inserir um valor para o valor por hora trabalhada V")),2))

Sal=H*V    #cálculo do salário
formated_num="{:.2f}".format(Sal)  #formato da decimal com duas casas após a vírgula

print("NUMBER =",int(N))
print("SALARY = U$",(formated_num))