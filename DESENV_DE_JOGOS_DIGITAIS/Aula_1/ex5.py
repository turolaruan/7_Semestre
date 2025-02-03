lista = [2, 5, 7, -2, 8]

def analise(lista):
    media = sum(lista) / len(lista)
    mediana = sorted(lista)[len(lista) // 2]
    min_value = min(lista)
    max_value = max(lista)
    return (media, mediana, min_value, max_value)

print(analise(lista))