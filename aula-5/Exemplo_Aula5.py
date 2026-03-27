class Pessoa: 
        def __init__(self, nome: str, idade, endereco, sexo): 
            self.nome = nome 
            self.idade = idade
            self.endereco = endereco
            self.sexo = sexo
        def setNome(self, nome): 
            self.nome = nome 
        def setIdade(self, idade): 
            self.idade = idade 
        def setEndereco(self, endereco): 
            self.endereco = endereco 
        def setSexo(self, sexo): 
            self.sexo = sexo 
        def getNome(self): 
            return self.nome 
        def getIdade(self): 
            return self.idade
        def getEndereco(self): 
            return self.endereco
        def getSexo(self): 
            return self.sexo

class Cofrinho: 
        def __init__(self, umaPessoa: Pessoa): 
            self.dono = umaPessoa 
            self.qt50 = 0
            self.qt25 = 0
            self.qt10 = 0
        def getDono(self): 
            return self.dono
        def setDono (self, novoDono):
            self.dono = novoDono
        def depositaUmaMoedaCinquentaCentavos (self):
            self.qt50 = self.qt50 +1
        def depositaUmaMoedaDezCentavos (self):
            self.qt10 = self.qt10 +1
        def depositaUmaMoedaVinteCincoCentavos (self):
            self.qt25 = self.qt25 +1
        def calculaTotal (self):
            total = self.qt50*0.5+ self.qt25*0.25+ self.qt10*0.10
            return total

p1 = Pessoa('Maria', 41, 'ABC, 34', 'F')
p2 = Pessoa('João', 52, 'DEF, 56', 'M')
p3 = Pessoa('Pedro', 30, 'XYZ, 52', 'M')

c1 = Cofrinho(p1)
c2 = Cofrinho(p2)

print ("O dono do cofrinho 1 é " + c1.getDono().getNome())
print ("O dono do cofrinho 2 é " + c2.dono.getNome())

c1.depositaUmaMoedaCinquentaCentavos()
c1.depositaUmaMoedaVinteCincoCentavos()
c1.depositaUmaMoedaDezCentavos()

print ("O total do cofrinho de " + c1.dono.getNome() + " é", c1.calculaTotal())

c1.dono = (p3)
print ("O dono do cofrinho 1 é " + c1.dono.getNome())