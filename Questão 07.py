X=(input("inserir a quantidade de dias X"))   #idade em dias

Anos=(X/365)
R1=(X%365)

Meses=(R1/30)
R2=(R1%30)

print(int(Anos), "ano(s)")
print(int(Meses), "mes(ses)")
print(int(R2), "dia(s)")