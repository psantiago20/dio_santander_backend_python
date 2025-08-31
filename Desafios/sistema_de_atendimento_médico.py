# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
ordem_de_status = {"urgente": 0, "normal": 1}
pacientes.sort(key=lambda p: (ordem_de_status.get(p[2], 99), -p[1]))

# TODO: Exiba a ordem de atendimento com título e vírgulas:
nomes = [p[0] for p in pacientes]
print("Ordem de Atendimento:", ", ".join(nomes))
