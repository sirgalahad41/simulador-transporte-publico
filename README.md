# Simulador de Red de Transporte Público

## Descripción del Proyecto/funcionalidades 
Este proyecto consiste en la simulación de una red de transporte público en una ciudad pequeña utilizando **Python**. Se construyó un grafo ponderado para representar 20 nodos conectados por rutas con tiempos específicos de recorrido. El objetivo es encontrar rutas óptimas entre dos puntos, calcular tiempos de llegada y adaptarse a cambios en condiciones del tráfico como trancones, semáforos o accidentes.

Este proyecto fue desarrollado como parte del curso de **Estructura de Datos Aplicados**.

las funcionalidades que se pretendian y se lograron aplicar a este codigo son 

1. simular un esquema de nodos y aristas (20) que representen una ciudad y sus calles 
2. darle pesos a las aristas que sepresente en minutos el tiempo que se tarda de ir de un nodo a otro, y con esto calcular el tiempo general del recorrido
3. repetir el paso anterior varias veces buscando todos los caminos posibles y encontrar el camino mas corto, mostrando ademas cada nodo recorrido, y el tiempo final y separado de cada nodo
4. en base al recorrido mas corto poder añadir obstaculos en el camino simulando uan situacion real donde algun contratiempo pueda alterar el tiempod e recorrido, eligiendo en que arista poner un obstaculo y de que clase
5. que el programa tras detectar un obstaculo recalcule la ruta y verifique si sigue siendo la ruta mas corta de lo contrario señalar la nueva ruta mas corta

estas funciones fueron pensadas para simular lo que podria ser una situacion real, no pretenden ser 100% similares pero si uan aproximacion 

### Lenguaje utilizado:
- Python 3.x  
- No se utilizó ningún framework externo.

---

## Requisitos para la instalación

- Tener instalado Python 3.x
- (Opcional) Instalar Git si se desea clonar el repositorio directamente

---

## prueba del codigo 

si usted ya a intalado correctamente el codigo en su dispositivo esta sera una guia detallada y precisa de como usar las funcionalidades presentes del codigo 

1. primero debe poner a correr el programa, si todo esta correcto le paracerea un menu directamente en el temrinal el cual sera este:
   === MENÚ DEL SIMULADOR DE TRANSPORTE ===
1. Mostrar conexiones del grafo
2. Consultar ruta más corta entre dos nodos
3. Agregar obstáculos y recalcular ruta
4. Salir
Seleccione una opción (1-4):

2. con el menu ya desplegado debe escribis en su teclado una de las opciones disponibles, aunque el correcto procedimiento seria primero elegir la opcion 2

3. al elegir la opcion 2 se le desplegara este nuevo menu 
=== Consulta de Ruta ===
Nodos disponibles: N1, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19, N2, N20, N3, N4, N5, N6, N7, N8, N9
Ingrese nodo de origen (ej: N1):

en este menu usted elegira cual es el nodo origen de donde empezara el recorrido, debe poner especificamente las siglas "N" seguidas de un numero entero del 1 al 20, luego al darle enter, le pedira escojerel destino a donde ira el recorrido, debe hacerse de la misma forma, "N" seguido del numero del nodo, tras esto debera darle enter y en la terminal se mostrara los resultados un ejemplo, suponiendo que escojio el nodo N2 como origen y el nodo N9 como destino, este sera el resultado:

=== Consulta de Ruta ===
Nodos disponibles: N1, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19, N2, N20, N3, N4, N5, N6, N7, N8, N9
Ingrese nodo de origen (ej: N1): N2
Ingrese nodo de destino (ej: N10): N9

🔁 Ruta recalculada con obstáculos aplicados:

📍 Ruta más corta encontrada:
N2 -> N1 -> N11 -> N12 -> N13 -> N14 -> N15 -> N10 -> N9
🧭 Número de segmentos recorridos: 8

🔍 Segmentos con obstáculos definidos:
 - N2 -> N1: 5 min
 - N1 -> N11: 4 min
 - N11 -> N12: 5 min
 - N12 -> N13: 3 min
 - N13 -> N14: 4 min
 - N14 -> N15: 5 min
 - N15 -> N10: 6 min
 - N10 -> N9: 2 min

🕒 Tiempo estimado sin obstáculos: 34.0 minutos
⏱️  Tiempo estimado con obstáculos: 34.0 minutos

4: tras esto ahora si podremos hacer uso de la funcion numero 3, la cual si no se a cargado una ruta previamente no funcionara, por lo que es obligatorio primero usar la funcion 2 antes que la 3, al elegir la opcion 3 se desplegara este menu:

=== Agregar Obstáculo Manual ===
Ingrese nodo origen del tramo (ej: N1):

en este menu se le pide al usuario que escoja el nodo inicial donde estara unicado el obstaculo, la respuesta del usuario debe seguir la misma logica, "N" seguido de un numero entero entre 1 al 20, tras darle enter, se pedira al usuario que escoja el nodo final, 

NOTA: esta parte es muy importante pues solo se asiganara la funcion de obstaculos a nodos que esten conectados directamente osea que si se escojio como origen el nodo N3 y como fianl el nodo N8 estos tiene que estar conectados directamente para poder aplicarse el obstaculo, en cambio si para llegar de uno al otro hay que pasar antes por otro nodo no se aplicara el obstaculo 

al elegir los nodos donde estar el obstaculo se desplegara este menu:

Tipos de obstáculos disponibles:
1. Semáforo rojo (+30%)
2. Accidente (+150%)
3. Congestión vehicular (+80%)
4. Reparaciones (+100%)
Seleccione tipo de obstáculo (1-4):

al elegir una de estas opciones se recalculara el peso de la arista que une a ambos nodos o lo que es lo mismo, aumentara el tiempo del recorrido de ese tramo lo que afectara el tiempo total de recorrido, al hacer esto el rpograma vovlera a recalcular la ruta y si hay una ruta mas corta en base al nuevo tiempo con el obstaculo, este reconocera a la nueva ruta mas corta y la reemplazara (en caso de que exista)

NOTA: la opcion numero 3 funciona gracias a que la opcion 2 guarda las cordenadas y tiempos del recorrido, las cuales permanecen siempre como las principales hasta que se vuelva  ejecutar la opcion 2 del menu principal, asi tambien funciona el guardado de la opcion numero 3 

EXTRA: las funciones 1 y 4 del menu principal son idependientes de las demas, y estas cumpliran siempre su tarbajo auqnue este no afecte en nada a las funciones 2 y 3, la funcion 1 mostrara el mapa de la ciudad, las conexiones de los nodos y el peso de las aristas representando los minutos, la opcion 4 cierra el programa

## Instrucciones de instalación y ejecuciónd 

1. Clonar el repositorio:
```bash
git clone https://github.com/sirgalahad41/simulador-transporte-publico
cd transporte

2. o si prefiere puede descargar el codigo directamente de la pagina de git, este correra con normalidad en cualquier entorno adaatado para phyton





