# Week 2 — AI Tool Comparison


## The requirement

Add a contact form to your Flask application. It must:
- render at /contact with fields for name, email and message
- validate that the email address is well-formed server side
- reject empty name or message fields with a visible error
- on success, show a confirmation page
- store nothing yet 


## Prompts used
the prompt was the same for both cases.



I have a small Flask application. Environment: Python 3.15.0, Flask 3.1.3,

Werkzeug 3.1.9, Jinja2 3.1.6, MarkupSafe 3.0.4, running locally on Windows.



Task: add a contact form.



Requirements:

1. GET /contact renders a form with fields: name, email, message.

2. POST /contact validates on the server:

  - name must not be empty or only whitespace

  - message must not be empty or only whitespace

 - email must be well-formed

3. If validation fails, re-display the form with a visible error message

  for each failing field, and keep what the user typed.

4. If validation passes, show a separate confirmation page.

5. Do not store the submission anywhere: no database, no file, no email.



Constraints:

- Use only Flask and the Python standard library. Do not add any packages

 (no Flask-WTF, no email-validator).

- Use Jinja2 templates in templates/ for the new pages only.

- Any user input shown back on the page must be escaped.

- Do not change, remove or reformat any existing code, including the

 ABOUT\_TEXT variable and the existing app.run() line.

- Do not hard-code any secrets.

- Only use functions you are certain exist in these versions; tell me if you are unsure.

### Claude

(verbatim prompt)

### Gemini

(verbatim prompt)


## Scores



&#x09;	ChatGPT		Claude

Correctness	4.5		3

Code quality	4.5		3 (down from 3.5 because of the templates)

Completeness	5		4.5

Security	4		3.5

Total /20	18		14 


## What each got wrong





#Chatgpt




The form is poorly laid out. 


There’s no link back from the confirmation page, and the action is hard-coded as /contact.

There’s no requirements.txt in its folder.

renders <script>alert(1)</script> 





## Which I kept, and why



Errors are styled red, and a “Please fix the errors below” summary appears at the top.

It uses novalidate with a comment explaining why: the browser’s own check is switched off so the server-side check is what actually gets tested. 

It keeps type="email", so phones show the email keyboard.

It uses url\_for('contact') instead of a hard-coded /contact.

The success page says “It has not been stored or sent anywhere” and links back to the form.
#Claude

Errors appear as plain black text. They’re technically visible, but they don’t stand out.

Form is very plain (but well set out)
renders <script>alert(1)</script> 


4. If validation passes, show a separate confirmation page.

5. Do not store the submission anywhere: no database, no file, no email.

