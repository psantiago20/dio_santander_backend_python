# while True:
#     opcao = int(input("Informe um número: "))

#     if opcao == 10:
#         break

#     print(opcao)

# for numero in range(100):
#     if numero == 12:
#         break
#     print(numero, end=" ")

# for numero in range(100):
#     if numero == 12:
#         continue
#     print(numero, end=" ")

# for numero in range(100):
#     if numero % 2 == 0:
#         continue
#     print(numero, end=" ")

# while True:
#     numero = int(input("Informe um número: "))

#     if numero % 2 == 0:
#         continue
#     if numero == 10:
#         break

#     print(numero)

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
