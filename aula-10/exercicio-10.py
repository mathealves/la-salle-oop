SEMANAS = 4.5

class Empregado():
  def __init__(self, nome):
    self.nome = nome
  def retornaPagamento(self):
    pass

class Assalariado(Empregado):
  def __init__(self, nome, salario):
    super().__init__(nome)
    self.nome = nome
    self.salario = salario

  def retornaPagamento(self):
    return self.salario
  
class Horista(Empregado):
  def __init__(self, nome, valor_hora, qtde_horas):
    super().__init__(nome)
    self.nome = nome
    self.valor_hora = valor_hora
    self.qtde_horas = qtde_horas

  def retornaPagamento(self):
    return self.valor_hora * self.qtde_horas * SEMANAS

all_empregados = []
total = 0
while True:
  user_input = input('''
1 - cadastrar assalariado
2 - cadastrar horista
3 - sair
Escolha uma opção: ''')

  if user_input == '1':
    nome = input("Digite o nome do assalariado: ")
    salario = float(input("Digite o salário do assalariado: "))
    empregado = Assalariado(nome, salario)
    all_empregados.append(empregado)
    for emp in all_empregados:
      total += emp.retornaPagamento()
    print(f"Gasto total da empresa com folha salarial: {total}")
  elif user_input == '2':
    nome = input("Digite o nome do horista: ")
    valor_hora = float(input("Digite o valor da hora do horista: "))
    qtde_horas = float(input("Digite a quantidade de horas trabalhadas pelo horista: "))
    empregado = Horista(nome, valor_hora, qtde_horas)
    all_empregados.append(empregado)
    for emp in all_empregados:
      total += emp.retornaPagamento()
    print(f"Gasto total da empresa com folha salarial: {total}")
  elif user_input == '3':
    break
  else:
    print("Opção inválida. Tente novamente.")
