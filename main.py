from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calculadora")
def abrir_calculadora():
    return render_template("calculadora.html")


@app.route("/calcular", methods=["POST"])
def resultado():
    campos = [
        "altura_poplitea",
        "altura_cotovelo",
        "altura_joelho",
        "sapato",
        "altura_cadeira",
    ]

    medidas = {}

    try:
        for campo in campos:
            valor = request.form.get(campo, "").strip()
            valor = valor.replace(",", ".")

            if not valor:
                raise ValueError("Preencha todos os campos.")

            medidas[campo] = float(valor)

        resultado_calculo = calcular(
            medidas["altura_poplitea"],
            medidas["altura_cotovelo"],
            medidas["altura_joelho"],
            medidas["sapato"],
            medidas["altura_cadeira"],
        )

        if not resultado_calculo["valido"]:
            return render_template(
                "calculadora.html",
                erro=resultado_calculo["mensagem"],
                medidas=medidas,
            )

        return render_template(
            "calculadora.html",
            resultado=resultado_calculo,
            medidas=medidas,
        )

    except ValueError as erro:
        return render_template(
            "calculadora.html",
            erro=str(erro) or "Informe medidas numéricas válidas.",
            medidas=request.form,
        )


if __name__ == "__main__":
    app.run(debug=True)