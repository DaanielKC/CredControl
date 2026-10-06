from abc import ABC, abstractmethod

# Classe abstrata para o serviço de gestão de limite
class GestaoLimiteService(ABC):
    @abstractmethod
    def desbloquearLimite(self, idLimite, matriculaUsuario):
        pass