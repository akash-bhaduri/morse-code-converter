# morse-code-converter

A small web-based Morse code converter. Provides a simple UI to convert between plain text and Morse code using a lightweight Python web app.

---

## Features

- Convert plain text → Morse code and Morse code → plain text
- Simple web interface (HTML templates + static CSS)
- Single-file entry point (`main.py`) for easy local testing

---

## Requirements

- Python 3.8 or newer
- A POSIX-like shell (Linux / macOS) or PowerShell on Windows

---

## Install (quick)

```bash
# clone
git clone https://github.com/akash-bhaduri/morse-code-converter.git
cd morse-code-converter

# create a virtual environment
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

```

---

## Run (development)

```bash
# quick run using Python
python main.py

```

Then open `http://127.0.0.1:5000` in your browser and use the converter UI.

---

## Typical file layout

```
morse-code-converter/
├─ main.py               # app entrypoint
├─ pyproject.toml        # project metadata / dependencies
├─ templates/index.html  # HTML templates for the web UI
├─ static/css           # stylesheet(s)
├─ .python-version
├─ .gitignore
└─ README.md
```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/your-change`)
3. Make changes and add tests if applicable
4. Open a pull request

Please keep changes small and focused.

---

## Issues & Support

Open an issue in this repository if you find a bug or want a feature.

---

## License

This project is licensed under the terms of the MIT License.  
See the [LICENSE](LICENSE) file for details.

### Notes for you

- I kept this README intentionally short and practical so it’s easy for newcomers to clone and run locally.
- If you want, I can expand the README with a `requirements.txt`, example screenshots, or a small demo GIF.

---
