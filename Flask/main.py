from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Thank you, {name}, for contacting us!"

    return render_template("contact.html")

# varaible rule 
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    return f"User ID: {user_id}"

@app.route("/score/<int:score>")
def results(score):

    return render_template("result.html", results=score )

@app.route("/newresults/<int:newscore>")
def displayResults(newscore):
    if newscore >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    output = { "Score": newscore, "Results" : res}

    return render_template("results1.html", results=output)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    name = request.form.get("name")
    return f"Thank you, {name}, for submitting your information!"



if (__name__ == "__main__"):
    app.run(debug=True, port=3000)