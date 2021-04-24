import random as r

filas = []
class fila:
    def __init__(self,nome):
        self.nome = nome

        self.clientes_na_fila = []
        self.tamanho = len(self.clientes_na_fila)
        filas.append(self)
        self.clientes_atendidos = 0


class cliente:
    def __init__(self):
        self.fila = 0
        # Cada cliente tem um problema que demora de 5 a 15 minutos para ser solucionado.
        tempo_de_atendimento_necessario = r.randint(5, 15)
        # Tempo que ele precisa para ser completamente atendido
        self.tempo_de_atendimento_necessario = tempo_de_atendimento_necessario
        # Tempo que ele ficou sendo atendido
        self.tempo_de_atendimento = 0
        self.tempo_fila = 0
        self.posicao = 0

        print("Foi criado um cliente ")

tempos_de_fila = []

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
def atender(fila):
    if fila.tamanho >0 :
        fila.clientes_na_fila[0].tempo_de_atendimento = fila.clientes_na_fila[0].tempo_de_atendimento + 1
        if fila.clientes_na_fila[0].tempo_de_atendimento == fila.clientes_na_fila[0].tempo_de_atendimento_necessario:
            print(f"Um cliente da {fila.nome} foi atendido")
            fila.clientes_atendidos += 1
            tempos_de_fila.append(fila.clientes_na_fila[0].tempo_fila)
            fila.clientes_na_fila.pop(0)
            fila.tamanho = fila.tamanho - 1

def media_tempo_de_fila():
    total = 0
    for i in range(len(tempos_de_fila)):
        total = total + tempos_de_fila[i]
    media_tempo = total / len(tempos_de_fila)
    return media_tempo


# Inicializando as duas filas e o lobby
# È preciso inicializar as filas com o nome fila(X) onde X é o número da fila
fila1 = fila("fila 1")
fila2 = fila("fila 2")
lobby = []

# Funcionamento da loja
while True:
    tempo_de_funcionamento = int(input("Digite a duração de funcionamento da loja (em minutos) = "))
    while tempo_de_funcionamento > 0 or fila1.tamanho > 0 or fila2.tamanho > 0:
        # Clientes entram na loja, alocadas no lobby (Número aleatório de 2 a 7)
        if tempo_de_funcionamento > 0:
            criarcliente()
        print(f"-- O tamanho da fila 1 é: {fila1.tamanho}, o da fila 2 é: {fila2.tamanho} e existem {len(lobby)} pessoas no lobby --")
        # Limpar o Lobby, alocar os clientes nas filas
        limparlobby(lobby)

        #  Retirar clientes atendidos
        atender(fila1)
        atender(fila2)
        # Atualizar tempo de fila de todos os clientes exceto o que está sendo atendido
        for i in range(1,len(fila1.clientes_na_fila)):
                 fila1.clientes_na_fila[i].tempo_fila = fila1.clientes_na_fila[i].tempo_fila + 1
        for i in range(1,len(fila2.clientes_na_fila)):
                 fila2.clientes_na_fila[i].tempo_fila = fila2.clientes_na_fila[i].tempo_fila + 1
        # Atualizar timer geral
        tempo_de_funcionamento = tempo_de_funcionamento - 1
    # Ao acabar o tempo é preciso perguntar se acabará o atendimento ou se serão dados mais minutos
    encerrar = input("Deseja encerrar o dia? (s/n)")
    if encerrar == "s" or "S" :
        break
# Mostrar quantos clientes cada atendente atendeu e o tempo médio de espera p cada fila
print(f"A Fila 1 atendeu: {fila1.clientes_atendidos} clientes")
print(f"A Fila 2 atendeu: {fila2.clientes_atendidos} clientes")
print(f"O tempo medio de atendimento foi de {media_tempo_de_fila()}")


