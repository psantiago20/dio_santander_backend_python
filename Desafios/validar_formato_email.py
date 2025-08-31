# Entrada do usuário
email = input().strip()

# Domínios permitidos
dominios_validos = ["gmail.com", "outlook.com"]

# Regra 1: contém '@'
tem_arroba = "@" in email

# Regra 2: não começa nem termina com '@'
posicao_valida = not email.startswith("@") and not email.endswith("@")

# Regra 3: sem espaços
sem_espaco = " " not in email

# Regra 4: domínio válido (parte depois do @)
dominio = email.split("@")[-1] if tem_arroba else ""
dominio_valido = dominio in dominios_validos

# Validação final
if tem_arroba and posicao_valida and sem_espaco and dominio_valido:
    print("E-mail válido")
else:
    print("E-mail inválido")
