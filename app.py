import streamlit as st
import subprocess
import os
from huggingface_hub import hf_hub_download


st.set_page_config(page_title="French2English", page_icon="🌍", layout="centered")

#model_path = "fr-en-model_step_100000.pt"
# Téléchargement du modèle depuis HuggingFace
model_path = hf_hub_download(
    repo_id="IngWalker/french2english-translator",
    filename="fr-en-model_step_100000.pt"
)

def translate_text(text):
    try:
        with open("input.txt", "w", encoding="utf-8") as f:
            f.write(text)

        output_file = "output.txt"

        command = [
            "onmt_translate",
            "-model", model_path,
            "-src", "input.txt",
            "-output", output_file,
            "-batch_size", "1",
            "-beam_size", "5",
            "-max_length", "50"
        ]

        subprocess.run(command, check=True)

        # Lire la traduction depuis le fichier de sortie
        with open(output_file, "r", encoding="utf-8") as f:
            translation = f.read().strip()

        cleaned_translation = translation.replace("<unk>", "").strip()
        return cleaned_translation

    except subprocess.CalledProcessError as e:
        return f"Erreur : {str(e)}"

    finally:
        # Nettoyer les fichiers temporaires
        os.remove("input.txt")
        if os.path.exists(output_file):
            os.remove(output_file)

# 🌟 CSS personnalisé pour l'interface
st.markdown(
    """
    <style>
    .main { background-color: #f5f5f5; color: black; }
    .stTextArea { border-radius: 10px; width: 100%; }
    .stButton>button { border-radius: 8px; background-color: #4285F4; color: white; font-size: 16px; width: 200px; }
    .stSelectbox [disabled] {
        background-color: #e9ecef;
        color: #6c757d;
        pointer-events: none;
        cursor: not-allowed;
    }
    .title { text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 20px; }
    .center-btn { display: flex; justify-content: center; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🌍 French2English Translator</div>', unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Langue source", ["Français"], index=0, disabled=True)
with col2:
    tgt_lang = st.selectbox("Langue cible", ["Anglais"], index=0, disabled=True)

col1, col2 = st.columns(2)


with col1:
    st.write("### Texte à traduire")
    user_input = st.text_area("Entrez votre texte", placeholder="Écrivez ici...", key="input_text")


with col2:
    st.write("### Traduction")
    translated_text = st.empty()


st.markdown('<div class="center-btn">', unsafe_allow_html=True)
if st.button("Traduire"):
    if user_input.strip():
        with st.spinner("🔄 Traduction en cours..."):
            translation = translate_text(user_input)
            translated_text.text_area("Traduction", translation, disabled=True)
    else:
        st.warning("Veuillez entrer un texte à traduire.")
st.markdown('</div>', unsafe_allow_html=True)
