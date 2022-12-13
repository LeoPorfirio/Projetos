class produto():

  def __init__(self, codigo, descricao, validade, quantidade):
    self.codigo = codigo
    self.descricao = descricao
    self.validade = validade
    self.quantidade = quantidade

  def calc_lucro():
    pass


class prod_uni(produto):

  def __init__(self, custo_uni, preco_uni, codigo, descricao, validade,
               quantidade):
    super().__init__(codigo, descricao, validade, quantidade)
    self.custo_uni = float(custo_uni)
    self.preco_uni = float(preco_uni)

  def __repr__(self):
    return f'[Código = {self.codigo}, Descrição = {self.descricao}, Quantidade = {self.quantidade}, Custo = {self.custo_uni}]'

  def calc_lucro(self):
    lucro_uni = (self.preco_uni - self.custo_uni)
    print('''
O lucro deste produto é de R$''', lucro_uni, '''por unidade
    ''')


class prod_peso(produto):

  def __init__(self, custo_kg, preco_kg, codigo, descricao, validade,
               quantidade):
    super().__init__(codigo, descricao, validade, quantidade)
    self.custo_kg = float(custo_kg)
    self.preco_kg = float(preco_kg)

  def __repr__(self):
    return f'[Código = {self.codigo}, Descrição = {self.descricao}, Quantidade = {self.quantidade}, Custo = {self.custo_kg}]'

  def calc_lucro(self):
    lucro_kg = (self.preco_kg - self.custo_kg)
    print('''
O lucro deste produto é de R$''', lucro_kg, '''por kg
    ''')


class venda():

  def __init__(self, produto, quantidade):
    self.quantidade = quantidade
    self.produto = produto

  def baixa_prod():
    prod_cod = int(input('qual o código do produto? '))
    venda.quantidade = int(input('quantidade de produtos: '))

    for produto in produtos_peso:
      if (prod_cod == produto.codigo):
        produto.quantidade = produto.quantidade - venda.quantidade
    print(produtos_peso)

    for produto in produtos_uni:
      if (prod_cod == produto.codigo):
        produto.quantidade = produto.quantidade - venda.quantidade
    print(produtos_uni)


produtos_peso = []
produtos_uni = []


def exibir_menu():
  print('''  
        - Menu -
1) cadastro de protudo
2) Entrada de produto
3) Baixa/Venda
4) Calcular o lucro de um produto
0) Sair
  ''')


def cadastro():

  codigo = int(input('código: '))
  descricao = input('descrição: ')
  validade = input('data de validade: ')

  tipo_prod = int(input('''Por peso[1] ou por unidade[2] ? '''))

  if (tipo_prod == 1):
    custo_kg = input('custo por kg: ')
    preco_kg = input('preço por kg: ')
    produto = prod_peso(custo_kg, preco_kg, codigo, descricao, validade, 0)
    produtos_peso.append(produto)

  elif (tipo_prod == 2):
    custo_uni = input('custo por unidade: ')
    preco_uni = input('preço por unidade: ')
    produto = prod_uni(custo_uni, preco_uni, codigo, descricao, validade, 0)
    produtos_uni.append(produto)


def entrada():
  cod_prod = int(input('qual o código do produto? '))
  qtd = int(input('quantidade de produtos: '))

  for produto in produtos_peso:
    if (cod_prod == produto.codigo):
      produto.quantidade = produto.quantidade + qtd
  print(produtos_peso)

  for produto in produtos_uni:
    if (cod_prod == produto.codigo):
      produto.quantidade = produto.quantidade + qtd
  print(produtos_uni)


def calcula_lucro():
  cod_produto = int(input('Qual o código do produto ?  '))
  for produto in produtos_peso:
    if (cod_produto == produto.codigo):
      produto.calc_lucro()

  for produto in produtos_uni:
    if (cod_produto == produto.codigo):
      produto.calc_lucro()


while True:
  exibir_menu()
  opt = int(input('escolha uma opção: '))

  if (opt == 1):
    cadastro()
    print(produtos_peso)
    print(produtos_uni)

  elif (opt == 2):
    entrada()

  elif (opt == 3):
    venda.baixa_prod()

  elif (opt == 4):
    calcula_lucro()

  elif (opt == 0):
    print("até logo")
    quit()
