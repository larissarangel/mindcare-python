import os
from datetime import datetime

ARQUIVO = "dados.txt"

emocoes = {
    "1": "😀 Muito feliz",
    "2": "🙂 Feliz",
    "3": "😐 Neutro",
    "4": "😔 Triste",
    "5": "😰 Ansioso"
}
dicas = {
    "😀 Muito feliz": "Continue valorizando os momentos positivos e compartilhe essa felicidade com pessoas importantes para você.",
    "🙂 Feliz": "Mantenha hábitos saudáveis que contribuam para o seu bem-estar físico e emocional.",
    "😐 Neutro": "Reserve alguns minutos para realizar uma atividade que lhe proporcione prazer, como ouvir música, ler ou caminhar.",
    "😔 Triste": "Lembre-se de que dias difíceis fazem parte da vida. Procure conversar com alguém de confiança e cuide de você.",
    "😰 Ansioso": "Respire profundamente, faça pausas quando necessário e concentre-se em realizar uma tarefa de cada vez."
}

def registrar_emocao():
    print("\n--- REGISTRAR EMOÇÃO ---")
    for k, v in emocoes.items():
        print(f"{k} - {v}")

    escolha = input("Escolha uma emoção (1 a 5): ")

    if escolha in emocoes:
        emocao = emocoes[escolha]

        comentario = input("Digite um comentário (opcional): ")

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{data_hora} - {emocao} | {comentario}\n")

        print(f"\nEmoção registrada: {emocao}")
        print("\n💡 Dica de bem-estar:")
        print(dicas[emocao])

        input("\nENTER para voltar ao menu...")
    else:
        print("Opção inválida!")
        input("\nENTER para voltar...")


def ver_historico():
    print("\n--- HISTÓRICO ---")

    if not os.path.exists(ARQUIVO):
        print("Nenhum dado encontrado.")
        input("\nENTER para voltar...")
        return

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum registro encontrado.")
        else:
            for linha in linhas:
                print(linha.strip())

    input("\nENTER para voltar...")


def estatisticas():
    print("\n--- ESTATÍSTICAS ---")
    contagem = {
        "😀 Muito feliz": 0,
        "🙂 Feliz": 0,
        "😐 Neutro": 0,
        "😔 Triste": 0,
        "😰 Ansioso": 0
    }

    if not os.path.exists(ARQUIVO):
        print("Nenhum dado encontrado.")
        input("\nENTER para voltar...")
        return

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(" - ")

            if len(partes) < 2:
                continue

            emocao_completa = partes[1]
            emocao = emocao_completa.split(" | ")[0]

            if emocao in contagem:
                contagem[emocao] += 1

    for emocao, total in contagem.items():
        print(f"{emocao}: {total}")

    input("\nENTER para voltar...")

def dicas_bem_estar():
    print("\n========================================")
    print("        💡 DICAS DE BEM-ESTAR")
    print("========================================")

    print("\n1. Mantenha uma rotina de sono adequada (7 a 9 horas por noite).")
    print("\n2. Hidrate-se regularmente durante o dia.")
    print("\n3. Pratique atividades físicas compatíveis com sua condição de saúde.")
    print("\n4. Faça pausas durante os estudos ou trabalho para descansar a mente.")
    print("\n5. Reserve momentos para lazer, convivência familiar e atividades que lhe tragam satisfação.")
    print("\n6. Busque manter uma alimentação equilibrada e hábitos saudáveis.")
    print("\n7. Caso emoções como tristeza ou ansiedade permaneçam por um longo período ou prejudiquem sua rotina, considere buscar orientação de um profissional de saúde.")

    input("\nENTER para voltar ao menu...")
   
def menu():
    while True:
        print("\n======================================")
        print("      🧠 MINDCARE")
        print(" Sistema de Monitoramento Emocional")
        print("======================================")
        print("1 - Registrar emoção")
        print("2 - Histórico")
        print("3 - Estatísticas")
        print("4 - Dicas de bem-estar")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            registrar_emocao()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            estatisticas()
        elif opcao == "4":
            dicas_bem_estar()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()
