from flask import Flask
from markupsafe import escape
from flask import render_template, request
import re

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


# Pragmatic email check: local@domain.tld, ASCII only, no spaces,
# no leading/trailing/double dots, domain labels may not start or end with "-".
EMAIL_RE = re.compile(
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}"
)


def validate_contact(name, email, message):
    errors = {}
    if not name.strip():
        errors["name"] = "Please enter your name."
    if len(email.strip()) > 254 or not EMAIL_RE.fullmatch(email.strip()):
        errors["email"] = "Please enter a valid email address, e.g. name@example.com."
    if not message.strip():
        errors["message"] = "Please enter a message."
    return errors


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", form={}, errors={})

    form = {
        "name": request.form.get("name", ""),
        "email": request.form.get("email", ""),
        "message": request.form.get("message", ""),
    }
    errors = validate_contact(form["name"], form["email"], form["message"])
    if errors:
        return render_template("contact.html", form=form, errors=errors), 400

    # Nothing is stored or sent: the submission is discarded after this response.
    return render_template("contact_success.html", name=form["name"].strip())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
