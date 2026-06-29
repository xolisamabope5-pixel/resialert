from flask import Flask, request, jsonify, render_template, redirect, session, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = "resialert_secret_key"


# -----------------------------
# DATABASE INIT
# -----------------------------
def init_db():
    conn = sqlite3.connect("resialert.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room TEXT,
            issue TEXT,
            device_id TEXT,
            time TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


# -----------------------------
# LOGIN PAGE
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # SIMPLE LOGIN (we upgrade later)
        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")

        return "Invalid login ❌"

    return render_template("login.html")


# -----------------------------
# LOGOUT
# -----------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return redirect("/login")


# -----------------------------
# REPORT (DEVICE → SERVER)
# -----------------------------
@app.route("/report", methods=["POST"])
def report():
    data = request.json

    room = data.get("room")
    issue = data.get("issue")
    device_id = data.get("device_id", "unknown")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("resialert.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO complaints (room, issue, device_id, time, status)
        VALUES (?, ?, ?, ?, ?)
    """, (room, issue, device_id, time, "Pending"))

    conn.commit()
    conn.close()

    return jsonify({"status": "success"})


# -----------------------------
# RESOLVE COMPLAINT
# -----------------------------
@app.route("/resolve/<int:complaint_id>", methods=["POST"])
def resolve(complaint_id):
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("resialert.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status = 'Resolved'
        WHERE id = ?
    """, (complaint_id,))

    conn.commit()
    conn.close()

    return redirect("/dashboard")


# -----------------------------
# DASHBOARD (PROTECTED)
# -----------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("resialert.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, room, issue, time, status
        FROM complaints
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    complaints = []
    for r in rows:
        complaints.append({
            "id": r[0],
            "room": r[1],
            "issue": r[2],
            "time": r[3],
            "status": r[4]
        })

    return render_template("dashboard.html", complaints=complaints)


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)