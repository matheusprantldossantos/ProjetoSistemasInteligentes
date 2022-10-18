from CONSTANTES.constates import Mensagens


class Asma:

    def __init__(self, sibilar, idade, qnt_criterios):
        self.sibilar = sibilar
        self.idade = idade
        self.qnt_criterios = qnt_criterios

    def setSimbilar(self, sibilar):
        self.sibilar = sibilar

    def getSimbilar(self):
        return self.simbilar

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def setQntCriterios(self, qnt_criterios):
        self.qnt_criterios = qnt_criterios

    def getQntCriterios(self):
        return self.qnt_criterios


class NaoAsmaInduzida(Asma):

    def __int__(self, recomendacao):
        super().__int__()
        self.recomendacao = Mensagens.NEGATIVO_ASMA_INDUZIDO

    def getRecomendacao(self):
        return self.recomendacao


class AsmaAtopica(Asma):

     def __int__(self):
         print("")
