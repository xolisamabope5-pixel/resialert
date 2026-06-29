import os
from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "resialert_secret_key"

# ----------------------------
# WEB PAGES
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

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ----------------------------
# API (FOR DEVICE MANAGER)
# ----------------------------

@app.route("/api/issue", methods=["POST"])
def api_issue():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    room = data.get("room")
    issue_type = data.get("type")

    print(f"[ISSUE RECEIVED] Room: {room}, Type: {issue_type}")

    return jsonify({
        "status": "success",
        "message": "Issue received",
        "room": room,
        "type": issue_type
    })


# ----------------------------
# RUN (RENDER READY)
# ----------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)