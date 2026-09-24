from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route("/website")
def website():
    return send_from_directory("frontend", "index.html")
@app.route("/style.css")
def style():
    return send_from_directory("frontend", "style.css")


@app.route("/script.js")
def script():
    return send_from_directory("frontend", "script.js")


@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")



@app.route("/add")
def add():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    return str(num1 + num2)


@app.route("/subtract")
def subtract():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    return str(num1 - num2)


@app.route("/multiply")
def multiply():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    return str(num1 * num2)


@app.route("/divide")
def divide():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))

    if num2 == 0:
        return "Cannot divide by zero."

    return str(num1 / num2)


@app.route("/square")
def square():
    num = float(request.args.get("num"))
    return str(num ** 2)


@app.route("/cube")
def cube():
    num = float(request.args.get("num"))
    return str(num ** 3)


@app.route("/percentage")
def percentage():
    num = float(request.args.get("num"))
    percent = float(request.args.get("percent"))
    return str((num * percent) / 100)


@app.route("/average")
def average():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    return str((num1 + num2) / 2)


@app.route("/convert")
def convert():
    conversion = request.args.get("conversion")
    value = float(request.args.get("value"))

    if conversion == "km_to_m":
        return str(value * 1000)

    elif conversion == "m_to_km":
        return str(value / 1000)

    elif conversion == "kg_to_g":
        return str(value * 1000)

    elif conversion == "g_to_kg":
        return str(value / 1000)

    elif conversion == "c_to_f":
        return str((value * 9 / 5) + 32)

    elif conversion == "f_to_c":
        return str((value - 32) * 5 / 9)

    else:
        return "Invalid conversion."


if __name__ == "__main__":
    app.run(debug=True)