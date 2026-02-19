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

if (__name__ == "__main__"):
    app.run(debug=True, port=3000)