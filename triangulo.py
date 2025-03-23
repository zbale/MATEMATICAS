import math
from browser import document, alert

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

def main(event=None):
    try:
        a = float(document["A"].value)
        b = float(document["B"].value)
        c = float(document["C"].value)

        if not es_triangulo_valido(a, b, c):
            alert("Los lados ingresados no forman un triangulo valido.")
            return

        ang1 = calcular_angulo(a, b, c)
        ang2 = calcular_angulo(b, c, a)
        ang3 = 180 - ang1 - ang2

        tipo_lados = caracterizar_lados(a, b, c)
        tipo_angulos = caracterizar_angulos(ang1, ang2, ang3)

        document["tipo_lados"].text = f"Tipo de triángulo según los lados: {tipo_lados}"
        document["tipo_angulos"].text = f"Tipo de triángulo según los ángulos: {tipo_angulos}"
        document["angulos"].text = f"Ángulos del triángulo: {ang1:.2f}°, {ang2:.2f}°, {ang3:.2f}°"

    except ValueError:
        alert("Por favor, ingresa valores numéricos validos.")