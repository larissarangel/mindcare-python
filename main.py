import datetime

def salvar_emocao(texto):
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("dados.txt", "a") as f:
        f.write(f"{data} - {texto}\n")

def registrar():
    emocao = input("Digite como você está se sentindo: ")
    salvar_emocao(emocao)
    print("Registro salvo com sucesso!\n")

def listar():
    try:
        with open("dados.txt", "r") as f:
            print("\nHistórico de emoções:")
            print(f.read())
    except:
        print("Nenhum registro encontrado.\n")

def dicas():
    lista = [
        "Respire fundo por alguns minutos",
        "Evite excesso de redes sociais",
        "Pratique atividade física leve",
        "Durma bem",
        "Converse com alguém de confiança"
    ]
    print("\nDicas de bem-estar:")
    for d in lista:
        print("-", d)
    print()

def menu():
    while True:
        print("=== MINDCARE ===")
        print("1 - Registrar emoção")
        print("2 - Ver histórico")
        print("3 - Dicas")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            registrar()
        elif op == "2":
            listar()
        elif op == "3":
            dicas()
        elif op == "4":
            break
        else:
            print("Opção inválida\n")

menu()
