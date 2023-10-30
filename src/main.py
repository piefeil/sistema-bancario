menu = f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_atual = float(input("Insira o saldo atual: ")) 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3 

while True:



    opcao = input(menu)

    if opcao.lower() == "d":
        print("\nDepósito")

        valor_deposito = float(input("\nInsira o valor que será depositado: "))


        if valor_deposito > 0:
            saldo_atual += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("\nSaldo atualizado na conta: R$ %.2f" %(saldo_atual))

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    

    elif opcao.lower() == "s":
        print("\nSaque")

        valor_saque = float(input("\nInsira o valor que será sacado: "))


        if numero_saques >= LIMITE_SAQUES:
            print("\nLimite de", LIMITE_SAQUES, "saques diários atingido!")

        elif valor_saque > saldo_atual:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        
        elif valor_saque > limite:
            print("\nOperação falhou! O valor do saque excede o limite de R$ %.2f" %(limite))

        elif valor_saque > 0:
            numero_saques += 1
            saldo_atual -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print("\nSaldo atualizado na conta: R$ %.2f" %(saldo_atual))



    elif opcao.lower() == "e":
        print("\nExtrato")

        print(f"\n=============== EXTRATO ===============")
        print()
        print(f"Não foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo_atual:.2f}")
        print(f"=======================================")


    
    elif opcao.lower() == "q":
        print("\nSaindo...")
        break
    
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
