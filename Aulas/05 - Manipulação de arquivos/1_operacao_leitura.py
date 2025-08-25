arquivo = open("Aulas\lorem.txt", "r")
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())
# for linha in arquivo.readlines():
#     print(linha)

while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()
