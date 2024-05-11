salario = float(input('Digite o valor do salario Inicial: '))

if salario>1500 :
    reajuste = salario*1.05
    porcentagem = int(5)
elif salario>700 :
    reajuste = salario*1.1
    porcentagem = int(10)
elif salario>280 :
    reajuste=salario*1.15
    porcentagem = int(15)
else :
    reajuste=salario*1.20
    porcentagem = int(20)

aumento = reajuste-salario

print(f"O salário inicial é {salario:.2f}R$")
print(f"A porcentagem de aumento foi {porcentagem}%")
print(f"O valor do aumento foi aproximadamente {aumento:.2f}$")
print(f"O novo salário aproximado é {reajuste:.2f}R$")
