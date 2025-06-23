# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
# Loop para adicionar participantes do evento
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_virgula = linha.rfind(",")
    
    # Separa o nome do participante e o tema
    participantes = linha[:posicao_virgula]
    tema = linha[posicao_virgula + 1:]
    
    # Adiciona ao evento
    if tema not in eventos:
        eventos[tema] = []  # cria a lista se ainda não existir

    eventos[tema].append(participantes)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")