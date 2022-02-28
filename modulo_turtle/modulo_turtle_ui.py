import turtle
import modulo_turtle as geo
import modulo_turtle_colores as col

print("Bienvenido, usario.\n¿Qué figura desea crear?")
print("Las figuras disponibles son:\n(1) Cuadrado\n(2) Rectángulo\n(3) Rombo\n(4) Hexágono\n(5) Triángulo\n(6) Paralelogramo\n(7) Círculo")
fig = int(input("Ingrese el número de la figura que desea crear: "))

print("\nLos colores disponibles son:\n(1) Rojo\n(2) Verde\n(3) Amarillo\n(4) Azul")
a = int(input("¿Qué color desea?: "))
#print(a)
color = col.color_hex(a)
#print(color)

if fig == 1:
    lado = int(input("¿Qué longitud desea?: "))
    geo.cuadrado(lado, color)
elif fig == 2:
    b = int(input("¿Qué longitud de base desea?: "))
    h = int(input("¿Qué longitud de altura desea?: "))
    geo.rect(b, h, color)
elif fig == 3:
    lado = int(input("¿Qué longitud desea?: "))
    geo.rombo(lado, color)
elif fig == 4:
    lado = int(input("¿Qué longitud desea?: "))
    geo.hexa(lado, color)
elif fig == 5:
    lado = int(input("¿Qué longitud desea?: "))
    geo.trg(lado, color)
elif fig == 6:
    b = int(input("¿Qué longitud de base desea?: "))
    h = int(input("¿Qué longitud de altura desea?: "))
    geo.para(b, h, color)
elif fig == 7:
    r = int(input("¿Qué radio desea?: "))
    geo.circ(r, color)
else:
    print("Por favor, ingrese una de las opciones disponibles.")