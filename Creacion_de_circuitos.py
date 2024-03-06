## Con este programa podemos crear un circuito electrico con una fuente, resistencias en serie y paralelo.
## Al final despues de ingresar los datos, el programa calcula la corriente y la resistencia total del circuito.

# Funcion para verificar el valor de la resistencia incluyendo sufijo.
import random
def verificar_resistencia(resistencia_usuario):
    resistencia_usuario = resistencia_usuario.upper()
    factor = 1 
    if resistencia_usuario.endswith('K'):
        factor = 1000
        resistencia_usuario = resistencia_usuario[:-1]
    elif resistencia_usuario.endswith('M'):
        factor = 1000000
        resistencia_usuario = resistencia_usuario[:-1]
    return float(resistencia_usuario) * factor

# Función para calcular la resistencia total en paralelo
def resistencia_en_paralelo(resistencias):
    total = 0
    for r in resistencias:
        total += 1 / r
    return 1 / total

# Función para imprimir una representación esquemática del circuito
def imprimir_circuito(fuente, resistencias):
    circuito = f"Fuente: (V{fuente})-->"
    for tipo, valor in resistencias:
        if tipo == "serie":
            circuito += f"-|-RS{valor}-|-"
        elif tipo == "paralelo":
            r1, r2 = valor
            circuito += f"-|-RP{r1}/{r2}-|-"
    circuito += "--(GND)"
    print(circuito)

# Función para configurar la resistencia con prefijos
def modificacion_valor(valor):
    if valor >= 1e6:
        return f"{valor / 1e6:.2f} Mega"
    elif valor >= 1e3:
        return f"{valor / 1e3:.2f} Kilo"
    elif valor >= 1e-3:
        return f"{valor * 1e3:.2f} mili"
    elif valor >= 1e-6:
        return f"{valor * 1e6:.2f} micro"
    else:
        return f"{valor:.2f}"

# Función principal
def main():
    # Input de valores
    valor_fuente = float(input("Por favor ingrese el valor de la fuente de voltaje: "))

    resistencias = []
    while True:
        tipo_resistencia = input("¿Agregar resistencia en serie (S), en paralelo (P), o cerrar circuito (C)? (S/P/C): ").lower()
        if tipo_resistencia == "s":
            valor_resistencia = verificar_resistencia(input("Ingrese el valor de la resistencia en serie (con sufijo K o M si es necesario): "))
            resistencias.append(("serie", valor_resistencia))
        elif tipo_resistencia == "p":
            valor_resistencia1 = verificar_resistencia(input("Ingrese el valor de la primera resistencia en paralelo (con sufijo K o M si es necesario): "))
            valor_resistencia2 = verificar_resistencia(input("Ingrese el valor de la segunda resistencia en paralelo (con sufijo K o M si es necesario): "))
            resistencias.append(("paralelo", (valor_resistencia1, valor_resistencia2)))
        elif tipo_resistencia == "c":
            break

    # Calcular resistencia total
    resistencia_total = 0
    for tipo, valor in resistencias:
        if tipo == "serie":
            resistencia_total += valor
        elif tipo == "paralelo":
            resistencia_total += resistencia_en_paralelo(valor)

    # Calcular tolerancia aleatoria entre -10% y 10%
    tolerancia = random.uniform(-0.10, 0.10)

    # Aplicar tolerancia a la resistencia total
    resistencia_total = resistencia_total + (resistencia_total* tolerancia)

    # Calcular corriente
    corriente = valor_fuente / resistencia_total

    # Imprimir resultados
    print("\nResistencia total del circuito:", modificacion_valor(resistencia_total), "Ohmios")
    print("Corriente resultante:", modificacion_valor(corriente), "Amperios")

    # Imprimir representación esquemática del circuito
    imprimir_circuito(valor_fuente, resistencias)
    print("Tolerancia aplicada:", f"{tolerancia * 100:.2f} %")

if __name__ == "__main__":
    main()
