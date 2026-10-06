# CredControl
Este projeto foi criado para a avaliação P1 da disciplina INE5404 - Programação Orientada a Objetos II.  Nesta avaliação, é preciso modelar e implementar o CredControl, um sistema fictício de gestão de limites, com uma única funcionalidade: o desbloqueio de limite.

## Linguagem utilizada:
- Python 3

## Instruções
1. Instale o Python 3
2. Abra um terminal na pasta do projeto
3. Execute `python main.py`
4. Selecione a opção 1 (Desbloquear limite)
5. Informe o ID do limite e a matrícula do usuário
6. Pressione 'Enter' para prosseguir
7. Para encerrar, selecione a opção 2 (Sair)

O projeto inicia com dois limites já registrados, um na situação **BLOQUEADO**, com id **1001**, e outro na situação **ATIVO**, com id **1002**.

## Seção 5 - Questões
Questão 01. Qual relação UML liga GestaoLimiteServiceImpl à interface GestaoLimiteService?\
**Resposta:** É a relação de realização.

Questão 02: Cite uma dependência existente entre GestaoLimiteServiceImpl e um repositório.\
**Resposta:** GestaoLimiteServiceImpl tem dependência com o LimiteRepository, pois ele usa esse Repository para identificar e atualizar o limite durante a operação de desbloqueio.


