class LimiteRepository():
    def __init__(self):
        self.limites = []

    def buscarPorId(self, idLimite):
        for lim in self.limites:
            if lim.idLimite == idLimite:
                return lim
        return None

    def salvar(self, limite):
        for i, limiteExistente in enumerate(self.limites):
            if limiteExistente.idLimite == limite.idLimite:
                self.limites[i] = limite
                return

    