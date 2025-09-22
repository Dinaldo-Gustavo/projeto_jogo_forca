import random

palavras = [
    'abacate', 'abacaxi', 'abelha', 'abobora', 'abrigo', 'absoluto', 'academia', 'açucar', 'adesivo', 'advogado',
    'aeromoça', 'água', 'agulha', 'aipo', 'alegria', 'alface', 'algodão', 'aliado', 'alicate', 'almoço',
    'aluno', 'amarelo', 'amigo', 'amor', 'anel', 'anjo', 'antena', 'apito', 'aplicativo', 'apontador',
    'aranha', 'arco', 'areia', 'arroz', 'aspirador', 'astronauta', 'atum', 'aula', 'avião', 'azeite',
    'bacia', 'bala', 'banco', 'banana', 'batata', 'bebê', 'beijo', 'bexiga', 'bicicleta', 'bigode',
    'biscoito', 'blusa', 'boia', 'bola', 'boneca', 'boneco', 'borboleta', 'borracha', 'brinquedo', 'broto',
    'cabelo', 'cabra', 'caderno', 'café', 'cama', 'caminhão', 'caneca', 'caneta', 'canguru', 'cão',
    'capivara', 'carne', 'carro', 'carta', 'casa', 'castelo', 'cavalo', 'cebola', 'celular', 'cesta',
    'chave', 'chuva', 'cinto', 'cola', 'colher', 'computador', 'corda', 'coruja', 'coração', 'copo',
    'cozinha', 'criança', 'cubo', 'cupom', 'dedo', 'desenho', 'dinheiro', 'docinho', 'doente', 'dragão'
]


class Forca:
    def __init__(self, palavra=random.choice(palavras)):
        self.palavra = palavra
        self.tentativas = len(self.palavra) + 5
        self.letras_certas = ''
        self.letras_erradas = ''

    def verificar_letra(self, letra):
        if letra in self.letras_certas or letra in self.letras_erradas:
            print("Você já tentou essa letra.")
            return

        if letra in self.palavra:
            print("Acertou!")
            self.letras_certas += letra
        else:
            print("Essa letra está incorreta.")
            self.tentativas -= 1
            self.letras_erradas += letra

    def mostrar(self):
        palavra_atual = ''.join([letra if letra in self.letras_certas else '_' for letra in self.palavra])
        print(f"Palavra :{palavra_atual}")
        print(f"Tentativas restantes: {self.tentativas}")
        print(f"Letras erradas: {', '.join(sorted(self.letras_erradas))}")

        if '_' not in palavra_atual:
            print("Parabéns! Você acertou a palavra!")
            exit()

        if self.tentativas == 0:
            print(f"Você perdeu a palavra era: {self.palavra}")
            exit()


print("JOGO DA FORCA")

jogo = Forca()
jogo.mostrar()

while True:
    escolha = input("Escolha uma letra para adivinhar a palavra: ").lower()

    if len(escolha) != 1 or not escolha.isalpha():
        print("Entrada inválida. Por favor, digite apenas uma letra.")
        continue

    jogo.verificar_letra(escolha)
    jogo.mostrar()
