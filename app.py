from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>GerryB-cct</title>
</head>
<body>
  <h1>Hello from GerryB-cct</h1>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
