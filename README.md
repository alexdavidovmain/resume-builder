# 📄 Alex Davidov's Resume Builder

🔗 **Live Demo:** [alexdavidov.onrender.com](https://alexdavidov.onrender.com)

## What is this?

You fill in your name, contact info, work experience, education, and skills. Click one button and AI rewrites everything — polishes your job descriptions into bullet points, writes a professional summary, and organizes your skills. The result is a clean resume preview you can export as a JSON file.

Think of it like having a professional resume writer sitting next to you, instantly.

---

## Two versions

**Flask version** — runs locally on your computer via Python. Full backend, more powerful.

**Browser version** (`preview/index.html`) — open directly in Chrome, no Python needed. Just enter your Groq API key and go. Great for demos.

---

## What I built it with

| Tool | What it's for |
|---|---|
| Python | Backend language |
| Flask | Web framework to serve the app |
| Groq API | Free AI API powering the resume generation |
| Llama 3.3 70B | The AI model that writes and enhances the resume |
| HTML/CSS/JS | Frontend interface |
| Render | Free cloud hosting for the live demo |

---

## How I built it — step by step

**Step 1 — Designed the form**
Built a two-column layout: left side is the input form (personal info, experience, education, skills), right side is a live preview panel where the generated resume appears.

**Step 2 — Connected the AI**
Used the Groq API with Llama 3.3 70B. The model receives all the user's raw data as JSON and returns an enhanced version — a professional summary, polished bullet points for each job, and a cleaned up skills list. The prompt strictly asks for JSON output so it's easy to parse and render.

**Step 3 — Built the Flask backend**
Three routes: `/` serves the page, `/generate` sends data to the AI and returns the result, `/export` packages everything into a downloadable JSON file.

**Step 4 — Built the browser version**
A standalone HTML file that calls the Groq API directly from the browser — no Python needed. The user enters their API key in a field and everything runs client-side. Perfect for showing the project without needing a server running.

**Step 5 — Deployed to Render**
Hosted the Flask app on Render with the API key stored as an environment variable so it never touches GitHub.

---

## How to run it locally

**Install dependencies:**
```
pip install flask groq
```

**Add your Groq API key** in `generator.py`:
```python
client = Groq(api_key="YOUR_GROQ_API_KEY_HERE")
```

**Run:**
```
python app.py
```

**Open:**
```
http://127.0.0.1:5000
```

Get a free Groq API key at **console.groq.com**

---

## What I learned

- How to prompt an AI model to return structured JSON reliably
- How to build a full Flask app with multiple routes
- How to call an external AI API from both Python and the browser
- How to design a split-panel UI that updates live
- How to deploy a Python web app to the cloud with environment variables

---

*Built by Alexander Davidov*
