#Dados Conta Corrente
num_conta = 0
saldo_conta = 0

#Dados conta Poupança
num_poupanca = 0
saldo_poupanca = 0

#Limites para Saque
limite_saque = 3000 #limite por saque
limite_diario = 10000 #limite total de saques por dia

def criar_conta(tipo_conta,num,saldo):
  global num_conta,saldo_conta,num_poupanca,saldo_poupanca

  match tipo_conta:
    case 'c':
      num_conta = num
      saldo_conta = saldo
      print(f'A conta Corrente foi criada com o número {num_conta} e com saldo inicial R$ {saldo_conta}')
    case 'p':
      num_poupanca = num
      saldo_poupanca = saldo
      print(f'A conta Poupança foi criada com o número {num_poupanca} e com saldo inicial R$ {saldo_poupanca}')


def check_valor_positivo(valor):
  if valor <= 0:
    print('Valor inválido.')
    return False

  return True

def creditar(tipo_conta,valor):
  global saldo_conta,saldo_poupanca

  if check_valor_positivo(valor):
    match tipo_conta:
      case 'c':
        saldo_conta = saldo_conta + valor
      case 'p':
        saldo_poupanca = saldo_poupanca + valor

def debitar(tipo_conta,valor):
  global saldo_conta,saldo_poupanca

  if check_valor_positivo(valor):
    match tipo_conta:
      case 'c':
        if (saldo_conta >= valor):
          saldo_conta = saldo_conta - valor
        else: print('Saldo Insuficiente.')
      case 'p':
        if (saldo_poupanca >= valor):
          saldo_poupanca = saldo_poupanca - valor
        else: print('Saldo Insuficiente.')

def transferir(origem,destino,valor):
  match origem:
    case 'c':
      debitar('c',valor)
      creditar('p',valor)
    case 'p':
      debitar('p',valor)
      creditar('c',valor)

def saldo():
  return f'\nO saldo atual da Conta Corrente é R${saldo_conta} e da Popupança é {saldo_poupanca}'