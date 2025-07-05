menu= """

[1] Depositar
[9] Sacar
[0] Extrato
[Q] Sair

""" 

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

while True :
    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito foi: R${valor:.2f}"

        else: print("Operação falhou!")


    
    elif opcao == "9":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo =  valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saque = numeros_saques >= LIMITES_SAQUES
        
        if excedeu_saldo :
            print ("Operação falhou! Não tem saldo suficiente.")

        elif excedeu_limite :
            print("Operação falhou! Você excedeu limite.")

        elif excedeu_saque :
            print("Operação falhou! Numero de saques excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque R$ {valor:.2f}\n"
            numeros_saques += 1 
        else:
            print("Operação falhou! Valor não é valido")

    
    elif opcao == "0": 

        print("Não foi realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")

    elif opcao == "Q":
        break

    else: print("Operação invalida, porfavor selecione novamente a operação desejada.")