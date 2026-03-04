Aquí tienes el código limpio, sin comentarios y con una estructura directa para que lo uses en cualquier proyecto:

Python

def es_bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

def incrementar_dia(d, m, a):
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(a):
        dias_mes[2] = 29

    d += 1

    if d > dias_mes[m]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            a += 1

    return d, m, a

# Ejemplo de uso:
dia, mes, año = incrementar_dia(28, 2, 2024)
print(f"{dia}/{mes}/{año}")