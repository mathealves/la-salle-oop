
class Montadora:
    def __init__(self, codigoMontadora, estado, razaoSocial):
        self.codigoMontadora = codigoMontadora
        self.estado = estado
        self.razaoSocial = razaoSocial
    def setCodigoMontadora(self, codigoMontadora):
        self.codigoMontadora = codigoMontadora
    def setEstado(self, estado):
        self.estado = estado
    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial
    def getCodigoMontadora(self):
        return self.codigoMontadora
    def getEstado(self):
        return self.estado
    def getRazaoSocial(self):
        return self.razaoSocial

class Modelo:
    def __init__(self, codigoModelo, nomeModelo, montadora):
        self.codigoModelo = codigoModelo
        self.nomeModelo = nomeModelo
        self.montadora = montadora
    def setCodigoModelo(self, codigoModelo):
        self.codigoModelo = codigoModelo
    def setNomeModelo(self, nomeModelo):
        self.nomeModelo = nomeModelo
    def setMontadora(self, montadora):
        self.montadora = montadora
    def getCodigoModelo(self):
        return self.codigoModelo
    def getNomeModelo(self):
        return self.nomeModelo
    def getMontadora(self):
        return self.montadora

class Carro:
    def __init__(self, placa, modelo, anoFabricacao):
        self.placa = placa
        self.modelo = modelo
        self.anoFabricacao = anoFabricacao
    def setPlaca(self, placa):
        self.placa = placa
    def setModelo(self, modelo):
        self.modelo = modelo
    def setAnoFabricacao(self, anoFabricacao):
        self.anoFabricacao = anoFabricacao
    def getPlaca(self):
        return self.placa
    def getModelo(self):
        return self.modelo
    def getAnoFabricacao(self):
        return self.anoFabricacao

montadoras = []
modelos = []
carros = []

"""
1 – Cadastro Montadora
2 – Cadastro Modelo. Apresentar uma lista das montadoras para vincular ao modelo
3 - Cadastro Carro. Apresentar uma lista dos modelos para vincular ao carro
4 – Listar Montadoras
5 – Listar Modelos
6 – Listar Carros
7 – Sair
"""

while True:
    user_input = input('''1 - cadastrar montadora
2 - cadastrar modelo
3 - cadastrar carro
4 - listar montadoras
5 - listar modelos
6 - listar carros
7 - sair
''')
    if user_input == '1':
        codigoMontadora = int(input('codigo montadora: '))
        estado = input('estado (UF): ')
        razaoSocial = input('razao social: ')
        montadora = Montadora(codigoMontadora, estado, razaoSocial)
        montadoras.append(montadora)
    if user_input == '2':
        if not montadoras:
            print('não há montadoras cadastradas')
        else:
            codigoModelo = int(input('codigo modelo: '))
            nomeModelo = input('nome do modelo: ')
            print(f"montadoras disponíveis: {[f'{m.getCodigoMontadora()} - {m.getRazaoSocial()}' for m in montadoras]}")
            codigoMontadoraInput = int(input('codigo da montadora: '))
            montadoraModelo = next((m for m in montadoras if m.getCodigoMontadora() == codigoMontadoraInput), None)
            if montadoraModelo is None:
                print('montadora não encontrada')
            else:
                modelo = Modelo(codigoModelo, nomeModelo, montadoraModelo)
                modelos.append(modelo)
    if user_input == '3':
        if not modelos:
            print('não há modelos cadastrados')
        else:
            placa = input('placa: ')
            anoFabricacao = int(input('ano de fabricação: '))
            print(f"modelos disponíveis: {[f'{m.getCodigoModelo()} - {m.getNomeModelo()}' for m in modelos]}")
            codigoModeloInput = int(input('codigo do modelo: '))
            modeloCarro = next((m for m in modelos if m.getCodigoModelo() == codigoModeloInput), None)
            if modeloCarro is None:
                print('modelo não encontrado')
            else:
                carro = Carro(placa, modeloCarro, anoFabricacao)
                carros.append(carro)
    if user_input == '4':
        if not montadoras:
            print('não há montadoras cadastradas')
        else:
            print(f"montadoras disponíveis: {[f'{m.getCodigoMontadora()} - {m.getRazaoSocial()} - {m.getEstado()}' for m in montadoras]}")
    if user_input == '5':
        if not modelos:
            print('não há modelos cadastrados')
        else:
            print(f"modelos disponíveis: {[f'{m.getCodigoModelo()} - {m.getNomeModelo()} - {m.getMontadora().getRazaoSocial()}' for m in modelos]}")
    if user_input == '6':
        if not carros:
            print('não há carros cadastrados')
        else:
            print(f"carros disponíveis: {[f'placa: {c.getPlaca()} - modelo: {c.getModelo().getNomeModelo()} - montadora: {c.getModelo().getMontadora().getRazaoSocial()} - ano: {c.getAnoFabricacao()}' for c in carros]}")
    if user_input == '7':
        break
