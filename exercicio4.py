#Nicolas Andrade de Freitas - Turma 2190
#Exercicio 4 

premio = float(input("Digite o valor do premio:"))

desconto = premio*(7/100)
premiofinal = premio-desconto

p1 = premiofinal-(premiofinal*(46/100))
p2 = (premiofinal)*(32/100)
p3 = premiofinal-(p1+p2)

print("O valor total do premio foi de: R${}".format(premio))
print("O valor do premio com impostos é de: R${:.2f}".format(premiofinal))
print("O valor final do premio foi de: R${:.2f}".format(desconto))
print("O primeiro ganhador ganhou: R${:.2f}".format(p1))
print("O segundo ganhador ganhou: R${:.2f}".format(p2))
print("O terceiro ganhador ganhou: R${:.2f}".format(p3))