from flask import Flask
from flask import render_template, request
from markupsafe import escape
from email.utils import parseaddr

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


def is_well_formed_email(value):
    if not value or value != value.strip() or any(char.isspace() for char in value):
        return False
    if value.count("@") != 1:
        return False
    display_name, address = parseaddr(value)
    if display_name or address != value:
        return False
    local, separator, domain = value.rpartition("@")
    if not separator or not local or not domain or "." not in domain:
        return False
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    return all(part and not part.startswith("-") and not part.endswith("-") for part in domain.split("."))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    values = {"name": "", "email": "", "message": ""}
    errors = {}

    if request.method == "POST":
        values = {field: request.form.get(field, "") for field in values}
        if not values["name"].strip():
            errors["name"] = "Please enter your name."
        if not is_well_formed_email(values["email"]):
            errors["email"] = "Please enter a valid email address."
        if not values["message"].strip():
            errors["message"] = "Please enter a message."
        if not errors:
            return render_template("contact_confirmation.html", name=values["name"])

    return render_template("contact.html", values=values, errors=errors)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
