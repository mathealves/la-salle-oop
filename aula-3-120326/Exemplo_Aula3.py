# Exemplo aula
class Pessoa: 
        def __init__(self, nome, idade, endereco, sexo):
            self.nome = nome 
            self.idade = idade
            self.endereco = endereco
            self.sexo = sexo
        def setNome(self, nome): 
            self.nome = nome 
        def setIdade(self, idade):
            if idade < self.idade:
                print('Idade deve ser maior que a atual')
            else: 
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
        def getAtributos(self):
            return self.atributos
    
p1 = Pessoa('Maria', 41, 'Rua 15 de Janeiro 100', 'F')
p2 = Pessoa('Jo�o', 52, 'Rua coronel vicente 200', 'M')
p3 = Pessoa('Pedro', 30, 'Rua Muk 105', 'M')

dict = { 1: 'nome', 2: 'idade', 3: 'endereco', 4: 'sexo'}

persons = []
add_more = True

while add_more:
    atributes = []
    for i in range(1, 5):
        atributes.append(input(f'Digite o atributo {dict[i]}: '))
    person = Pessoa(atributes[0], atributes[1], atributes[2], atributes[3])
    persons.append(person)
    add_more = input('Deseja adicionar mais pessoas? (s/n) ').lower() == 's'