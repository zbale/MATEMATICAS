function esTrianguloValido(a, b, c) {
    return a + b > c && a + c > b && b + c > a;
}

function calcularAngulo(a, b, c) {
    return (Math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 180) / Math.PI;
}

function caracterizarLados(a, b, c) {
    if (a === b && b === c) return "Equilátero";
    if (a === b || a === c || b === c) return "Isósceles";
    return "Escaleno";
}

function caracterizarAngulos(ang1, ang2, ang3) {
    if (ang1 === 90 || ang2 === 90 || ang3 === 90) return "Rectángulo";
    if (ang1 < 90 && ang2 < 90 && ang3 < 90) return "Acutángulo";
    return "Obtusángulo";
}

function calcularTriangulo() {
    let a = parseFloat(document.getElementById("A").value);
    let b = parseFloat(document.getElementById("B").value);
    let c = parseFloat(document.getElementById("C").value);

    if (isNaN(a) || isNaN(b) || isNaN(c)) {
        alert("Por favor, ingresa valores numéricos válidos.");
        return;
    }

    if (!esTrianguloValido(a, b, c)) {
        alert("Los lados ingresados no forman un triángulo válido.");
        return;
    }

    let ang1 = calcularAngulo(a, b, c);
    let ang2 = calcularAngulo(b, c, a);
    let ang3 = 180 - ang1 - ang2;

    let tipoLados = caracterizarLados(a, b, c);
    let tipoAngulos = caracterizarAngulos(ang1, ang2, ang3);

    document.getElementById("tipo_lados").textContent = `Tipo de triángulo: ${tipoLados}`;
    document.getElementById("tipo_angulos").textContent = `Tipo de triángulo (ángulos): ${tipoAngulos}`;
    document.getElementById("angulos").textContent = `Ángulos del triángulo: ${ang1.toFixed(2)}°, ${ang2.toFixed(2)}°, ${ang3.toFixed(2)}°`;

    let imgSrc = "";
    if (tipoLados === "Equilátero") {
        imgSrc = "imagenes/equilatero.png";
    } else if (tipoLados === "Isósceles") {
        imgSrc = "imagenes/isosceles.png";
    } else {
        imgSrc = "imagenes/escaleno.png";
    }

    document.getElementById("modalTriangleImage").src = imgSrc;
    abrirModal();
}

function abrirModal() {
    document.getElementById("modal").style.display = "flex";
}

function cerrarModal() {
    document.getElementById("modal").style.display = "none";
}
