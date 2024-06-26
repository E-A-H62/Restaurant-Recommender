import os
from flask import Flask, request, render_template, redirect, url_for

from project import Project

app = Flask(__name__)

my_api_key = os.getenv('OPENAI_KEY')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_data():
    age = request.form["age"]
    cuisine = request.form["cuisine"]
    df = Project.get_recs(my_api_key, age, cuisine)
    return df.to_html()



if __name__ == '__main__':
    app.run(debug=True)