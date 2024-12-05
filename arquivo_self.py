class Filme():
    def __init__(self, descricao):
        self.descricao = descricao # difinindo o atributo da classe 
        print('Criando uma instancia')
    
    def assistir_filme(self): # metodo é definido como uma função dentro de uma classe
        print('iniciando filme')

filme1 = Filme() #instancia a classe

filme1.assistir_filme() 



'''Self é a referência do objeto'''