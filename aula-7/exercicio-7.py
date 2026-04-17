class Funcionario(): 
        def __init__(self, nome, cpf, salario, departamento): 
            self.nome = nome 
            self.cpf = cpf
            self.salario = salario
            self.departamento = departamento
        
        def bonificar(self): 
            self.salario += self.salario * 0.1

class Gerente(Funcionario): 
        def __init__(self, nome, cpf, salario, departamento, senha, n_employees): 
            super().__init__(nome, cpf, salario, departamento)   
            self.senha = senha
            self.n_employees = n_employees

        def autenticarSenha(self, senha): 
            return self.senha == senha
        
        def bonificar(self):
              self.salario += self.salario * 0.15

class Vendedor(Funcionario): 
        def __init__(self, nome, cpf, salario, departamento, vendas, comissao): 
            super().__init__(nome, cpf, salario, departamento)
            self.vendas = vendas
            self.comissao = comissao
        
        def atualizaQuantidadeVendas(self, qtd): 
            self.vendas += qtd
        
        def calculaSalario(self): 
            return self.salario + self.comissao

funcionarios = []
gerentes = []
vendedores = []

while True:
    user_input = input('''
1  - cadastrar funcionário
2  - cadastrar gerente
3  - cadastrar vendedor
4  - bonificar funcionário
5  - bonificar gerente
6  - autenticar senha gerente
7  - atualizar quantidade de vendas do vendedor
8  - calcular salário do vendedor
9  - listar funcionários
10 - listar gerentes
11 - listar vendedores
12 - sair
> ''')

    if user_input == '1':
        nome = input('nome: ')
        cpf = input('CPF: ')
        salario = float(input('salário: '))
        departamento = input('departamento: ')
        funcionarios.append(Funcionario(nome, cpf, salario, departamento))
        print('funcionário cadastrado com sucesso.')

    elif user_input == '2':
        nome = input('nome: ')
        cpf = input('CPF: ')
        salario = float(input('salário: '))
        departamento = input('departamento: ')
        senha = input('senha: ')
        n_employees = int(input('número de funcionários gerenciados: '))
        gerentes.append(Gerente(nome, cpf, salario, departamento, senha, n_employees))
        print('gerente cadastrado com sucesso.')

    elif user_input == '3':
        nome = input('nome: ')
        cpf = input('CPF: ')
        salario = float(input('salário base: '))
        departamento = input('departamento: ')
        vendas = int(input('quantidade de vendas: '))
        comissao = float(input('comissão: '))
        vendedores.append(Vendedor(nome, cpf, salario, departamento, vendas, comissao))
        print('vendedor cadastrado com sucesso.')

    elif user_input == '4':
        if not funcionarios:
            print('não há funcionários cadastrados.')
        else:
            print('funcionários disponíveis:')
            for f in funcionarios:
                print(f'  CPF: {f.cpf} - {f.nome} - salário atual: {f.salario:.2f}')
            cpf_input = input('CPF do funcionário a bonificar: ')
            funcionario = next((f for f in funcionarios if f.cpf == cpf_input), None)
            if funcionario is None:
                print('funcionário não encontrado.')
            else:
                funcionario.bonificar()
                print(f'bonificação aplicada. novo salário: {funcionario.salario:.2f}')

    elif user_input == '5':
        if not gerentes:
            print('não há gerentes cadastrados.')
        else:
            print('gerentes disponíveis:')
            for g in gerentes:
                print(f'  CPF: {g.cpf} - {g.nome} - salário atual: {g.salario:.2f}')
            cpf_input = input('CPF do gerente a bonificar: ')
            gerente = next((g for g in gerentes if g.cpf == cpf_input), None)
            if gerente is None:
                print('gerente não encontrado.')
            else:
                gerente.bonificar()
                print(f'bonificação aplicada. novo salário: {gerente.salario:.2f}')

    elif user_input == '6':
        if not gerentes:
            print('não há gerentes cadastrados.')
        else:
            print('gerentes disponíveis:')
            for g in gerentes:
                print(f'  CPF: {g.cpf} - {g.nome}')
            cpf_input = input('CPF do gerente: ')
            gerente = next((g for g in gerentes if g.cpf == cpf_input), None)
            if gerente is None:
                print('gerente não encontrado.')
            else:
                senha_input = input('senha: ')
                if gerente.autenticarSenha(senha_input):
                    print('senha autenticada com sucesso.')
                else:
                    print('senha incorreta.')

    elif user_input == '7':
        if not vendedores:
            print('não há vendedores cadastrados.')
        else:
            print('vendedores disponíveis:')
            for v in vendedores:
                print(f'  CPF: {v.cpf} - {v.nome} - vendas atuais: {v.vendas}')
            cpf_input = input('CPF do vendedor: ')
            vendedor = next((v for v in vendedores if v.cpf == cpf_input), None)
            if vendedor is None:
                print('vendedor não encontrado.')
            else:
                qtd = int(input('quantidade de vendas a adicionar: '))
                vendedor.atualizaQuantidadeVendas(qtd)
                print(f'vendas atualizadas. total de vendas: {vendedor.vendas}')

    elif user_input == '8':
        if not vendedores:
            print('não há vendedores cadastrados.')
        else:
            print('vendedores disponíveis:')
            for v in vendedores:
                print(f'  CPF: {v.cpf} - {v.nome}')
            cpf_input = input('CPF do vendedor: ')
            vendedor = next((v for v in vendedores if v.cpf == cpf_input), None)
            if vendedor is None:
                print('vendedor não encontrado.')
            else:
                print(f'salário total de {vendedor.nome}: {vendedor.calculaSalario():.2f}')

    elif user_input == '9':
        if not funcionarios:
            print('não há funcionários cadastrados.')
        else:
            nome_busca = input('nome do funcionário (ou parte do nome): ')
            resultado = [f for f in funcionarios if nome_busca.lower() in f.nome.lower()]
            if not resultado:
                print('nenhum funcionário encontrado.')
            else:
                for f in resultado:
                    print(f'  CPF: {f.cpf} - {f.nome} - departamento: {f.departamento} - salário: {f.salario:.2f}')

    elif user_input == '10':
        if not gerentes:
            print('não há gerentes cadastrados.')
        else:
            nome_busca = input('nome do gerente (ou parte do nome): ')
            resultado = [g for g in gerentes if nome_busca.lower() in g.nome.lower()]
            if not resultado:
                print('nenhum gerente encontrado.')
            else:
                for g in resultado:
                    print(f'  CPF: {g.cpf} - {g.nome} - departamento: {g.departamento} - salário: {g.salario:.2f} - funcionários gerenciados: {g.n_employees}')

    elif user_input == '11':
        if not vendedores:
            print('não há vendedores cadastrados.')
        else:
            nome_busca = input('nome do vendedor (ou parte do nome): ')
            resultado = [v for v in vendedores if nome_busca.lower() in v.nome.lower()]
            if not resultado:
                print('nenhum vendedor encontrado.')
            else:
                for v in resultado:
                    print(f'  CPF: {v.cpf} - {v.nome} - departamento: {v.departamento} - vendas: {v.vendas} - comissão: {v.comissao:.2f}')

    elif user_input == '12':
        break

