class Pessoa(): 
        def __init__(self, nome, endereco): 
            self.nome = nome 
            self.endereco = endereco 

class PessoaFisica(Pessoa): 
        def __init__(self, nome, endereco, CPF, dataNascimento): 
            super().__init__(nome, endereco)   
            self.CPF = CPF 
            self.dataNascimento = dataNascimento 

class PessoaJuridica(Pessoa): 
        def __init__(self, nome, endereco, CNPJ, inscricaoEstadual): 
            super().__init__(nome, endereco)
            self.CNPJ = CNPJ 
            self.inscricaoEstadual = inscricaoEstadual 

p1 = PessoaFisica('Maria', 'ABC, 123', '1222333', '20/08/1980')
p2 = PessoaJuridica('Comercial LTDA', 'XYZ, 123', '2223334', '334444')
p3 = Pessoa ('Marta', 'XYZ, 134')


print (p1.nome + ' - ' + p1.endereco + ' - ' + p1.CPF + ' - ' + p1.dataNascimento)

print (p2.nome + ' - ' + p2.endereco + ' - ' + p2.CNPJ + ' - ' + p2.inscricaoEstadual)

print (p3.nome + ' - ' + p3.endereco)
p3.nome = 'Marta Silveira'
print (p3.nome + ' - ' + p3.endereco)