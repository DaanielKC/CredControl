from Classes.SituacaoLimite import SituacaoLimite
from Classes.GestaoLimiteService import GestaoLimiteService
from datetime import datetime
from Classes.HistoricoAlteracaoLimite import HistoricoAlteracaoLimite

class GestaoLimiteServiceImpl(GestaoLimiteService):
    def __init__(self, limiteRepository, historicoRepository):
        self.limiteRepository = limiteRepository
        self.historicoRepository = historicoRepository

    def desbloquearLimite(self, idLimite, matriculaUsuario):
        limite = self.limiteRepository.buscarPorId(idLimite)

        # Verifica se o limite existe
        if limite is None:
            return "Desbloqueio de limite não realizado."

        # Verifica se o limite está bloqueado ou ativo
        if limite.situacao != SituacaoLimite.BLOQUEADO:
            return "Desbloqueio de limite não realizado."

        now = datetime.now()

        # Sabendo que o limite está bloqueado, vamos desbloqueá-lo e salvá-lo no repositório
        situacaoAnterior = limite.situacao
        limite.situacao = SituacaoLimite.ATIVO
        limite.dataAtualizacao = now
        self.limiteRepository.salvar(limite)
        
        
        # Registra a alteração no histórico
        historico = HistoricoAlteracaoLimite(
            id = None,
            idLimite = limite.idLimite,
            situacaoAnterior = situacaoAnterior,
            situacaoNova = limite.situacao,
            matriculaUsuario = matriculaUsuario,
            dataHora = now
        )
        self.historicoRepository.salvar(historico)

        return "Limite desbloqueado com sucesso."