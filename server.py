import os
from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "resialert_secret_key"

# ----------------------------
# TEMP STORAGE (FOR DASHBOARD)
# ----------------------------
issues = []

# ----------------------------
# WEB ROUTES
# ----------------------------

@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect("/dashboard")

        return "Invalid credentials"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", issues=issues)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ----------------------------
# API ROUTE (DEVICE INPUT)
# ----------------------------

@app.route("/api/issue", methods=["POST"])
def api_issue():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error"}), 400

    issue = {
        "room": data.get("room"),
        "type": data.get("type")
    }

    issues.append(issue)

    print(f"[NEW ISSUE] {issue}")

    return jsonify({"status": "success", "data": issue})


# ----------------------------
# RUN SERVER (RENDER READY)
# ----------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)