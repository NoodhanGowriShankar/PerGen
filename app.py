import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from fpdf import FPDF
import pyperclip
import re

# Load API Key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Configure OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Streamlit UI config
st.set_page_config(page_title="PersonaGen", page_icon="🧠")
st.title("🧠 PerGen – AI-Powered User Persona Generator")
st.markdown("Paste user research notes below to generate a structured persona.")

# Sidebar controls
st.sidebar.title("⚙️ Settings")

models = {
    "Mixtral (Mistral AI)": "mistralai/mixtral-8x7b-instruct",
    "Claude 2 (Anthropic)": "anthropic/claude-2"
}

model_choice = st.sidebar.selectbox("Choose a model:", list(models.keys()))
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
                persona = response.choices[0].message.content
                st.success("✅ Persona generated!")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Display with clean formatting
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

    # Action buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(persona)
            st.success("Copied to clipboard!")

    with col2:
        if st.button("📄 Export to PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in persona.split('\n'):
                pdf.multi_cell(0, 10, line)
            pdf.output("persona_output.pdf")
            with open("persona_output.pdf", "rb") as f:
                st.download_button(
                    label="Download Persona PDF",
                    data=f,
                    file_name="persona_output.pdf",
                    mime="application/pdf"
                )
