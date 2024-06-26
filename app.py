import os
from flask import Flask, request, render_template

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
    return render_template(
        "results.html", tables=[
            df.to_html(classes='table table-striped',
                       index=False)], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True)
