import os

restaurantes = [{'nome': 'Pizza Hut', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Sushi Place', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'Burger King', 'categoria': 'Fast Food', 'ativo': False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o programa...')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu\n ')
    main()

def opcaoes_invalidas():
    print('Opção inválida!\n')
    voltar_ao_menu_principal() 


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo 
    restaurante no sistema.
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante


    Outputs:
    - Adiona um novo restaurante na lista de restaurantes
    
    
    ''' 
    exibir_subtitulo('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f' O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado ' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alterar_status_do_restaurante():
    exibir_subtitulo('Ativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi {"ativado" if restaurante["ativo"] else "desativado"} com sucesso! if restaurante["ativo"] else "desativado comn sucesso!"'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
        2
        
    voltar_ao_menu_principal()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1: 
        cadastrar_restaurante()
    elif opcao_escolhida == 2: 
        listar_restaurantes()
    elif opcao_escolhida == 3: 
        alterar_status_do_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else: 
        finalizar_app()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()