# Jogo da Forca

Este é um projeto em Python que simula o clássico jogo da Forca. O objetivo foi aplicar conceitos de **Programação Orientada a Objetos (POO)** para criar um jogo interativo e robusto, com um bom gerenciamento da lógica.

## 🛠️ Habilidades Demonstradas

* **Programação Orientada a Objetos (POO):** Uso de uma classe (`Forca`) para encapsular toda a lógica do jogo (palavra secreta, tentativas, letras certas/erradas) e os métodos para interagir com o usuário.
* **Controle de Fluxo e Loops:** Implementação de um loop `while` para manter o jogo em execução e condicionais para verificar o status de vitória ou derrota.
* **Manipulação de Strings:** O projeto utiliza fatiamento de strings e compreensão de lista para exibir a palavra com as letras corretas e os `_` nas posições das letras não adivinhadas.
* **Módulo `random`:** Uso da biblioteca `random` do Python para selecionar a palavra do jogo de forma aleatória a partir de uma lista pré-definida.
* **Validação de Entrada:** O código verifica se o usuário digitou uma única letra antes de processar a entrada, garantindo a integridade do jogo.

## 💡 Como Usar

1.  Clone este repositório para sua máquina local.
2.  Abra o arquivo `jogo_da_forca.py` em um terminal ou IDE (como PyCharm).
3.  Execute o script. O programa irá apresentar um menu de opções.
4.  Digite uma letra por vez para tentar adivinhar a palavra.
5.  O jogo continua até você adivinhar a palavra ou suas tentativas acabarem.
