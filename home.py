from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio_1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad = int(request.form.get("cantidad"))

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        # Calcular descuento según edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        monto_descuento = int(total_sin_descuento * descuento)
        total_con_descuento = int(total_sin_descuento - monto_descuento)

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "monto_descuento": monto_descuento,
            "total_con_descuento": total_con_descuento
        }

    return render_template("ejercicio_1.html", resultado=resultado)


@app.route("/ejercicio_2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == "POST":
        usuario = request.form.get("usuario")
        clave = request.form.get("clave")

        if usuario in usuarios and clave == usuarios[usuario]:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template("ejercicio_2.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)