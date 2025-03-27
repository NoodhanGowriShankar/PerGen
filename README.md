# 🧠 PersonaGen – AI-Powered User Persona Generator

**PersonaGen** is a generative AI tool that transforms raw user research — interviews, surveys, or notes — into structured user personas in seconds.

Built with [Streamlit](https://streamlit.io/) and powered by [OpenRouter](https://openrouter.ai/) LLMs like **Mixtral**, **GPT-3.5**, and **Command R+**, this tool helps product teams, UX researchers, and marketers generate personas on the fly to better understand their users.

---

## ✨ Features

- 🔍 Converts qualitative research into clear, structured personas
- 🧠 Powered by multiple LLMs (Mixtral, Command R+, GPT-3.5 Turbo)
- ✅ Optimized for clarity, tone, and concise output
- 📋 Expandable, copyable output view
- ⚡ Live demo-ready (no export dependencies)

---

## 🚀 Live Demo

🔗 Try it here: [https://pergen.streamlit.app/](https://pergen.streamlit.app/)

---

## 🛠 How It Works

1. Paste your user interview notes or survey input
2. Choose a model from the sidebar
3. Click **“Generate Persona”**
4. Get a structured output with:
   - Name
   - Demographics
   - Goals
   - Pain Points
   - Behavioral Traits
   - User Quote

---

## 🧩 Tech Stack

- `Python`
- `Streamlit`
- `OpenRouter` API
- `Dotenv` for API key handling
- `Regex` for persona parsing

---

## 🧪 Models Available

| Model              | Provider         | Cost-efficient? | Description                      |
|-------------------|------------------|-----------------|----------------------------------|
| Mixtral            | Mistral AI       | ✅ Very cheap     | Fast, clean, concise output      |
| Command R+         | Cohere           | ✅ Cheap          | Great for structured text        |
| GPT-3.5 Turbo      | OpenAI (via OR)  | ✅ Affordable     | Friendly tone, reliable fallback |

---

## 🔐 API Key Setup

This app uses [OpenRouter](https://openrouter.ai/) for multi-model LLM access.

Create a `.env` file in your root directory:

```
OPENROUTER_API_KEY="your-api-key-here"
```

If you're using **Streamlit Cloud**, set this under **App > Settings > Secrets**:

```toml
OPENROUTER_API_KEY = "your-api-key-here"
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/personagen.git
cd personagen
pip install -r requirements.txt
streamlit run app.py
```

---

## 🤝 Contribution & Feedback

Feel free to fork this repo, add features, or reach out with suggestions or bugs.

---

## 📄 License

MIT License
