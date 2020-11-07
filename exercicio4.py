'''
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário. 
- Criar uma função que recebe como parâmetro de entrada a lista e uma
  posição (índice) e retorna o nome que está nessa posição.
 - Essa função deve gerar e tratar uma exceção do tipo IndexError
  caso o índice não exista na lista.
'''

def buscar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print('Erro')
        raise IndexError

lista = []
for i in range(5):
    nome = input('Nome: ')
    lista.append(nome)
print(lista)

try:
    nome = buscar(lista, 10)
    print(nome)
except Exception:
    print('Erro')


