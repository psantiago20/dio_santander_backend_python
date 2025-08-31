# Dicionário com os valores de desconto
descontos = {"DESCONTO10": 0.10, "DESCONTO20": 0.20, "SEM_DESCONTO": 0.00}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()


# TODO: Aplique o desconto se o cupom for válido:
if cupom == "DESCONTO10":
    cupom = 0.10
    preco_final = preco - (preco * cupom)
    print(f"{preco_final:.2f}")
elif cupom == "DESCONTO20":
    cupom = 0.20
    preco_final = preco - (preco * cupom)
    print(f"{preco_final:.2f}")
elif cupom == "SEM_DESCONTO":
    cupom = 0.00
    preco_final = preco - (preco * cupom)
    print(f"{preco_final:.2f}")
else:
    print(
        "Desconto não cadastrado favor seguir conforme abaixo:\nDESCONTO10': 0.10,\n 'DESCONTO20': 0.20,"
        "\n'SEM_DESCONTO': 0.00"
    )
