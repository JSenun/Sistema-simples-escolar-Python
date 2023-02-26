import json
from random import randint


# Funções Gráficas


def cria_linha(separador, tamanho_linha=150):  # Cria linha no CMD
    print(separador * tamanho_linha)


def cria_cabecalho(string):  # Cria "cabeçalho" no CMD
    cria_linha('=')
    print(string.center(150))
    cria_linha('=')

# Funcionalidades Sistema


def le_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        data = json.load(arquivo_json)
    return data


def cadastra_notas(numero_notas):
    notas = []
    num_notas = numero_notas
    while num_notas > 0:
        materia = input('Insira a materia da nota: ')
        nota = float(input('Digite a nota a ser cadastrada: '))
        notas.append({
            "materia": f"{materia}",
            "nota": nota
        })
        cria_linha('=')
        num_notas -= 1
    return notas


def cria_aluno():
    cria_linha('=')
    id = randint(100, 550)
    nome = input('Insira o nome do aluno: ')
    sala = input('Insira a sala do aluno: ')
    materias = int(
        input('Insira a quantidade de materias que o aluno cursou: '))
    cria_linha('=')
    aluno = {
        "id": str(id),
        "nome": nome,
        "sala": sala,
        "materias": cadastra_notas(materias)
    }

    return aluno


def listar_alunos(db_alunos):
    print('')
    cria_cabecalho('LISTAGEM ALUNOS')
    for aluno in db_alunos['alunos']:
        nome_aluno = aluno['nome']
        id_aluno = aluno['id']
        sala_aluno = aluno['sala']
        print(f'ID: {id_aluno}\nNome: {nome_aluno}\nTurma: {sala_aluno}')
        cria_linha('=')
    print('')


def filtrar_alunos(db, chave_busca):
    cria_linha('=')
    print(f'Informe o/a {chave_busca} para filtrar o/a aluno/a específico/a ou informe a parcialmente pra ter um filtro mais amplo dos alunos')
    valor_filtro = input('Adicione o valor referente ao filtro: ')
    print('')
    cria_cabecalho('ALUNO(S) FILTRADO(S)')
    if len(valor_filtro) == 4:
        for aluno in db['alunos']:
            if valor_filtro == aluno[chave_busca]:
                nome_aluno = aluno['nome']
                id_aluno = aluno['id']
                sala_aluno = aluno['sala']
                print(
                    f'ID: {id_aluno}\nNome: {nome_aluno}\nTurma: {sala_aluno}')
                cria_linha('=')
    elif 4 > len(valor_filtro) > 0:
        for aluno in db['alunos']:
            if aluno[chave_busca][0:len(valor_filtro)] == valor_filtro:
                nome_aluno = aluno['nome']
                id_aluno = aluno['id']
                sala_aluno = aluno['sala']
                print(
                    f'ID: {id_aluno}\nNome: {nome_aluno}\nTurma: {sala_aluno}')
                cria_linha('=')


def organiza_sistema_filtro(db_alunos):
    finalizar_filtro = False
    cria_linha('=')
    while finalizar_filtro == False:
        decisao = input(
            'Como você deseja filtrar os alunos?\n 1 - ID\n 2 - Nome\n 3 - Turma\n 4 - Sair do Filtro \nInsira sua escolha: ')
        if decisao == '1':
            filtrar_alunos(db_alunos, 'id')
            decisao_2 = input('Continuar no filtro? s/n\n')
            if decisao_2 == 'n' or decisao_2 == 'N':
                print('\nSaindo do filtro...')
                cria_linha('=')
                print('')
                break
        elif decisao == '2':
            filtrar_alunos(db_alunos, 'nome')
            decisao_2 = input('Continuar no filtro? s/n\n')
            if decisao_2 == 'n' or decisao_2 == 'N':
                print('\nSaindo do filtro...')
                cria_linha('=')
                print('')
                break
        elif decisao == '3':
            filtrar_alunos(db_alunos, 'sala')
            decisao_2 = input('Continuar no filtro? s/n\n')
            if decisao_2 == 'n' or decisao_2 == 'N':
                print('\nSaindo do filtro...')
                cria_linha('=')
                print('')
                break
        elif decisao == '4':
            print('\nSaindo do filtro...')
            cria_linha('=')
            print('')
            break
        else:
            decisao_2 = input('\nEntrada inválida! Tentar novamente? s/n\n')
            if decisao_2 == 'n' or decisao_2 == 'N':
                break


def buscar_informacoes_aluno(db_alunos):
    print(' ')
    cria_linha('=')
    print(' ')
    aluno_id = input('Informe o ID do aluno:\n')
    print(' ')
    for aluno in db_alunos['alunos']:
        if aluno['id'] == aluno_id:
            cria_cabecalho('INFORMAÇÕES DO ALUNO')
            nome_aluno = aluno['nome']
            id_aluno = aluno['id']
            sala_aluno = aluno['sala']
            materias = aluno['materias']
            print(
                f'\nID: {id_aluno}\nNome: {nome_aluno}\nTurma: {sala_aluno}\n')
            print('Matérias:\n')
            for materia in materias:
                print(' * Matéria:', materia['materia'])
                print('   - Nota:', materia['nota'], '\n')
            break
    cria_linha('=')
    print(' ')


def atualiza_arquivo_json(nome_arquivo, dados_processados_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        new_data = json.dumps(dados_processados_arquivo)
        new_data = json.loads(new_data)
        json.dump(new_data, arquivo_json)


finalizar_programa = False

cria_cabecalho('SISTEMA BÁSICO ESCOLAR')
print('\nSeja bem-vindo/a ao sistema de cadastro e verificação de alunos!\n')
while finalizar_programa == False:
    data = le_arquivo_json('db.json')
    decisao = input(
        'O que você deseja fazer?\n 1 - Listar todos os alunos \n 2 - Filtrar aluno(a)\n 3 - Informações do aluno(a)(Necessário ID do aluno(a)) \n 4 - Cadastrar aluno(a) \n 5 - Modificar aluno(a) \n 6 - Remover aluno(a) \n 7 - Finalizar programa\nInsira sua escolha: ')
    if decisao == '1':
        listar_alunos(data)
    elif decisao == '2':
        organiza_sistema_filtro(data)
    elif decisao == '3':
        buscar_informacoes_aluno(data)
    elif decisao == '4':
        data['alunos'].append(cria_aluno())
        atualiza_arquivo_json('db.json', data)
    elif decisao == '5':
        pass
    elif decisao == '6':
        pass
    elif decisao == '7':
        cria_linha('=')
        print('Finalizando o programa...')
        cria_linha('=')
        finalizar_programa = True
    else:
        print('\nEntrada inválida! Tente novamente')
        cria_linha('=')
