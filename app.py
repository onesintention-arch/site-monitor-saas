from flask import Flask, request

app = Flask(__name__)

data = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        url = request.form["url"]
        webhook = request.form["webhook"]

        data.append({
            "url": url,
            "webhook": webhook
        })

    html = """
    <h1>サイト監視SaaS</h1>

    <form method="POST">

    <p>監視URL</p>
    <input name="url" placeholder="https://example.com">

    <p>Discord Webhook</p>
    <input name="webhook" placeholder="Discord webhook URL">

    <br><br>

    <button type="submit">登録</button>

    </form>

    <h2>登録リスト</h2>
    """

    for item in data:
        html += f"<p>{item['url']}</p>"

    return html


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)