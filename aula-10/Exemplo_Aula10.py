class FormaGeometrica():
  def calcArea(self):
    return

class Quadrado(FormaGeometrica):
  def __init__(self,base):
    self.base = base
  def calcArea(self):
    return self.base * self.base

class Circulo(FormaGeometrica):
  def __init__(self, raio):
    self.raio = raio
  def calcArea(self):
    return self.raio * self.raio * 3.14

class Triangulo(FormaGeometrica):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def calcArea(self):
    return (self.base * self.altura)/2

quad1 = Quadrado(2)
quad2 = Quadrado(3)
cir1 = Circulo(1)
cir2 = Circulo(2)
tri1 = Triangulo (2,3)
tri2 = Triangulo (4,5)


formas_geometricas = [quad1, quad2 , cir1, cir2, tri1, tri2]

soma=0
for forma in formas_geometricas:
  soma = soma + forma.calcArea()

print("A �rea total � de {}".format(soma))