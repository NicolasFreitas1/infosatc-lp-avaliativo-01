#Nicolas Andrade de Freitas - Turma 2190
#Exercicio 3

altura = float(input("Digite a altura da parede: "))
comprimento= float(input("Digite o comprimento da parede: "))

area = altura*comprimento

tintatotal= area*(1/3)

precototal = (tintatotal/3.6)*107

print("A quantidade de litros de tinta necessarios é de: {:.2f}L".format(tintatotal))
print("O valor final será de: R${:.2f}".format(precototal))