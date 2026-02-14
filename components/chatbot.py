"""Composant chatbot IA (Groq/Llama 3)."""
import os
import streamlit as st
from groq import Groq

from utils.translations import t


SYSTEM_PROMPT = """Tu es un assistant expert en électrochimie computationnelle : voltamétrie cyclique et spectroscopie d'impédance.

Tu connais parfaitement :
1. **La physique CV** : couple redox ferri/ferrocyanure Fe(CN)₆³⁻/Fe(CN)₆⁴⁻, cinétique de Butler-Volmer, transport de masse par diffusion (loi de Fick)
2. **La physique EIS** : circuit de Randles avec CPE et impédance de Warburg, diagrammes de Nyquist et Bode, extraction de R_ct, σ (Warburg), C_dl,eff
3. **Les paramètres clés** :
   - k₀ (constante cinétique standard) : de 10⁻⁶ à 10⁻³ m/s
   - α (coefficient de transfert) : 0.3, 0.5, 0.7
   - ν (vitesse de balayage) : 0.1, 0.2, 0.5 V/s
   - D (coefficient de diffusion), c (concentration), Q₀ (paramètre CPE)
4. **Les métriques CV** :
   - Ipa/Ipc (courants de pic anodique/cathodique)
   - ΔEp (séparation des pics) : ≈59 mV pour réversible
   - Régime réversible vs quasi-réversible vs irréversible
5. **L'implémentation** : Firedrake (FEM, maillage GMSH, solveur Newton-Raphson) pour CV ; Python/NumPy pour EIS

Réponds de manière concise, pédagogique et scientifiquement rigoureuse.
Utilise des équations LaTeX quand c'est pertinent (format $equation$ pour inline).
Si tu ne connais pas la réponse, dis-le honnêtement.
Réponds dans la langue de l'utilisateur (français ou anglais).
"""


def is_chatbot_enabled() -> bool:
    """Vérifie si le chatbot doit être affiché."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", None)
        except Exception:
            pass
    return bool(api_key)


def get_groq_client() -> Groq | None:
    """Retourne le client Groq si la clé API est disponible."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", None)
        except Exception:
            pass
    if api_key:
        return Groq(api_key=api_key)
    return None


def stream_groq_response(user_message: str):
    """Génère la réponse de Groq (Llama 3) en streaming."""
    client = get_groq_client()
    if not client:
        yield t("chat_api_missing")
        return

    st.session_state.chat_messages.append({"role": "user", "content": user_message})

    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(st.session_state.chat_messages)

        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
            stream=True
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                full_response += text
                yield text

        st.session_state.chat_messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        yield f"{t('chat_error')} ({str(e)[:50]}...)"


def render_chatbot():
    """Affiche le chatbot dans un popover."""
    with st.sidebar.popover(f"{t('chat_title')}", use_container_width=True):
        if st.button(t("chat_clear"), use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()

        st.markdown("---")

        if not st.session_state.chat_messages:
            st.info(t("chat_welcome"))

        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input(t("chat_placeholder")):
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                st.write_stream(stream_groq_response(prompt))
