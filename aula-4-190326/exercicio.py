import sys
class Produto:
    def __init__(self, code, description, price, cost):
        self.code = code
        self.description = description
        self.price = price
        self.cost = cost
    def setCode(self, code):
        self.code = code
    def setDescription(self, description):
        self.description = description
    def setPrice(self, price):
        if (self.price*1.10)< price:
            return 'bigger price'
        elif (self.price*0.90)> price:
            return 'lower price'
        else:
            self.price = price
    def setCost(self, cost):
        self.cost = cost
    def getCode(self):
        return self.code
    def getDescription(self):
        return self.description
    def getPrice(self):
        return self.price
    def getCost(self):
        return self.cost
    def calculaMargem(self):
        return ((self.price - self.cost) / self.price) * 100

product_dict = {}
while True:
    user_input = input('''
1 - cadastrar produto
2 - listar produtos
3 - calcular margem
4 - alterar produto
5 - sair 
''')
    if user_input == '1':
        code = int(input('code: '))
        description = input('description: ')
        price= float(input('price: '))
        cost = float(input('cost: '))
        product = Produto(code, description, price, cost)
        product_dict = {**product_dict, code: product}
    if user_input == '2':
        if not product_dict:
            print('não há produtos cadastrados')
        for k in product_dict:
            code = product_dict[k].getCode()
            description = product_dict[k].getDescription()
            price = product_dict[k].getPrice()
            cost = product_dict[k].getCost()
            print(f"produto {code}: descrição: {description}, preço: {price}, custo: {cost}")
    if (user_input == '3'):
        if not product_dict:
            print('não há produtos cadastrados')
        else:
            code_input = int(input('digite o código do produto: '))
            if not product_dict[code_input]:
                print("esse produto não existe")
            else: 
                product = product_dict[code_input]
                print(product.calculaMargem())
    if (user_input == '4'):
        if not product_dict:
            print('não há produtos cadastrados')
        else:
            code_input = int(input('digite o código do produto: '))
            if not product_dict[code_input]:
                print("esse produto não existe")
            else: 
                code = int(input('code: '))
                description = input('description: ')
                price= float(input('price: '))
                cost = float(input('cost: '))
                product = product_dict[code_input]

                product.setCode(code)
                product.setDescription(description)
                product.setPrice(price)
                product.setCost(cost)
    if user_input == '5':
        sys.exit() 
        