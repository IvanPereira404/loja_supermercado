from produtos import *
from crudclientes import *

def menu_principal():
    print("Menu:")
    print("1. Clientes")
    print("2. Fornecedores")
    print("3. Funcionários")
    print("4. Produtos")
    print("5. Categorias")
    print("6. Vendas")

    escolha = input("Escolha uma opção(1-6): ")

    if escolha == '1':
        menu_opc_1()
    elif escolha == '2':
        menu_opc_2()
    elif escolha == '3':
        menu_opc_3()
    elif escolha == '4':
        menu_opc_4()
    elif escolha == '5':
        menu_opc_5()
    elif escolha == '6':
        menu_opc_6()


def menu_opc_4():
    print("Menu Produtos:")
    print("1. Criar/Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Procurar/Encontrar Produto")
    print("4. Atualizar Produto")
    print("5. Apagar Produto")
    print("6. Sair")

    while True:
        escolha = input("Escolha uma opção(1-6): ")
        
        if escolha == '1':
            criar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            encontrar_produto()
        elif escolha == '4':
            atualizar_produto()
        elif escolha == '5':
            apagar_produto()
        elif escolha == '6':
            print("Saindo...")
            menu_principal()
        else:
            print("Opção inválida! Tente novamente.")


def menu_opc_1():
    print("Menu Clientes:")
    print("1. Criar/Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Atualizar Cliente")
    print("4. Sair")

    while True:
        escolha = input("Escolha uma opção(1-4): ")
        
        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            data_cadastro = input("Data de Cadastro (YYYY-MM-DD): ")
            create_cliente(nome, telefone, email, endereco, data_cadastro)
        elif escolha == '2':
            read_clientes()
        elif escolha == '3':
            id_cliente = int(input("ID do Cliente a atualizar: "))
            nome = input("Novo Nome (deixe em branco para não alterar): ") or None
            telefone = input("Novo Telefone (deixe em branco para não alterar): ") or None
            email = input("Novo Email (deixe em branco para não alterar): ") or None
            endereco = input("Novo Endereço (deixe em branco para não alterar): ") or None
            data_cadastro = input("Nova Data de Cadastro (YYYY-MM-DD) (deixe em branco para não alterar): ") or None
            update_cliente(id_cliente, nome, telefone, email, endereco, data_cadastro)
        elif escolha == '4':
            print("Saindo...")
            menu_principal()
        else:
            print("Opção inválida! Tente novamente.")

while True:
    menu_principal()
