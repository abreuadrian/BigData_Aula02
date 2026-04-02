#Atividade 01 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
num = int(input('Digite um número: '))
ant = num - 1 
pos = num + 1

print(f'\nO número é {num}, o número anterior é {ant} e o seu posterior é {pos}.')

#Atividade 02 --------------------------------------------------------------------------------------------------------------------------------------------------------------------
preco = float(input('Informe o valor do produto: '))
qnt = int(input('Informe a quantidade: '))
preco_tot = preco * qnt
desc = preco_tot * 0.1
preco_final = preco_tot - desc

print(f'\nO preço total da compra ficou em R${preco_tot}\nO valor com 10% de desconto (R${desc}) ficou em R${preco_final}')

#Atividade 03 --------------------------------------------------------------------------------------------------------------------------------------------------------------------
salario = float(input('Digite seu salário: '))
aumt = salario * 0.15
salario_tot = salario + aumt

print(f'\nSalário: R${salario:.2f}.\nBônus do mês: R${aumt:.2f}.\nSalário final: R${salario_tot:.2f}.')