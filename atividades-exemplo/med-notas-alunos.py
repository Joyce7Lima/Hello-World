total = int(input('Qual o total de alunos? '))

alunos = {}

for i in range(1, total + 1):
    nome = input(f'Nome do aluno {i}: ')
    notas = []

    for j in range(1, 5):
        nota = float(input(f'Nota {j} do aluno {i}: '))
        notas.append(nota)

    alunos[nome] = notas

print('')
print('Notas dos Alunos')
print('-' * 40)

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    resultado = 'Aprovado' if media >= 7.0 else 'Reprovado'
    print(f'{nome} | {notas} | {resultado}', end="")
    print('')
