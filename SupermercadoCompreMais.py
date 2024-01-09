carrinho = []
quantidades = []
valores = []

produtos = [# 1 ao 10 - Frutas e Verduras
            ["Maçã", "Tomate", "Alface", "Cenoura", "Cebola", "Uva", "Limão", "Coentro", "Banana", "Mamão",
             # 11 ao 20 - Produtos de Limpeza
             "Amaciante", "Detergente", "Desinfetante", "Sabão em pó", "Sabão em barra", "Sabão líquido", "Água sanitária", "Limpa vidros", "Multiuso", "Alvejante",
             # 21 ao 30 - Molhos
             "Molho de tomate", "Extrato de tomate", "Molho shoyo", "Molho caesar", "Molho barbacue", "Molho rosé", "Molho quatro queijos", "Molho bechamel", "Molho italiano", "Molho balsâmico",
             # 31 ao 40 - Alimentos
             "Arroz", "Feijão", "Macarrão espaguete", "Macarrão parafuso", "Farinha de trigo", "Massa para cuscuz", "Massa para tapioca", "Açúcar", "Sal", "Café", 
              # 41 ao 50 - Higiene Pessoal
             "Shampoo", "Condicionador", "Sabonete", "Pasta de dente", "Escova de dente", "Fio dental", "Desodorante", "Creme de cabelo",  "Absorvente", "Sabonete líquido",
             # 51 ao 60 - Bebidas
             "Água", "Cerveja", "Refrigerante", "Suco", "Vinho", "Whisky", "Cachaça", "Vodka", "Rum", "Espumante"],
             # Preços
             [4, 6, 2, 3, 3.50, 4.50, 4.80, 1, 5, 6.20, 10, 8, 7.50, 5.30, 2.40, 8.30, 3, 11, 5.20, 12, 7.30, 8.30, 10.40, 18, 17.50, 18.70, 20.30, 20.30, 21.80, 10.20,9, 8, 5, 5.40, 3.50, 2.30, 4.80, 10.10, 3, 9.70,29, 32, 5, 2.50, 5.40, 1.30, 20.10, 25.40, 30.30, 34.80,4, 6.80, 8, 11, 63, 100, 40, 75, 40, 80],
             # Códigos
             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]]

# Funcão para o menu inicial:
def menuInicial ():
    menu = ["1-Listar produtos", "2-Adicionar produto ao carrinho", "3-Ver carrinho", "4-Finalizar compra"]
    print("MENU INICIAL:")
    for i in menu:
        print(i)

# Função para a opcção "ver produtos":
def opcao1 ():
    menuProdutos = ["1-Frutas e Verduras", "2-Produtos de Limpeza", "3-Molhos", "4-Alimentos", "5-Higiene Pessoal", "6-Bebidas"]
    print("MENU DE PRODUTOS")
    for i in menuProdutos:
        print(i)

# Função para a opção "Adicionar produto ao carrinho":
def opcao2 ():
    precoTotal = 0
    print("ADICIONAR PRODUTO AO CARRINHO: ")
    indProdutoPreco = int(input("Digite o código do produto: "))
    quant = int(input("Quantidade do produto: "))
    if (quant <= 0):
        print("Quantidade inválida, repita a operação.")
    
    else:
        carrinho.append(produtos[0][indProdutoPreco-1])
        quantidades.append(quant)
        valores.append(quant * produtos[1][indProdutoPreco-1])

# Função para a opção "Ver carrinho":
def opcao3 ():
    if (len(carrinho) == 0):
            print("O carrinho está vazio. Vamos comprar?!")
    else:
        print("SEU CARRINHO:")
        for i in range(len(carrinho)):
            print("Produto: {} | Quantidade: {} | Valor: {:.2f}".format(carrinho[i],quantidades[i], valores[i]))

# Função para a opção "Finalizar compra"
def opcao4 ():
    precoTotal = 0

    for valor in valores:
            precoTotal += valor
    
    print("FINALIZANDO COMPRA:")
    print("O valor total da compra é: R${:.2f}".format(precoTotal))

# Funções para cada categoria de produtos da opção "Ver produtos":
def categoria1 ():
    if (categoria == 1):
        print("LISTA DE PRODUTOS:")
        for j in range (len(produtos[0][0:10])):
            print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))

def categoria2 ():
    print("LISTA DE PRODUTOS:")
    for j in range (len(produtos[0][11:21])):
        j += 10
        print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))

def categoria3 ():
    print("LISTA DE PRODUTOS:")
    for j in range (len(produtos[0][21:31])):
        j += 20
        print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))

def categoria4 ():
    print("LISTA DE PRODUTOS:")
    for j in range (len(produtos[0][31:41])):
        j += 30
        print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))

def categoria5 ():
    print("LISTA DE PRODUTOS:")
    for j in range (len(produtos[0][41:51])):
        j += 40
        print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))

def categoria6 ():
    print("LISTA DE PRODUTOS:")
    for j in range (len(produtos[0][51:61])):
        j += 50
        print("{} - {} R${:.2f}".format(produtos[2][j], produtos[0][j], produtos[1][j]))
                       
opcao = 0
while (opcao != "4"):
    menuInicial()
    opcao = input("Digite para onde você quer ir: ")

    while (opcao == "1"):
        opcao1()
        categoria = int(input("Digite a sessão que você quer ser direcionado: "))

        if (categoria == 1):
            categoria1()

        elif (categoria == 2):
            categoria2()

        elif (categoria == 3):
            categoria3()

        elif (categoria == 4):
            categoria4()

        elif (categoria == 5):
            categoria5()

        elif (categoria == 6):
            categoria6()

        else:
            print("Categoria não encontrada.")
        
        opcao = input("Deseja continuar vendo os produtos? 1 - S | 0 - N ")

    while (opcao == "2"):
        opcao2()

        opcao = input("Deseja continuar comprando? 2 - Sim | 0 - Não ")
    
    if (opcao == "3"):
        opcao3()

        print("Voltando para o menu inicial.")

    elif (opcao == "4"):
        opcao4()

        print("Obrigado e volte sempre :)")