from flask import Flask, render_template, request
import main

app = Flask(__name__)
app.secret_key = "app"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/how")
def how():
    return render_template("how.html")


@app.route("/pred", methods=["GET", "POST"])
def pred():
    gelen_url = request.form.get("url")
    dff = main.make_all(gelen_url, 1)
    dff["site_ranking"] = [i + 1 for i in dff.index.tolist()]
    liste_bar = dff.sort_values("bar_sorting_score", ascending=False).values.tolist()

    return render_template("sort.html", liste_bar=liste_bar)


if __name__ == "__main__":
    app.run(debug=True)
