# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"
)
print(arquivo.read())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"
)
print(arquivo.readline())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"
)
print(arquivo.readlines())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
