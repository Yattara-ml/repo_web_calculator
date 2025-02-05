from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    if request.method == "POST":
        try:
            nombre1 = float(request.form["nombre1"])
            nombre2 = float(request.form.get("nombre2", 1))  # Utilisation de get avec une valeur par défaut
            operation = request.form["operation"]

            if operation == "addition":
                resultat = nombre1 + nombre2
            elif operation == "soustraction":
                resultat = nombre1 - nombre2
            elif operation == "multiplication":
                resultat = nombre1 * nombre2
            elif operation == "division":
                if nombre2 == 0:
                    resultat = "Division par zéro impossible"
                else:
                    resultat = nombre1 / nombre2
            elif operation == "carre":
                resultat = nombre1 ** 2
            elif operation == "racine":
                if nombre1 < 0:
                    resultat = "Racine d'un nombre négatif impossible"
                else:
                    resultat = math.sqrt(nombre1)
            elif operation == "puissance":
                resultat = nombre1 ** nombre2
            elif operation == "inverse":
                if nombre1 == 0:
                    resultat = "Inverse de zéro impossible"
                else:
                    resultat = 1 / nombre1
        except ValueError:
            resultat = "Entrée invalide"

    return render_template("index.html", resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)