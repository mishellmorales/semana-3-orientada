# Programación Tradicional

def ingresar_velocidades_diarias():
    velocidades = []
    for i in range(7):
        velocidad = float(input(f"Ingrese la velocidad del viento para el día {i + 1}: "))
        velocidades.append(velocidad)
    return velocidades

def calcular_promedio_semanal(velocidades):
    promedio = sum(velocidades) / len(velocidades)
    return promedio

def main():
    velocidades_diarias = ingresar_velocidades_diarias()
    promedio_semanal = calcular_promedio_semanal(velocidades_diarias)
    print(f"El promedio semanal de velocidades del viento es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()
