from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/discord")
def discord():
    return redirect('https://discord.gg/myjXrkH2fu')

@app.route("/forum")
def forum():
    return render_template("forum.html")


if __name__ == "__main__":
    app.run(debug=True)

