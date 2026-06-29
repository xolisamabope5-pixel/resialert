import os
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "resialert_secret_key"

# ----------------------------
# ROUTES
# ----------------------------

@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # simple demo login (you can improve later)
        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect("/dashboard")

        return "Invalid credentials"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ----------------------------
# RUN (IMPORTANT FOR RENDER)
# ----------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)