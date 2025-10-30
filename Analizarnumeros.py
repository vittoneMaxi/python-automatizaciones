# archivo: analizar_numeros.py

ruta = "numeros.txt"

# 1) Leer el archivo robustamente
numeros = []
with open(ruta, "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        s = linea.strip()
        # Ignorar líneas vacías o comentarios (empiezan con #)
        if not s or s.startswith("#"):
            continue
        try:
            numeros.append(float(s))
        except ValueError:
            print(f"Aviso: línea {i} -> '{s}' no es numérica. La ignoro.")

# 2) Procesar cada número
for n in numeros:
    if n > 0:
        print(n, "es positivo")
    elif n < 0:
        print(n, "es negativo")
    else:
        print(n, "es cero")
