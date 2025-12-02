print("testing")
from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion logic
def convert_length(value, from_unit, to_unit):
    factors = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "ounce": 28.3495,
        "pound": 453.592
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        category = request.form["category"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        if category == "length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "weight":
            result = convert_weight(value, from_unit, to_unit)
        elif category == "temperature":
            result = convert_temperature(value, from_unit, to_unit)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
