import math

def es_triangulo_valido(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calcular_angulo(a, b, c):
    return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

def caracterizar_lados(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def caracterizar_angulos(ang1, ang2, ang3):
    if 90 in (ang1, ang2, ang3):
        return "Rectángulo"
    elif all(ang < 90 for ang in (ang1, ang2, ang3)):
        return "Acutángulo"
    else:
        return "Obtusángulo"

def main():
    print("Caracterización de un triángulo")
    
    # Ingresar los lados
    a = float(input("Ingrese el lado a: "))
    b = float(input("Ingrese el lado b: "))
    c = float(input("Ingrese el lado c: "))
    
    if not es_triangulo_valido(a, b, c):
        print("Los lados ingresados no forman un triángulo válido.")
        return
    
    # Calcular los ángulos
    ang1 = calcular_angulo(a, b, c)
    ang2 = calcular_angulo(b, c, a)
    ang3 = 180 - ang1 - ang2

    # Caracterizar triángulo
    tipo_lados = caracterizar_lados(a, b, c)
    tipo_angulos = caracterizar_angulos(ang1, ang2, ang3)

    # Mostrar resultados
    print(f"\nLados del triángulo: a = {a}, b = {b}, c = {c}")
    print(f"Ángulos del triángulo: {ang1:.2f}°, {ang2:.2f}°, {ang3:.2f}°")
    print(f"Tipo según lados: {tipo_lados}")
    print(f"Tipo según ángulos: {tipo_angulos}")

if __name__ == "__main__":
    main()
