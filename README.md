# GerryB-cct

A minimal [Flask](https://flask.palletsprojects.com/) 3.x web application with 3 routes:

- `/` returns an HTML page saying **"Hello from GerryB-cct"**.
- `/about` returns a short answer to "What would you build if it took an evening instead of a quarter?"
- `/contact` returns a short form that allows a name, email address and message to be sent to the server and the e-mail address is server side validated

## Project files

lowcode-project/
├── app.py                     The Flask application
├── requirements.txt           Pinned dependency versions
├── templates/
│   ├── contact.html           Contact form, with error messages
│   └── contact_success.html   Confirmation page after a valid submission
└── experiments/
    ├── week02/
    │   ├── chatgpt-winner/    ChatGPT's contact form (unedited; this version was kept)
    │   └── claude/            Claude's contact form (unedited)
    └── docs/
        ├── week02-tool-comparison.md   Week 2 AI tool comparison report
        ├── notes.md                    Working notes
        └── images/                     Screenshots used in the report
## Requirements

* Python 3.9 or newer (Flask 3.1 minimum). Tested with Python 3.13.\*Correction: "Tested with Python 3.13 on Linux, plus 3.15 on Windows"

## Installation

Create a virtual environment in the project folder, activate it, and install the dependencies.

If a virtual environment is already active (your prompt starts with `(.venv)`), run `deactivate` first. On Windows, Python cannot replace a `python.exe` that is currently running.

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows: Git Bash or MSYS2 (UCRT64)**

Use forward slashes. Bash treats `\\` as an escape character.

```bash
python3 -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

**Windows: PowerShell**

```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

If PowerShell refuses to run the activation script, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

## Running

With the virtual environment active:

```bash
python app.py
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. Press `Ctrl+C` to stop the server.

You can also start it without debug mode:

```bash
flask --app app run
```

## Notes

* **Debug mode:** `python app.py` starts the server with `debug=True`, which enables auto-reload and the interactive debugger. Use this only on your own machine. The debugger lets anyone who can reach the server run code on your machine.
* **Local only:** the server listens on `127.0.0.1`, so only your own machine can reach it. To allow access from other devices on your network, change the host in `app.py` to `0.0.0.0`.
* **Production:** don't use the built-in development server. Use a production WSGI server instead, for example `gunicorn app:app` (Linux/macOS) or `waitress-serve app:app` (Windows). Install either with `pip` first.
* **Git:** keep the virtual environment out of version control:

```bash
  echo ".venv/" >> .gitignore
  ```

