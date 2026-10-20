from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Replace with your own ~150-word answer.
ABOUT_TEXT = """\
I would build a simple library manager for a home or community book collection. Instead of typing in every detail by hand, the owner would scan or enter a book’s ISBN, and the system would automatically pull in the title, author, cover image, genre and description from an online book database. Every book would then sit in one searchable catalogue.

On top of that, I’d add filters so anyone can quickly narrow the collection by fiction or non-fiction, genre, or author. Finding a book should take seconds, not a hunt along the shelves.

The final piece is lending. When someone borrows a book, they log their name, and the owner gets a notification. When it comes back, another alert confirms the return. Over time, the owner has a clear record of who has what, who had it before, and which books never came home.\
"""


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


@app.route("/about")
def about():
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>About - GerryB-cct</title>
</head>
<body>
  <h1>What would I build if it took an evening instead of a quarter?</h1>
  <p>{escape(ABOUT_TEXT)}</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)