# main.py

from random import shuffle
from perguntas import mostrar_perguntas


def continuar_jogo(resp):
    while True:
        valor = input(resp).strip().upper()

        if valor in ['S', 'N']:
            return valor

        print("ERRO! DIGITE APENAS S OU N!")
        print()


def leia_string(resp):
    while True:
        valor = input(resp).strip().upper()

        if not valor:
            print("Digite algo pelo teclado!")
            print()
            continue

        if valor in ['A', 'B', 'C', 'D']:
            return valor

        print("ERRO: Digite apenas A, B, C ou D!")
        print()


def mostrar_respostas():

    while True:
        acertos = 0
        erros = 0

        quiz_python_ai = mostrar_perguntas()
        shuffle(quiz_python_ai)

        for indice, quiz in enumerate(quiz_python_ai):

            print("=" * 40)
            print(f"PERGUNTA {indice + 1}/{len(quiz_python_ai)}")
            print("=" * 40)
            print()

            print(quiz['pergunta'])
            print()

            for letra, texto in quiz['respostas']:
                print(f"{letra} - {texto}")

            print()
            print(f"RESPOSTAS CORRETAS: {acertos}")
            print(f"RESPOSTAS ERRADAS: {erros}")
            print()

            usuario = leia_string("Digite a sua resposta: ")

            print()

            if usuario == quiz['resposta']:
                print(f"USUÁRIO ACERTOU! A resposta é {quiz['resposta']}")
                acertos += 1

            else:
                for letra, texto in quiz['respostas']:
                    if letra == quiz['resposta']:
                        print(f"ERROU! A resposta correta era {letra} - {texto}")
                        erros += 1
                        break

            print()

        print("=" * 40)
        print("PONTUAÇÃO FINAL")
        print("=" * 40)

        pontuacao = (acertos / len(quiz_python_ai)) * 100

        if pontuacao > 80:
            print("Excelente desempenho!")

        elif 50 <= pontuacao <= 80:
            print("Bom desempenho!")

        else:
            print("Precisa revisar mais!")

        print()
        print(f"Taxa de acertos: {pontuacao:.1f}%")
        print(f"RESPOSTAS CORRETAS: {acertos}")
        print(f"RESPOSTAS ERRADAS: {erros}")
        print()

        resp = continuar_jogo("Quer continuar? [S/N] ")

        if resp == "N":
            print()
            print("Encerrando o jogo...")
            break


if __name__ == "__main__":
    mostrar_respostas()