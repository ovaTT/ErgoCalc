from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def resultado():
    altura_poplitea = float(request.form["altura_poplitea"])
    altura_cotovelo = float(request.form["altura_cotovelo"])
    altura_joelho = float(request.form["altura_joelho"])
    sapato = float(request.form["sapato"])
    altura_cadeira = float(request.form["altura_cadeira"])

    avaliacao = calcular(altura_poplitea, altura_cotovelo, altura_joelho, sapato, altura_cadeira)

    return render_template("index.html", avaliacao=avaliacao)

if __name__ == "__main__":
    app.run(debug=True)