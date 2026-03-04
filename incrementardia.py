def incrementar_dias_remoto(d, m, a, n):
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for _ in range(n):
        if es_bisiesto(a):
            dias_mes[2] = 29
        else:
            dias_mes[2] = 28

        d += 1

        if d > dias_mes[m]:
            d = 1
            m += 1
            if m > 12:
                m = 1
                a += 1
                
    return d, m, a

# Ejemplo: Incrementar 40 días desde el 28/2/2024
dia, mes, año = incrementar_dias_remoto(28, 2, 2024, 40)
print(f"{dia}/{mes}/{año}")