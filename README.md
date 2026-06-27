# My Portfolio

A clean, professional portfolio website built with **Python Flask** + **HTML/CSS**.

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python app.py
```

### 3. Open your browser
Visit: **http://127.0.0.1:5000**

---

## Customize It

All your content lives in one place — the `PORTFOLIO` dictionary at the top of `app.py`.

### Change your name, role & tagline
```python
"name": "Your Name",
"role": "Your Job Title",
"tagline": "A short line about what you do.",
```

### Add projects
```python
{
    "title": "My Cool Project",
    "tag": "Web App",
    "description": "What it does.",
    "tech": ["Python", "Flask", "CSS"],
    "link": "https://github.com/you/project",
},
```

### Add skills
```python
{
    "icon": "🤖",
    "name": "Machine Learning",
    "items": ["scikit-learn", "TensorFlow", "Pandas"],
},
```

### Change contact links
```python
{"icon": "✉️", "label": "Email Me", "href": "mailto:you@email.com"},
{"icon": "💼", "label": "LinkedIn",  "href": "https://linkedin.com/in/yourprofile"},
{"icon": "🐙", "label": "GitHub",    "href": "https://github.com/yourusername"},
```

---

## File Structure

```
portfolio/
├── app.py                  ← Flask server + all your data
├── requirements.txt        ← Dependencies
├── templates/
│   └── index.html          ← HTML template (Jinja2)
└── static/
    └── css/
        └── style.css       ← All styling
```
