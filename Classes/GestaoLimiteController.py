class GestaoLimiteController():
    def __init__(self, service):
        self.service = service

    def executar(self):
        idLimite = int(input("Digite o ID do limite a ser desbloqueado: "))
        matriculaUsuario = input("Digite a matrícula do usuário: ")

        mensagem = self.service.desbloquearLimite(idLimite, matriculaUsuario)
        print(mensagem)
