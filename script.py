def agregar_ganancias(lista, ganancia):
    lista.append(ganancia)

def agregar_gastos(lista, gasto):
    lista.append(gasto)

def calcular_diferencia(ganancias, gastos):
    ganancia_total = sum(ganancias)
    gasto_total = sum(gastos)
    return ganancia_total - gasto_total

def ganancia_promedio(ganancias):
    return sum(ganancias) / len(ganancias) if ganancias else 0

def gasto_promedio(gastos):
    return sum(gastos) / len(gastos) if gastos else 0

def main():
    ganancias = []
    gastos = []

    option = -1
    while option != 0:
        print("ELIJA UNA OPCIÓN")
        print("----------------------")
        print("0. Salir")
        print("1. Ingresar ganancias")
        print("2. Ingresar gastos")
        print("3. Información sobre mi dinero")

        option = int(input())

        if option == 0:
            print("Saliendo del programa...")
        elif option == 1:
            ganancia = float(input("- Ingrese aquí sus ganancias -\n"))
            agregar_ganancias(ganancias, ganancia)
            print("Mis ganancias:", ganancias)
        elif option == 2:
            gasto = float(input("- Ingrese aquí sus gastos -\n"))
            agregar_gastos(gastos, gasto)
            print("Mis gastos:", gastos)
        elif option == 3:
            print("1. Historial de ganancias:", ganancias)
            print("2. Historial de gastos:", gastos)
            diferencia = calcular_diferencia(ganancias, gastos)
            print("3. Mi cartera:", diferencia)
            promedio_ganancias = ganancia_promedio(ganancias)
            print("4. Ganancia promedio:", promedio_ganancias)
            promedio_gastos = gasto_promedio(gastos)
            print("5. Gasto promedio:", promedio_gastos)
        else:
            print("Opción no válida. Por favor, elija una opción entre 0 y 3.")

if __name__ == "__main__":
    main()
