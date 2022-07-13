print(
    "2. Una concordancia es una lista alfabética de las palabras presentes en un texto o"
    + "\ntextos, con un recuento del número de veces que aparece la palabra."
    + "\nSu programa de concordancia debe incluir los siguientes pasos:"
)
print("")

phrase = input("Por favor, ingrese el texto a analizar: ")

print("\nb. Divida la oración en palabras individuales (puede usar split())")
words = phrase.split(" ")
print(f"Frase dividida en palabras: {words}")

print(
    "\nc. Genere una lista de todas las palabras en la oración y la cantidad de veces que ocurren. (counter )."
)

# Create Dictionary with words and times repeated
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

# Show the list of words and the times it is repeated
for key, value in counter.items():
    print(f"{key}: {value}")

print("\nd. Produzca una lista alfabética de las palabras con sus cantidades.")
print("e. Imprima la lista ordenada alfabéticamente.")
print(
    f"Lista ordenada alfabeticamente y sus cantidades: {sorted(counter, key = lambda x: x[0])}"
)
