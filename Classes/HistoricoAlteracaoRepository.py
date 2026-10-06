class HistoricoAlteracaoRepository():
    def __init__(self):
        self.historicos = []
        self.proximoId = 1

    def salvar(self, historico):
        historico.id = self.proximoId
        self.proximoId += 1
        self.historicos.append(historico)