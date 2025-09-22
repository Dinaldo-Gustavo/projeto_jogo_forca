import random
import string


class Senha:
    def __init__(self, tamanho):
        self.caracteres = ''
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.caracteres}'

    def maiusculas(self):
        self.caracteres += string.ascii_uppercase

    def minusculas(self):
        self.caracteres += string.ascii_lowercase

    def numeros(self):
        self.caracteres += string.digits

    def simbolos(self):
        self.caracteres += string.punctuation

    def gerar_senha(self):
        if not self.caracteres:
            return "Erro: Não foi selecionado nenhum tipo de caracter"

        senha_gerada = ''.join(random.choice(self.caracteres) for _ in range(self.tamanho))
        return senha_gerada


print("GERADOR DE SENHAS ALEATÓRIAS")

tamanho_escolhido = int(input("Escolha o tamanho da sua senha: "))
gerador = Senha(tamanho=tamanho_escolhido)

print("Agora escolha entre Sim (S) ou Não (N)")

maiusculas = input("Deseja adicionar maiúsculas? ").upper()
minusculas = input("Deseja adicionar minúsculas? ").upper()
numeros = input("Deseja adicionar números? ").upper()
pontuacao = input("Deseja adicionar símbolos? ").upper()

if maiusculas == "S":
    gerador.maiusculas()
if minusculas == "S":
    gerador.minusculas()
if numeros == "S":
    gerador.numeros()
if pontuacao == "S":
    gerador.simbolos()

nova_senha = gerador.gerar_senha()
print(f"A senha gerada foi {nova_senha}")