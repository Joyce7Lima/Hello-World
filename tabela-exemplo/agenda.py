lista = []
list(lista)
agenda = dict()
maiores18 = []
menores18 = []

print('-_' * 20)
print('            AGENDA PESSOAL')
print('_-' * 20)
print()

agenda['nome'] = str(input('Nome do contato:'))
while agenda['nome'] != '':
    agenda['idade'] = int(input('Qual a idade do contato?'))
    agenda['numero'] = int(input('Qual o número de telefone do contato?'))
    lista.append(agenda.copy())
    agenda['nome'] = str(input('Nome do contato:'))
print('-' * 40)
print(f'AGENDA PESSOAL COMPLETA')
print('-' * 40)
print()
for usuario in lista:
    print(f' Nome: {usuario["nome"]} | Idade: {usuario["idade"]} | Número: {usuario["numero"]}')
    if usuario['idade'] >= 18:
        maiores18.append(usuario.copy())
    if usuario['idade'] < 18:
       menores18.append(usuario.copy())
print('-' * 40)
print(f'AGENDA DE CONTATOS MAIORES DE 18 ANOS')
print('-' * 40)
print()

for usuario in maiores18:
    print(f' Nome: {usuario["nome"]} | Idade: {usuario["idade"]} | Número: {usuario["numero"]}')
print('-' * 40)
print(f'AGENDA DE CONTATOS MENORES DE 18 ANOS')
print('-' * 40)
print()

for usuario in menores18:
    print(f' Nome: {usuario["nome"]} | Idade: {usuario["idade"]} | Número: {usuario["numero"]}')

