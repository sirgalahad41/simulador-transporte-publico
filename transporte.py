# === Importación de librerías necesarias ===
import heapq
import random 


# === Paso 1: Definir la estructura del grafo ===
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.conexiones = {}  # nodo: [(vecino, peso)]

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.conexiones[nodo] = []

    def agregar_arista(self, origen, destino, peso):
        self.conexiones[origen].append((destino, peso))
        self.conexiones[destino].append((origen, peso))  # Asumimos grafo no dirigido

    def actualizar_peso(self, origen, destino, nuevo_peso):
        self.conexiones[origen] = [
            (d, nuevo_peso) if d == destino else (d, p)
            for d, p in self.conexiones[origen]
        ]
        self.conexiones[destino] = [
            (d, nuevo_peso) if d == origen else (d, p)
            for d, p in self.conexiones[destino]
        ]


# === Crear el grafo y nodos ===
grafo = Grafo()
obstaculos_definidos = {}  # Clave: (origen, destino), Valor: (tipo_obstaculo, factor)

# Crear 20 nodos numerados del 1 al 20
for i in range(1, 21):
    grafo.agregar_nodo(f"N{i}")

# Conexiones fijas y lógicas entre los nodos (ejemplo)
# Esto es solo una estructura base, se puede ajustar luego según el diseño de ciudad
grafo.agregar_arista("N1", "N2", 5)
grafo.agregar_arista("N2", "N3", 4)
grafo.agregar_arista("N3", "N4", 6)
grafo.agregar_arista("N4", "N5", 7)
grafo.agregar_arista("N5", "N6", 3)
grafo.agregar_arista("N6", "N7", 5)
grafo.agregar_arista("N7", "N8", 4)
grafo.agregar_arista("N8", "N9", 6)
grafo.agregar_arista("N9", "N10", 2)

# Segunda ruta que conecta con la primera en distintos puntos
grafo.agregar_arista("N1", "N11", 4)
grafo.agregar_arista("N11", "N12", 5)
grafo.agregar_arista("N12", "N6", 6)
grafo.agregar_arista("N12", "N13", 3)
grafo.agregar_arista("N13", "N14", 4)
grafo.agregar_arista("N14", "N15", 5)
grafo.agregar_arista("N15", "N10", 6)

# Últimos nodos que conectan a la red existente
grafo.agregar_arista("N16", "N4", 7)
grafo.agregar_arista("N17", "N13", 3)
grafo.agregar_arista("N18", "N8", 5)
grafo.agregar_arista("N19", "N15", 4)
grafo.agregar_arista("N20", "N16", 6)

# Mostrar conexiones como verificación visual
for nodo in grafo.conexiones:
    print(f"{nodo}: {grafo.conexiones[nodo]}")

