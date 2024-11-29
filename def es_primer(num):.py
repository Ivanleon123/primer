def es_primer(num):
    """Comprova si un número és primer."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Llista per emmagatzemar números primers
numeros_prims = []

# Trobar números primers entre 1 i 100
for num in range(1, 101):
    if es_primer(num):
        numeros_prims.append(num)

# Imprimir els números primers
print("Números primers entre 1 i 100:", numeros_prims)
print("Total de números primers:", len(numeros_prims))