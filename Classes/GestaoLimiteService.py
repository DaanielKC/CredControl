from abc import ABC, abstractmethod

class GestaoLimiteService(ABC):
    @abstractmethod
    def desbloquearLimite(self, idLimite, matriculaUsuario):
        pass