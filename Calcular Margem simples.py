class produto:

  def __init__(self, codigo, descrição, preço, custo):
    self.codigo = codigo
    self.descrição = descrição
    self.preço = preço
    self.custo = custo

  def setCodigo(self, codigo):
    self.codigo = codigo

  def setDescrição(self, descrição):
    self.descrição = descrição

  def setPreço(self, preço):
    self.preço = preço

  def setCusto(self, custo):
    self.custo = custo

  def getCodigo(self):
    return self.codigo

  def getDescrição(self):
    return self.descrição

  def getPreço(self):
    return self.preço

  def getCusto(self):
    return self.custo

  def calc_margem(self):
    margem = ((self.custo / self.preço) * 100)
    print('''
  ---A margem de lucro deste produto é de {}%---
    '''.format(margem))


lista = []

while True:
  print('''Digite um numero para escolher uma opção:
1 - Cadasrar um produto
2 - calcular margem
3 - sair''')
  opt = int(input('escolha uma opção: '))

  if (opt == 1):
    NCodigo = input('digite o código do produto: ')
    NDescrição = input('digite a descrição do produto: ')
    NCusto = float(input('digite o custo do produto: '))
    NPreço = float(input('digite o preço do produto: '))

    novoProduto = produto(NCodigo, NDescrição, NCusto, NPreço)
    lista.append(novoProduto)
    print(lista)

  elif (opt == 2):
    cod = input('qual o código do produto?')
    for produto in lista:
      if (cod == produto.codigo):
        produto.calc_margem()

  elif (opt == 3):
    print("até logo")
    quit()
