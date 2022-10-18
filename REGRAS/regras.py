from MODEL.asma import Asma


class Regra:

    def __init__(self, recomendacao, asma=Asma(False, 0, 0)):
        self.recomendacao = recomendacao
        self.asma = asma

    def setRecomendacao(self, recomendacao):
        self.recomendacao = recomendacao

    def setAsma(self, asma):
        self.asma = asma

    def getRecomendado(self):
        return self.recomendacao

    def getAsma(self):
        return self.asma

    def indicarAsma(self):
        return None
