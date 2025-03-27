# 🧠 PerGen – AI-Powered User Persona Generator

**PersonaGen** is a generative AI tool that transforms raw user research — interviews, surveys, or notes — into structured user personas in seconds.

Built with [Streamlit](https://streamlit.io/) and powered by [OpenRouter](https://openrouter.ai/) LLMs like **Mixtral**, **GPT-3.5**, and **Command R+**, this tool helps product teams, UX researchers, and marketers generate personas on the fly to better understand their users.

---

## ✨ Features

- 🔍 Converts qualitative research into clear, structured personas
- 🧠 Powered by multiple LLMs (Mixtral, Command R+, GPT-3.5 Turbo)
- ✅ Optimized for clarity, tone, and concise output
- 📋 Expandable, copyable output view
- ⚡ Live demo-ready (no PDF/export dependencies)

---

## 🚀 Demo

> Coming soon: [https://yourusername-personagen.streamlit.app](https://pergen.streamlit.app/)

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

