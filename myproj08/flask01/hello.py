from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    #DB Access.가능.
    like_foods = ["스테이크", "전골", "고기", "쌀국수", "자장면",]
    return render_template("profile.html", like_foods=like_foods)

@app.route("/posts")
def post_list():
    return render_template("post_list.html")

