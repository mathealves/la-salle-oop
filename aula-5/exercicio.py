class Editora:
    def __init__(self, codigoEditora, razaoSocial, nomeContato, telefone):
        self.codigoEditora = codigoEditora
        self.razaoSocial = razaoSocial
        self.nomeContato = nomeContato
        self.telefone = telefone
    def setCodigoEditora(self, codigoEditora):
        self.codigoEditora = codigoEditora 
    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial
    def setNomeContato(self, nomeContato):
        self.nomeContato = nomeContato
    def setTelefone(self, telefone):
        self.telefone = telefone
    def getCodigoEditora(self):
        return self.codigoEditora
    def getRazaoSocial(self):
        return self.razaoSocial
    def getNomeContato(self):
        return self.nomeContato
    def getTelefone(self):
        return self.telefone
    
class Livro:
    def __init__(self, codigoLivro, tituloLivro, codigoISBN, editora):
        self.codigoLivro = codigoLivro
        self.tituloLivro = tituloLivro
        self.codigoISBN = codigoISBN
        self.editora = editora
    def setCodigoLivro(self, codigoLivro):
        self.codigoLivro = codigoLivro
    def setTituloLivro(self, tituloLivro):
        self.tituloLivro = tituloLivro
    def setCodigoISBN(self, codigoISBN):
        self.codigoISBN = codigoISBN
    def setEditora(self, editora):
        self.editora = editora
    def getCodigoLivro(self):
        return self.codigoLivro
    def getTituloLivro(self):
        return self.tituloLivro
    def getCodigoISBN(self):
        return self.codigoISBN
    def getEditora(self):
        return self.editora
    
editoras = []
livros = []

while True:
    user_input = input('''1 - cadastrar editora
2 - cadastrar livro
3 - pesquisar editora
4 - pesquisar livro
5 - sair
''')
    if user_input == '1':
        codigoEditora = int(input('codigo editora: '))
        razaoSocial = input('razao social: ')
        nomeContato = input('nome contato: ')
        telefone = input('telefone: ')
        editora = Editora(codigoEditora, razaoSocial, nomeContato, telefone)
        editoras.append(editora)
    if user_input == '2':
        codigoLivro = int(input('codigo livro: '))
        tituloLivro = input('titulo livro: ')
        codigoISBN = input('codigo ISBN: ')
        editoraInput = int(input(f"editoras disponíveis: {[editora.getCodigoEditora() for editora in editoras]}\ncodigo editora do livro: "))
        editoraLivro = next((editora for editora in editoras if editora.getCodigoEditora() == editoraInput), None)
        livro = Livro(codigoLivro, tituloLivro, codigoISBN, editoraLivro)
        livros.append(livro)
    if user_input == '3':
        if not editoras:
            print('não há editoras cadastradas')
        else:
            razaoSocialEditora = input('razao social da editora: ')
            for editora in editoras:
                if editora.getRazaoSocial() == razaoSocialEditora:
                    print(f"código da editora: {editora.getCodigoEditora()}, razão social: {editora.getRazaoSocial()}, nome contato: {editora.getNomeContato()}, telefone: {editora.getTelefone()}")
    if user_input == '4':
        if not livros:
            print('não há livros cadastrados')
        else:
            tituloLivro = input('titulo do livro: ')
            for livro in livros:
                if livro.getTituloLivro() == tituloLivro:
                    print(f"código do livro: {livro.getCodigoLivro()}, título: {livro.getTituloLivro()}, ISBN: {livro.getCodigoISBN()}, editora: {livro.getEditora().getRazaoSocial()}")
    if user_input == '5':
        break