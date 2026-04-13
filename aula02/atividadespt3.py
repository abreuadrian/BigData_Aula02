#Atividade3:
list_nota = []
for i in range (4):
    nota = float(input(f'Informe a nota da {i+1}ª avaliação: '))
    list_nota.append(nota)
med = sum(list_nota) / len(list_nota)
print(f'\nA média do aluno foi: {med:.1f}')

# nota1 = float(input('Informe a nota da AV1: '))
# nota2 = float(input('Informe a nota da AV2: '))
# nota3 = float(input('Informe a nota da AV3: '))
# nota4 = float(input('Informe a nota da AV4: '))

# med_final = (nota1 + nota2 + nota3 + nota4) / 4
# print(f'A média do aluno foi: {med_final:.1f}')