# === Paso 2: Implementar algoritmo de ruta más corta (Dijkstra) ===
def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo.nodos}
    previos = {nodo: None for nodo in grafo.nodos}
    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo.conexiones[nodo_actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias, previos


# === Función para reconstruir la ruta más corta ===
def obtener_ruta(previos, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.insert(0, actual)
        actual = previos[actual]
    return ruta


# === Paso 3: Mostrar resultados del recorrido / Interfaz básica por consola ===
def consultar_ruta(grafo, obstaculos_definidos):
    print("\n=== Consulta de Ruta ===")
    print(f"Nodos disponibles: {', '.join(sorted(grafo.nodos))}")
    origen = input("Ingrese nodo de origen (ej: N1): ").strip()
    destino = input("Ingrese nodo de destino (ej: N10): ").strip()

    if origen not in grafo.nodos or destino not in grafo.nodos:
        print("❌ Nodo inválido. Intente de nuevo.")
        return

    distancias, previos = dijkstra(grafo, origen)
    ruta = obtener_ruta(previos, destino)

    if not ruta or distancias[destino] == float("inf"):
        print("🚫 No hay una ruta posible entre esos nodos.")
        return


    mostrar_resultado_con_obstaculos(grafo, ruta, distancias[destino], obstaculos_definidos)



# === Paso 4: Función para agregar obstáculos definidos por el usuario ===
def agregar_obstaculo_manual(obstaculos_definidos):
    print("\n=== Agregar Obstáculo Manual ===")
    origen = input("Ingrese nodo origen del tramo (ej: N1): ").strip()
    destino = input("Ingrese nodo destino del tramo (ej: N2): ").strip()

    print("Tipos de obstáculos disponibles:")
    print("1. Semáforo rojo (+30%)")
    print("2. Accidente (+150%)")
    print("3. Congestión vehicular (+80%)")
    print("4. Reparaciones (+100%)")

    tipo_opcion = input("Seleccione tipo de obstáculo (1-4): ").strip()

    tipos = {
        "1": ("semaforo rojo", 0.3),
        "2": ("accidente", 1.5),
        "3": ("congestion vehicular", 0.8),
        "4": ("reparaciones", 1.0),
    }

    if tipo_opcion not in tipos:
        print("❌ Tipo inválido.")
        return

    obstaculo, factor = tipos[tipo_opcion]
    obstaculos_definidos[(origen, destino)] = (obstaculo, factor)
    obstaculos_definidos[(destino, origen)] = (obstaculo, factor)  # Para grafos no dirigidos

    print(f"✅ Obstáculo '{obstaculo}' agregado entre {origen} y {destino}.")

def mostrar_resultado_con_obstaculos(grafo, ruta, tiempo_base, obstaculos_definidos):
    print("\n📍 Ruta más corta encontrada:")
    print(" -> ".join(ruta))
    print(f"🧭 Número de segmentos recorridos: {len(ruta) - 1}")
    print("\n🔍 Segmentos con obstáculos definidos:")

    tiempo_total = 0

    for i in range(len(ruta) - 1):
        nodo_actual = ruta[i]
        siguiente_nodo = ruta[i + 1]

        # Buscar peso base
        peso_tramo = next(
            (p for v, p in grafo.conexiones[nodo_actual] if v == siguiente_nodo),
            None
        )
        if peso_tramo is None:
            continue

        # Revisar si hay obstáculo en este tramo
        clave = (nodo_actual, siguiente_nodo)
        if clave in obstaculos_definidos:
            obstaculo, factor = obstaculos_definidos[clave]
            retraso = peso_tramo * factor
            tiempo_total += peso_tramo + retraso
            print(f" - {nodo_actual} -> {siguiente_nodo}: {peso_tramo} min ⛔ +{retraso:.1f} min por {obstaculo}")
        else:
            tiempo_total += peso_tramo
            print(f" - {nodo_actual} -> {siguiente_nodo}: {peso_tramo} min")

    print(f"\n🕒 Tiempo estimado sin obstáculos: {tiempo_base:.1f} minutos")
    print(f"⏱️  Tiempo estimado con obstáculos: {tiempo_total:.1f} minutos\n")



# === Paso 5: Función para recalcular ruta si hay cambios ===
def recalcular_ruta(grafo, inicio, fin):
    # Copia del grafo original con pesos actualizados según los obstáculos
    grafo_temporal = Grafo()
    grafo_temporal.nodos = grafo.nodos.copy()

    for nodo in grafo.nodos:
        grafo_temporal.conexiones[nodo] = []

    for nodo in grafo.conexiones:
        for vecino, peso in grafo.conexiones[nodo]:
            clave = (nodo, vecino)
            if clave in obstaculos_definidos:
                obstaculo, factor = obstaculos_definidos[clave]
                nuevo_peso = peso + (peso * factor)
            else:
                nuevo_peso = peso

            # Para evitar duplicar aristas en grafo no dirigido
            if (vecino, nodo) not in grafo_temporal.conexiones or \
               all(v != nodo for v, _ in grafo_temporal.conexiones[vecino]):
                grafo_temporal.conexiones[nodo].append((vecino, nuevo_peso))

    distancias, previos = dijkstra(grafo_temporal, inicio)
    ruta = obtener_ruta(previos, fin)

    if not ruta or distancias[fin] == float('inf'):
        print("🚫 No hay una ruta posible con los obstáculos actuales.")
    else:
        print("\n🔁 Ruta recalculada con obstáculos aplicados:")
        mostrar_resultado_con_obstaculos(grafo, ruta, distancias[fin], obstaculos_definidos)


# === Paso 6: Menú de usuario (interfaz de consola) ===
def mostrar_menu():
    print("\n=== MENÚ DEL SIMULADOR DE TRANSPORTE ===")
    print("1. Mostrar conexiones del grafo")
    print("2. Consultar ruta más corta entre dos nodos")
    print("3. Agregar obstáculos y recalcular ruta")
    print("4. Salir")


def ejecutar_menu():
    origen_guardado = None
    destino_guardado = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            print("\n📌 Conexiones actuales del grafo:")
            for nodo in sorted(grafo.conexiones):
                conexiones = grafo.conexiones[nodo]
                for vecino, peso in conexiones:
                    if nodo < vecino:
                        print(f" - {nodo} ↔ {vecino}: {peso} min")

        elif opcion == "2":
            print("\n=== Consulta de Ruta ===")
            nodos_disponibles = sorted(grafo.conexiones.keys())
            print("Nodos disponibles:", ", ".join(nodos_disponibles))
            origen = input("Ingrese nodo de origen (ej: N1): ").strip()
            destino = input("Ingrese nodo de destino (ej: N10): ").strip()

            if origen not in grafo.conexiones or destino not in grafo.conexiones:
                print("❌ Uno de los nodos ingresados no existe.")
                continue

            recalcular_ruta(grafo, origen, destino)
            
            # Ahora sí, guardamos el origen y destino reales usados
            origen_guardado = origen
            destino_guardado = destino

        elif opcion == "3":
            if not origen_guardado or not destino_guardado:
                print("❗ Debes consultar primero una ruta (Opción 2) para usar esta función.")
                continue

            agregar_obstaculo_manual(obstaculos_definidos)
            recalcular_ruta(grafo, origen_guardado, destino_guardado)

        elif opcion == "4":
            print("👋 Saliendo del simulador...")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")



# === Paso 7: Ejecución principal ===
if __name__ == "__main__":
    ejecutar_menu()

     
