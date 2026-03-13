from flask import Flask, request

app = Flask(__name__)

urls = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        urls.append(url)

    html = """
    <h1>サイト監視SaaS</h1>
    <form method="POST">
        <input name="url" placeholder="監視したいURL">
        <button type="submit">登録</button>
    </form>
    <h2>登録URL</h2>
    """

    for u in urls:
        html += f"<p>{u}</p>"

    return html


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)