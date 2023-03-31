from flask import Flask, render_template, request, flash
from transformers import pipeline
import predefined_model_test as pmt

sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
app = Flask(__name__)
app.secret_key = "arunisto"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sentiment", methods=["POST"])
def sentiment():
    text = request.form["word"]
    li = pmt.sentiment_analysis(text, sentiment_pipeline)
    flash(li)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)