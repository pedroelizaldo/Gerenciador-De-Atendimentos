import random as r


class fila:
    def __init__(self):
        self.tamanho = 0
        self.clientes_na_fila = []


class cliente:
    def __init__(self):
        # Cada cliente tem um problema que demora de 5 a 15 minutos para ser solucionado.
        tempo_de_atendimento = r.randint(5, 15)
        self.fila = 0
        self.tempo_de_atendimento = tempo_de_atendimento
        self.tempo_fila = 0
        self.posicao = 0
        print("Foi criado um cliente ")


def alocar_cliente(cliente):
    if fila1.tamanho > fila2.tamanho:
        cliente.fila = 2
        fila2.tamanho = 1 + fila2.tamanho
        print("Cliente alocado na fila 2")
        fila2.clientes_na_fila.append(cliente)
        cliente.posicao = len(fila2.clientes_na_fila)
    else:
        cliente.fila = 1
        fila1.tamanho = fila1.tamanho + 1
        print("Cliente alocado na fila 1")
        fila1.clientes_na_fila.append(cliente)


def limparlobby(lobby):
    while len(lobby) > 0:
        alocar_cliente(lobby[0])
        lobby.pop(0)


def criarcliente():
    clientes_criados = r.randint(2, 7)
    for i in range(clientes_criados):
        lobby.append(cliente())




# Inicializando as duas filas e o lobby
fila1 = fila()
fila2 = fila()
lobby = []

# Funcionamento da loja
while True:
    tempo_de_funcionamento = int(input("Digite a duração de funcionamento da loja (em minutos) = "))
    while tempo_de_funcionamento > 0:
        # Clientes entram na loja, alocadas no lobby (Número aleatório de 2 a 7)
        criarcliente()
        print(f" O tamanho da fila 1 é:{fila1.tamanho}, o da fila 2 é: {fila2.tamanho} e existem {len(lobby)} pessoas no lobby")
        # Limpar o Lobby, alocar os clientes na fila
        limparlobby(lobby)

        #  Retirar clientes atendidos

         # Atualizar tempo de fila de todos os clientes
        for i in range(len(fila1.clientes_na_fila)):
                 fila1.clientes_na_fila[i].tempo_fila = fila1.clientes_na_fila[i].tempo_fila + 1
        for i in range(len(fila2.clientes_na_fila)):
                 fila2.clientes_na_fila[i].tempo_fila = fila2.clientes_na_fila[i].tempo_fila + 1
        # Atualizar timer geral
        tempo_de_funcionamento = tempo_de_funcionamento - 1
    # Ao acabar o tempo é preciso perguntar se acabará o atendimento ou se serão dados mais minutos
    encerrar = input("Deseja encerrar o dia? (s/n)")
    if encerrar == "s" or "S" :
        break




