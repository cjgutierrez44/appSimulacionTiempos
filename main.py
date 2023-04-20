import random

actividades = []
precio = 150000
unidadTiempo = "dias"
cantidadSimulaciones = 500

simulaciones = []

tiempoMinimo = 0
tiempoMaximo = 0

diferencia = 0

class Actividad:
	nombre = ""
	optimista = 0
	costoMinimo = 0
	pesimista = 0
	costoMaximo = 0
	simulacion = []

	def __init__(self, nombre, optimista, pesimista):
		self.nombre = nombre
		self.optimista = optimista
		self.costoMinimo = self.optimista * precio
		self.pesimista = pesimista
		self.costoMaximo = self.pesimista * precio
		self.simulacion = []
		for i in range(cantidadSimulaciones):
			self.simulacion.append(random.random( ) * (self.pesimista - self.optimista) + self.optimista)

class Intervalo:

	def __init__(self, letra, tiempoMinimo, tiempoMaximo):
		self.letra = letra
		self.tiempoMinimo = tiempoMinimo
		self.tiempoMaximo = tiempoMaximo
		self.costoMinimo = tiempoMinimo * precio
		self.costoMaximo = tiempoMaximo * precio
		self.cantidad = 0



actividades.append(Actividad("Identificación de requerimientos y Análisis de requisitos", 2, 5))
actividades.append(Actividad("Análisis de la viabilidad del proyecto", 1, 3))
actividades.append(Actividad("Diseño de la arquitectura del software y Diseño de la base de datos", 5, 8))
actividades.append(Actividad("Diseño de casos de uso y Diseño de interfaces de usaurio", 4, 6))
actividades.append(Actividad("Programación de módulos", 8, 10))
actividades.append(Actividad("Integración de módulos", 3, 5))
actividades.append(Actividad("Pruebas unitarias", 3, 5))
actividades.append(Actividad("Pruebas de integración", 5, 8))
actividades.append(Actividad("Pruebas de aceptación del usuario", 8, 11))
actividades.append(Actividad("Despliegue del software en producción y Configuración y personalización del software", 2, 4))
actividades.append(Actividad("Migración de datos", 1, 2))
actividades.append(Actividad("Resolución de problemas y Mejora continua del software", 7, 12))

for actividad in actividades:
	tiempoMinimo += actividad.optimista
	tiempoMaximo += actividad.pesimista

diferencia = tiempoMaximo - tiempoMinimo






print("ESTE PROYECTO SEPUEDE TARDAR ENTRE " + str(tiempoMinimo) + " Y " + str(tiempoMaximo) + " COSTANDO ENTRE $" + str(tiempoMinimo * precio) + " Y $" + str(tiempoMaximo * precio))


print("TIENE LAS SIGUIENTES ACTIVIDADES:")
for i in range(len(actividades)):
	print(str(i + 1) + ". " + actividades[i].nombre)
	print("\t"  + "SE TARDA ENTRE " + str(actividades[i].optimista) + " Y " + str(actividades[i].pesimista) + " " + unidadTiempo)
	print("\t" + "SUS SIMULACIONES SON LAS SIGUIENTES:")
	for j in range(cantidadSimulaciones):
		print("\t\t" + str(j + 1) + ": " + str(actividades[i].simulacion[j]) + " " + unidadTiempo + " Y COSTARIA $" + str(round(actividades[i].simulacion[j] * precio, 2)))

tamañoIntervalo = 2

intervalos = []

letra = 65
inicio = tiempoMinimo

if diferencia % 2 != 0:
	tamañoIntervalo = 1

for i in range(int(diferencia / tamañoIntervalo)):
	fin = inicio + tamañoIntervalo
	intervalo = Intervalo(chr(letra), inicio, fin)
	intervalos.append(intervalo)
	inicio = fin
	letra = letra + 1

	print(intervalo.letra + " ENTRE " + str(intervalo.tiempoMinimo) + " " + unidadTiempo + " $" + str(intervalo.costoMinimo) + " Y " + str(intervalo.tiempoMaximo) + " " + unidadTiempo + " $" + str(intervalo.costoMaximo))




for i in range(cantidadSimulaciones):
	tiempoSimulacion = 0
	for actividad in actividades:
		tiempoSimulacion += actividad.simulacion[i] 
	simulaciones.append(tiempoSimulacion)
	for intervalo in intervalos:
		if tiempoSimulacion >= intervalo.tiempoMinimo and tiempoSimulacion <= intervalo.tiempoMaximo:
			intervalo.cantidad += 1 

mayor = intervalos[0]
for intervalo in intervalos:
	if intervalo.cantidad > mayor.cantidad:
		mayor = intervalo
	print("intervalo " + intervalo.letra + " " + str(intervalo.cantidad) + " ==== " + str(round(intervalo.cantidad / cantidadSimulaciones * 100 , 2)) + "%")


print("LO MAS PROBABLE ES QUE USTED ENTREGUE SU PORYECTO ENTRE " + str(mayor.tiempoMinimo) + " " + unidadTiempo + " Y " + str(mayor.tiempoMaximo) + " " + unidadTiempo)
print("PUEDE COBRAR ENTRE $" + str(mayor.costoMinimo) + " Y $" + str(mayor.costoMaximo))
print("ES EL INTERVALO " + mayor.letra)




