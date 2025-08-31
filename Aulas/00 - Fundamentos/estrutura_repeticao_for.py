# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()  # adiciona uma quebra de linha

# exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
