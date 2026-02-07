"""Traductions et gestion de la langue — Couple redox ferro/ferricyanure."""
import streamlit as st

TRANSLATIONS = {
    "fr": {
        "title": "CV et EIS — Couple redox ferro/ferricyanure",
        "sidebar_title": "CV et EIS — Couple redox",
        "gen_header": "Général",
        "models_header": "Résultats de modélisation",
        "annex_header": "Annexes",
        "gen_pages": ["Accueil", "Introduction", "Données électrochimiques", "Comparaison des études"],
        "model_pages": ["1 : CV couple redox sur Au", "2 : EIS couple redox sur Au"],
        "annex_pages": ["Conclusion et perspectives", "Lexique", "Équations clés", "Un peu d'histoire", "Références bibliographiques"],
        "tabs_cv_study": ["Physique", "Code", "Résultats", "Analyse"],
        "tabs_eis_ferro": ["Physique", "Code", "Résultats", "Analyse"],
        "version_info": """**Version 2.1.2** — Dec 2025 - *EQU*

**Nouveautés :**
- Étude paramétrique EIS
- Assistant IA Llama 3
- Filtres en cascade""",
        # Labels CV
        "title_study_1": "Étude 1 : CV d'un couple redox sur Au",
        "title_study_2": "Étude 2 : EIS d'un couple redox sur Au",
        "lbl_k0": "k⁰ (m/s)",
        "lbl_alpha": "α",
        "lbl_scan_rate": "v (V/s)",
        # Labels EIS ferro
        "lbl_n_elec": "n (électrons)",
        "lbl_D": "D (m²/s)",
        "lbl_conc": "c (mol/m³)",
        "lbl_Q0": "Q₀ (µF/cm²)",
        "eis_ferro_metrics_title": "Métriques EIS — ferro/ferri",
        "lbl_Rct_calc": "Rct calc (Ω)",
        "lbl_sigma": "σ (Ω·s⁻⁰·⁵)",
        "lbl_omega_max": "ω_max (rad/s)",
        "lbl_Cdl_eff": "Cdl_eff (F)",
        "lbl_Rs": "Rs (Ω)",
        "lbl_Rct": "Rct (Ω)",
        "lbl_phase_max": "Phase max (°)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LANCER LA VISUALISATION",
        "btn_reset": "RÉINITIALISER",
        "lbl_avail_sims": "Simulations disponibles",
        "metrics_title": "Métriques Électrochimiques",
        "lbl_Ipa": "Ipa (µA)",
        "lbl_Ipc": "Ipc (µA)",
        "lbl_ratio": "|Ipa/Ipc|",
        "lbl_delta_Ep": "ΔEp (mV)",
        "image_unavailable": "Image non disponible",
        "analysis_cv_title": "### Analyse de l'étude paramétrique",
        "gif_coming_soon": "Visualisation dynamique (Gifs) - À venir",
        "placeholder_coming_soon": "Étude à venir - Contenu en cours de préparation",
        # Chatbot
        "chat_title": "Assistant IA",
        "chat_welcome": "Bonjour ! Je suis votre assistant pour comprendre les simulations de voltamétrie cyclique et d'impédance. Posez-moi vos questions sur Butler-Volmer, le transport de masse, ou l'interprétation des diagrammes !",
        "chat_placeholder": "Posez votre question...",
        "chat_error": "Erreur de connexion à l'API.",
        "chat_clear": "Effacer",
        "chat_api_missing": "Clé API manquante. Configurez GROQ_API_KEY.",
    },
    "en": {
        "title": "CV & EIS — Ferro/ferricyanide Redox Couple",
        "sidebar_title": "CV & EIS — Redox Couple",
        "gen_header": "General",
        "models_header": "Modeling Results",
        "annex_header": "Appendices",
        "gen_pages": ["Home", "Introduction", "Electrochemical Data", "Study Comparison"],
        "model_pages": ["1: CV redox couple on Au", "2: EIS redox couple on Au"],
        "annex_pages": ["Conclusion and Perspectives", "Glossary", "Key Equations", "A Bit of History", "Bibliographical References"],
        "tabs_cv_study": ["Physics", "Code", "Results", "Analysis"],
        "tabs_eis_ferro": ["Physics", "Code", "Results", "Analysis"],
        "version_info": """**Version 2.1.2** — Dec 2025 - *EQU*

**New Features:**
- EIS parametric study
- AI Assistant Llama 3
- Cascade filters""",
        # Labels CV
        "title_study_1": "Study 1: CV of a redox couple on Au",
        "title_study_2": "Study 2: EIS of a redox couple on Au",
        "lbl_k0": "k⁰ (m/s)",
        "lbl_alpha": "α",
        "lbl_scan_rate": "v (V/s)",
        # Labels EIS ferro
        "lbl_n_elec": "n (electrons)",
        "lbl_D": "D (m²/s)",
        "lbl_conc": "c (mol/m³)",
        "lbl_Q0": "Q₀ (µF/cm²)",
        "eis_ferro_metrics_title": "EIS Metrics — ferro/ferri",
        "lbl_Rct_calc": "Rct calc (Ω)",
        "lbl_sigma": "σ (Ω·s⁻⁰·⁵)",
        "lbl_omega_max": "ω_max (rad/s)",
        "lbl_Cdl_eff": "Cdl_eff (F)",
        "lbl_Rs": "Rs (Ω)",
        "lbl_Rct": "Rct (Ω)",
        "lbl_phase_max": "Phase max (°)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LAUNCH VISUALIZATION",
        "btn_reset": "RESET",
        "lbl_avail_sims": "Available Simulations",
        "metrics_title": "Electrochemical Metrics",
        "lbl_Ipa": "Ipa (µA)",
        "lbl_Ipc": "Ipc (µA)",
        "lbl_ratio": "|Ipa/Ipc|",
        "lbl_delta_Ep": "ΔEp (mV)",
        "image_unavailable": "Image not available",
        "analysis_cv_title": "### Parametric Study Analysis",
        "gif_coming_soon": "Dynamic Visualization (Gifs) - Coming Soon",
        "placeholder_coming_soon": "Coming Soon - Content under preparation",
        # Chatbot
        "chat_title": "AI Assistant",
        "chat_welcome": "Hello! I'm your assistant to help you understand cyclic voltammetry and impedance simulations. Ask me about Butler-Volmer, mass transport, or diagram interpretation!",
        "chat_placeholder": "Ask your question...",
        "chat_error": "API connection error.",
        "chat_clear": "Clear",
        "chat_api_missing": "API key missing. Configure GROQ_API_KEY.",
    }
}


def get_language() -> str:
    """Retourne la langue actuelle."""
    if 'lang' not in st.session_state:
        st.session_state.lang = 'fr'
    return st.session_state.lang


def t(key: str) -> str:
    """Retourne la traduction pour la clé donnée."""
    lang = get_language()
    return TRANSLATIONS[lang].get(key, key)
