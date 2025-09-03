from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Lista de acertijos
acertijos = [
    {"pregunta": "Entre mar y palmeras, sol y arena, caminamos juntos y reímos sin pena.¿Dónde estábamos disfrutando la brisa y la vista serena?", 
     "respuesta": "vallarta", "imagen": "imagenes/vallarta.jpg"},
    {"pregunta": "Entre plata y callecitas empedradas, tomamos fotos y exploramos fachadas.¿En qué lugar subimos y bajamos cada subida y escalera cansada?", 
     "respuesta": "taxco", "imagen": "imagenes/taxco.jpg"},
    {"pregunta": "Isla caribeña, sin coches, solo arena, con un sol que se despide en escena serena. Mientras la noche caía, una rebanada de un manjar redondo compartimos, ¿dónde fue este mágico atardecer que vivimos?", 
     "respuesta": "holbox", "imagen": "imagenes/holbox.jpg"},
    {"pregunta": "Con harina, salsa y queso, hicimos algo con mucho progreso.¿Qué fue lo que hicimos con tanto sabor y esfuerzo?", 
     "respuesta": "pizzas", "imagen": "imagenes/pizza.jpg"},
    {"pregunta": "Soy ciudad virreinal,con túneles y un callejón sin igual. Mis casas de colores y un beso escondido,¿adivinas dónde hemos estado y dónde nos hemos atrevido?", 
     "respuesta": "guanajuato", "imagen": "imagenes/c_beso.jpg"},
]

codigo_correcto = ["vallarta", "taxco", "holbox", "pizzas", "guanajuato"]

@app.route("/")
def inicio():
    session["index"] = 0
    session["respuestas"] = []
    return render_template("inicio.html")

@app.route("/juego", methods=["GET", "POST"])
def juego():
    index = session.get("index", 0)
    respuestas = session.get("respuestas", [])

    if request.method == "POST":
        respuesta = request.form["respuesta"].strip().lower()
        respuestas.append(respuesta)
        session["respuestas"] = respuestas
        session["index"] = index + 1
        return redirect(url_for("juego"))

    if index < len(acertijos):
        return render_template("juego.html", 
                               pregunta=acertijos[index]["pregunta"],
                               imagen=acertijos[index]["imagen"])
    else:
        return redirect(url_for("final"))

@app.route("/final")
def final():
    respuestas = session.get("respuestas", [])
    if respuestas == codigo_correcto:
        return render_template("final.html", exito=True, codigo="309")
    else:
        return render_template("final.html", exito=False)

if __name__ == "__main__":
    app.run(debug=True)

