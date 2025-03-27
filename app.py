import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import re

# Load API Key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Streamlit UI
st.set_page_config(page_title="PerGen", page_icon="🧠")
st.title("🧠 PerGen – AI-Powered User Persona Generator")
st.markdown("Paste user research notes below to generate a structured persona.")

# Sidebar model selection
models = {
    "Mixtral (Mistral AI)": "mistralai/mixtral-8x7b-instruct",
    "Command R+ (Cohere)": "cohere/command-r-plus",
    "GPT-3.5 Turbo": "openai/gpt-3.5-turbo"
}
model_choice = st.sidebar.selectbox("Choose a model:", list(models.keys()), index=0)
selected_model = models[model_choice]

# Input
user_input = st.text_area("✍️ Paste user interview notes, survey results, or feedback here:", height=300)
persona = ""

# Generate
if st.button("Generate Persona"):
    if not user_input.strip():
        st.warning("Please enter some input text.")
    else:
        with st.spinner("Generating persona..."):
            try:
                response = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {
                            "role": "user",
                            "content": f'''You're an AI assistant helping a product team create a structured user persona based on research notes.

Generate a persona with the following sections:
- Name
- Demographics (age, job, location)
- Goals
- Pain Points
- Behavioral Traits
- A short, natural-sounding user quote

Keep the tone professional but friendly. Be brief and avoid repeating ideas. Do not pad the output.

Notes:
{user_input}'''
                        }
                    ],
                    temperature=0.7
                )

                if response and hasattr(response, "choices") and response.choices:
                    choice = response.choices[0]

                    if hasattr(choice, "message") and hasattr(choice.message, "content"):
                        persona = choice.message.content
                    elif hasattr(choice, "text"):
                        persona = choice.text
                    else:
                        persona = None

                    if persona:
                        st.success("✅ Persona generated!")
                    else:
                        st.error("❌ No content found in the response. Try another model or input.")
                else:
                    st.error("❌ No response choices received.")

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Display
if persona:
    st.markdown("### 👤 **Persona Summary**")

    sections = {
        "Name": "🧍 Name",
        "Demographics": "📊 Demographics",
        "Goals": "🎯 Goals",
        "Pain Points": "❌ Pain Points",
        "Behavioral Traits": "🧠 Behavioral Traits",
        "Short User Quote": "💬 Quote"
    }

    formatted = ""
    for key, label in sections.items():
        match = re.search(f"{key}:(.*?)(?=\n[A-Z][a-z]+:|$)", persona, re.DOTALL)
        if match:
            content = match.group(1).strip()
            formatted += f"**{label}**\n\n{content}\n\n---\n"

    st.markdown(formatted)

    # Expandable raw view
    with st.expander("📋 View & Copy Raw Persona Text"):
        st.code(persona, language="markdown")
