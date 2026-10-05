salario = float(input("Digite o salario:"))

if salario >=3000:
    bonus = salario *0.10
if salario >= 2000:
    bonus = salario *0.05
else:
    bonus = salario *0.02
salario_final = bonus+salario
print ("salario final", salario_final)