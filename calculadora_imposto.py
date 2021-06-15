def somaLista(precos):
    soma = 0
    for i in precos:
        soma = soma + i
    return soma

class CalculadoraImposto:
    __preco = 0.0
    
    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco
    

class Pais(CalculadoraImposto):
    __imposto: 0.0
    
    def getPreco(self):
        return super().getPreco() * self.__imposto
    
    def getImposto(self):
        return self.__imposto
    
    def setImposto(self, imposto):
        self.__imposto = imposto
    
america = Pais()
america.setPreco(100.00)
america.setImposto(1.1)
print("O preço do produto na América com imposto é {:.2f}".format(america.getPreco()))

europa = Pais()
europa.setPreco(100.00)
europa.setImposto(1.15)
print("O preço do produto na Europa com imposto é {:.2f}".format(europa.getPreco()))

asia = Pais()
asia.setPreco(100.00)
asia.setImposto(1.20)
print("O preço do produto na Asia com imposto é {:.2f}".format(asia.getPreco()))

lista = []
lista.append(america.getPreco())
lista.append(europa.getPreco())
lista.append(asia.getPreco())

print("A soma dos valores dos produtos acrescido de impostos é {:.2f}".format(somaLista(lista)))
