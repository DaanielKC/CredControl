import os
from datetime import datetime
from Classes.LimiteRepository import LimiteRepository
from Classes.HistoricoAlteracaoRepository import HistoricoAlteracaoRepository
from Classes.LimiteContaCartao import LimiteContaCartao
from Classes.SituacaoLimite import SituacaoLimite
from Classes.GestaoLimiteServiceImpl import GestaoLimiteServiceImpl
from Classes.GestaoLimiteController import GestaoLimiteController

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

limiteRepository = LimiteRepository()
historicoRepository = HistoricoAlteracaoRepository()

# Criação de um limite bloqueado para teste
limiteBloqueado = LimiteContaCartao(
    idLimite = 1001,
    numeroCartao = "4002 8922 4002 8922",
    cpfCnpj = "123.456.789-10",
    valorLimite = 8436.72,
    situacao = SituacaoLimite.BLOQUEADO,
    dataAtualizacao = datetime.now()
)
limiteRepository.limites.append(limiteBloqueado)

# Criação de um limite ativo para teste
limiteAtivo = LimiteContaCartao(
    idLimite = 1002,
    numeroCartao = "1234 5678 9876 5432",
    cpfCnpj = "109.876.543-21",
    valorLimite = 108534.92,
    situacao = SituacaoLimite.ATIVO,
    dataAtualizacao = datetime.now()
)
limiteRepository.limites.append(limiteAtivo)

service = GestaoLimiteServiceImpl(limiteRepository, historicoRepository)

controller = GestaoLimiteController(service)

clear()
print("-------------------------")
print("| DESBLOQUEIO DE LIMITE |")
print("-------------------------")
print()
print("1. Desbloquear limite")
print("2. Sair")
print()
opcao = input("Seleciona a opção desejada: ")
clear()
while opcao != "2":
    if opcao == "1":
        controller.executar()
        print()
        input("Pressione Enter para continuar: ")
        clear()
    else:
        clear()
        print("Opção inválida. Tente novamente.")
        print()

    print("-------------------------")
    print("| DESBLOQUEIO DE LIMITE |")
    print("-------------------------")
    print()
    print("1. Desbloquear limite")
    print("2. Sair")
    print()
    opcao = input("Seleciona a opção desejada: ")
    clear()
