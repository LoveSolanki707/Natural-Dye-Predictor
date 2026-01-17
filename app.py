from flask import Flask, render_template, request
from ai.sd_client import generate_image
from logic.explanation import generate_explanation
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    explanation = None

    if request.method == "POST":
        cloth = request.form["cloth"]
        fabric = request.form["fabric"]
        ingredient = request.form["ingredient"]
        placement = request.form["placement"]

        prompt = f"""
        A realistic {fabric} {cloth} naturally dyed using {ingredient} petals,
        eco print pattern with {placement} placement,
        soft organic texture, sustainable fashion, photorealistic
        """

        result = generate_image(prompt)
        explanation = generate_explanation(ingredient, placement)

    return render_template("index.html", result=result, explanation=explanation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
