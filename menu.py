from CrudProdutos import *

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

while True:
    menu_principal()
