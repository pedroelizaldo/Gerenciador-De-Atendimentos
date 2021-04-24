
from random import randint
from time import sleep
from datetime import datetime
import os

class fila:
  def __init__(self):
    #vetor cliente
    self.cliente = [" 🧍 "]
    #listas onde serão inserido os clientes
    self.fila1 = []
    self.fila2 = []
    #varivael que vai armazenar a data e hora do sistema
    self.hora_comeco = datetime.now()
    #dicionario que irá armazenar o horario de chegada e saida dos clientes
    self.horarios = {}
    #indentificador do cliente no dicionario dos horarios
    self.id_cliente = 1
  #função principal, tem a função de organizar o fluxo do programa
  def master(self):
    os.system("clear")
    #esse for por enquanto é apenas para teste
    for x in range(5):
      self.entrar_na_fila()
      self.status_das_filas()
      self.retarda_e_limpa()
    self.estatisticas()
  # essa função adiciona o cliente a fila
  def entrar_na_fila(self):
    # Essa variavel define a quantidade de clientes que vai chegar por minuto
    self.Q_chegada_cliente = randint(2,5)
    #variavel que vai armazenar a data e o horario do sistema 
    self.now = datetime.now()
    #chamada para a função
    self.verificar_tamanho_filas()
    print('''
                    ~~~~~~~~~~~~~~~~~~
                     \033[22mSTATUS DAS FILAS
                    ~~~~~~~~~~~~~~~~~~
    ''')
    #dependendo do valor da variavel "cupom" que foi definido na função "self.verificar_tamanho_filas()" o cliente será adicionado a fila1 ou fila2
    #o loop irá durar conforme a quantidade de clientes que vai chegar que é entre 2 e 7   
    for s in range(self.Q_chegada_cliente):
      if self.cupom == 1:
        self.fila1.append(self.cliente[0])
        #print(f'{self.inicio.minute} minutos e {self.inicio.second} segundos')
        self.armazenar_horario_chegada()
      elif self.cupom == 2:
        self.fila2.append(self.cliente[0])
        self.armazenar_horario_chegada()
  #Essa função é renposavel por printar as informações sobre as 2 filas, quantos clientes chegaram, a hora atual, e a hora dde chegada dos clientes 
  def status_das_filas(self):
    # As variaveis "self.inicio.hour","self.inicio.minute","self.inicio.second" variam da variavel "self.inicio" que recebeu "datetime.now()" dependendo da terminação da variavel ela pode retornar diferentes informações tais como: minute retorna hora; second retorna segundos e hour retorna hora
    print(
      f'''    
              {"_"*35}
              INICIO DAS ATIVIDADES {self.hora_comeco.hour}:{self.hora_comeco.minute}:{self.hora_comeco.second}
              {"_"*35}
              HORA ATUAL:{self.now.hour}:{self.now.minute}:{self.now.second}
              {"_"*35}
              Entraram {self.Q_chegada_cliente} clientes na {self.cupom}° fila
              {"~~~~~"*10+"~~~"*(len(self.fila1))}
              FILA 1 >>{self.fila1}
              {"~~~~~"*10+"~~~"*(len(self.fila1))}
              FILA 2 >>{self.fila2}
              {"~~~~~"*10+"~~~"*(len(self.fila1))}
{"x"*150}
              ''')
#Essa função verifica qual fila contém um menor numero de pessoas e passa essa informação atraves da variavel "self.cupom" que posteriormente será ultilizada para alocar os clientes na fila.
#Se a quantidade de pessoas nas filas forem iquais o valor da variavel será sorteada(ou 1 ou 2)
  def verificar_tamanho_filas(self):
    if len(self.fila1) < len(self.fila2):
      self.cupom = 1
    elif len(self.fila2) < len(self.fila1):
      self.cupom = 2
    elif len(self.fila2) == len(self.fila2):
      self.cupom = randint(1,2)
  #Essa função é responsavel por limpar o console e dar uma pausa na execução do código para que seja possivel acompanhar o fluxo e respeitar as definições passadas na proposta 
  def retarda_e_limpa(self):
    sleep(5)
    #os.system("clear") 
  # essa função é responsavel por arnazenar o horario de chegada do cliente
  def armazenar_horario_chegada(self):
    sleep(2)
    self.now = datetime.now()
    self.horario_chegada = (f"{self.now.hour}:{self.now.minute}:{self.now.second}")
    # aqui eu adiciono uma chave de nove cliente+id com o valor sendo o horario de chegada 
    self.horarios[f"Cliente[{self.id_cliente}]"] = self.horario_chegada
    # esse id é responsavel pela indentiicação do cliente sendo alterada a cada registro com 1 unidade
    self.id_cliente +=1
  # essa função se o usuario desejar printa os horarios de chegada de cada cliente
  def estatisticas(self):
    x = input("Deseja ver os horarios?[S/N]-> ").upper()
    if "S" in x:
      for m in self.horarios:
        print("~"*50)
        print(f'{m} chegou às: {self.horarios[m]}')
        sleep(0.5)
    else:
      print("Bye,Bye")
    
#instancio a classe fila com isso passo todas as funções da classe para a variavel
dany = fila()
# com a variavel "dany" possuindo todas as funções da classe fila eu posso chamar a função "master". 
dany.master()
