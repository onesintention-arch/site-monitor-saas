from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS monitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        webhook TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        url = request.form["url"]
        webhook = request.form["webhook"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO monitors (url, webhook) VALUES (?, ?)",
            (url, webhook)
        )

        conn.commit()
        conn.close()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT url FROM monitors")
    urls = c.fetchall()

    conn.close()

    html = """
    <h1>サイト監視SaaS</h1>

    <form method="POST">

    <p>監視URL</p>
    <input name="url">

    <p>Discord Webhook</p>
    <input name="webhook">

    <br><br>
    <button type="submit">登録</button>

    </form>

    <h2>登録URL</h2>
    """

    for u in urls:
        html += f"<p>{u[0]}</p>"

    return html


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)