from unittest import case
from flask import Flask, redirect, make_response, render_template, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    
    return render_template("index.html")


@app.route("/cv")
def cv():
    
    return render_template("cv.html")


@app.route("/projects")
def projects():
    
    return render_template("projects.html")


@app.route("/report/<name>")
def report(name):
    match name:
        case "League API":
            return render_template("leagueAPI_report.html", name=name)
        case "TopOut":
            return render_template("topout_report.html", name=name)
        case _:
            return

    
    