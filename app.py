"""Application Streamlit — CV et EIS du couple redox ferro/ferricyanure sur Au."""
import os
import streamlit as st

# --- Configuration de la page (DOIT être en premier) ---
st.set_page_config(page_title="CV & EIS — Redox Couple", layout="wide")

# --- Imports locaux ---
from config import ASSETS_PATH, CSS_PATH, DATA_PATH
from utils.translations import TRANSLATIONS, get_language, t
from utils.data_loaders import (
    load_cv_mapping,
    load_eis_ferro_mapping,
    load_file_content,
)
from utils.media import load_media_as_base64, display_smart_markdown
from components.filters import (
    render_cv_cascading_filters,
    render_eis_ferro_cascading_filters,
)
from components.chatbot import is_chatbot_enabled, render_chatbot


# --- Chargement CSS externe ---
def load_custom_css():
    """Charge le CSS et les boutons de navigation."""
    css_content = ""
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH, 'r', encoding='utf-8') as f:
            css_content = f.read()

    nav_buttons_html = """
<a href="#top" class="nav-button back-to-top" title="Retour en haut / Back to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 4l-8 8h5v8h6v-8h5z"/>
    </svg>
</a>
<a href="#bottom" class="nav-button scroll-to-bottom" title="Aller en bas / Go to bottom">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 20l8-8h-5V4h-6v8H4z"/>
    </svg>
</a>
<div id="top"></div>
"""
    return f"<style>{css_content}</style>{nav_buttons_html}"


st.markdown(load_custom_css(), unsafe_allow_html=True)


# --- Callbacks pour Navigation (INDEX-based) ---
def on_change_gen():
    selected = st.session_state.get('_radio_gen')
    if selected is not None:
        gen_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["gen_pages"]
        try:
            st.session_state.nav_gen_idx = gen_pages.index(selected)
        except ValueError:
            st.session_state.nav_gen_idx = 0
    st.session_state.nav_model_idx = None
    st.session_state.nav_annex_idx = None


def on_change_model():
    selected = st.session_state.get('_radio_model')
    if selected is not None:
        model_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["model_pages"]
        try:
            st.session_state.nav_model_idx = model_pages.index(selected)
        except ValueError:
            st.session_state.nav_model_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_annex_idx = None


def on_change_annex():
    selected = st.session_state.get('_radio_annex')
    if selected is not None:
        annex_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["annex_pages"]
        try:
            st.session_state.nav_annex_idx = annex_pages.index(selected)
        except ValueError:
            st.session_state.nav_annex_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_model_idx = None


# --- Initialisation Centralisée des États ---
DEFAULT_SESSION_STATES = {
    # Navigation (stocke INDEX, pas texte - indépendant de la langue)
    'nav_gen_idx': 0,
    'nav_model_idx': None,
    'nav_annex_idx': None,
    # CV Visualization
    'run_cv_results': False,
    'files_cv_results': (None, None),
    # EIS ferro Visualization
    'run_eisf_results': False,
    'files_eisf_results': (None, None),
    # Chatbot
    'chat_messages': [],
}

for key, default in DEFAULT_SESSION_STATES.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Initialisation: Accueil (index 0) au premier chargement
if (st.session_state.nav_gen_idx is None and
    st.session_state.nav_model_idx is None and
    st.session_state.nav_annex_idx is None):
    st.session_state.nav_gen_idx = 0


# --- Barre Latérale ---

# Sélecteur de langue
old_lang = st.session_state.get('lang', 'fr')
lang_selection = st.sidebar.radio(
    "Language",
    ["Français", "English"],
    horizontal=True,
    label_visibility="collapsed",
    index=0 if old_lang == "fr" else 1,
)
new_lang = "fr" if "Français" in lang_selection else "en"

# Si la langue change, simplement rerun (les index sont indépendants de la langue)
if new_lang != old_lang:
    st.session_state.lang = new_lang
    st.rerun()

st.session_state.lang = new_lang

st.sidebar.title(t("sidebar_title"))
st.sidebar.markdown("---")

# Navigation par groupes avec callbacks INDEX-based
gen_pages = t("gen_pages")
model_pages = t("model_pages")
annex_pages = t("annex_pages")

st.sidebar.subheader(t("gen_header"))
nav_gen = st.sidebar.radio(
    "Nav Gen",
    gen_pages,
    key="_radio_gen",
    index=st.session_state.nav_gen_idx,
    on_change=on_change_gen,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("models_header"))
nav_model = st.sidebar.radio(
    "Nav Models",
    model_pages,
    key="_radio_model",
    index=st.session_state.nav_model_idx,
    on_change=on_change_model,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("annex_header"))
nav_annex = st.sidebar.radio(
    "Nav Annex",
    annex_pages,
    key="_radio_annex",
    index=st.session_state.nav_annex_idx,
    on_change=on_change_annex,
    label_visibility="collapsed"
)

# --- Chatbot dans la Sidebar ---
if is_chatbot_enabled():
    st.sidebar.markdown("---")
    render_chatbot()

st.sidebar.markdown("---")
st.sidebar.markdown(t("version_info"))

# --- Déterminer la page active ---
# Priorité : modèles > annexes > général
selected_page = None
if st.session_state.nav_model_idx is not None:
    selected_page = model_pages[st.session_state.nav_model_idx]
elif st.session_state.nav_annex_idx is not None:
    selected_page = annex_pages[st.session_state.nav_annex_idx]
elif st.session_state.nav_gen_idx is not None:
    selected_page = gen_pages[st.session_state.nav_gen_idx]
else:
    selected_page = gen_pages[0]


# ===========================================================================
# PAGES
# ===========================================================================

# ===== PAGE ACCUEIL =====
if selected_page == gen_pages[0]:
    st.title(t("title"))
    st.markdown(load_file_content("accueil/accueil.md"))

# ===== PAGE INTRODUCTION =====
elif selected_page == gen_pages[1]:
    st.markdown(load_file_content("intro/intro_cv.md"))

# ===== PAGE DONNÉES ÉLECTROCHIMIQUES =====
elif selected_page == gen_pages[2]:
    st.markdown(load_file_content("data_electrochim/data_electrochim.md"))

# ===== PAGE COMPARAISON =====
elif selected_page == gen_pages[3]:
    st.markdown(load_file_content("intro/comparaison_cv.md"))

# ===== ÉTUDE 1 - CV couple redox sur Au =====
elif selected_page == model_pages[0]:
    st.title(t("title_study_1"))

    tabs = st.tabs(t("tabs_cv_study"))

    # Tab 0: Physics
    with tabs[0]:
        st.markdown(load_file_content("physics/cv_firedrake.md"))

    # Tab 1: Code
    with tabs[1]:
        st.markdown(load_file_content("code/cv_firedrake_code.md"))

    # Tab 2: Results
    with tabs[2]:
        _, df_cv = load_cv_mapping()

        if not df_cv.empty:
            with st.container(border=True):
                c_pop, _ = st.columns([0.3, 0.7])
                with c_pop:
                    with st.popover(t("lbl_avail_sims"), use_container_width=True):
                        st.dataframe(
                            df_cv[['run', 'k0', 'alpha', 'scan_rate', 'delta_Ep', 'ratio']],
                            use_container_width=True, hide_index=True
                        )

                files1 = render_cv_cascading_filters(df_cv, "cr", 1)
                st.divider()
                files2 = render_cv_cascading_filters(df_cv, "cr", 2)

                _, btn1, btn2, _ = st.columns([1, 1, 1, 1])
                with btn1:
                    if st.button(t("btn_launch"), type="primary", key="btn_cv_results"):
                        st.session_state.run_cv_results = True
                        st.session_state.files_cv_results = (files1, files2)
                with btn2:
                    if st.button(t("btn_reset"), type="secondary", key="rst_cv_results"):
                        st.session_state.run_cv_results = False
                        st.rerun()

            # Display results
            if st.session_state.get('run_cv_results', False):
                f1, f2 = st.session_state.files_cv_results

                # Row 1: CV.gif
                st.markdown("### 1. Voltammogramme (GIF)")
                c1, c2 = st.columns(2)
                with c1:
                    if f1 and os.path.exists(f1['gif_cv']):
                        st.markdown(f"**{t('sim_1')}** - Run {f1['run']}")
                        html = load_media_as_base64(f1['gif_cv'])
                        if html:
                            st.markdown(html, unsafe_allow_html=True)
                    else:
                        st.warning(t("image_unavailable"))
                with c2:
                    if f2 and os.path.exists(f2['gif_cv']):
                        st.markdown(f"**{t('sim_2')}** - Run {f2['run']}")
                        html = load_media_as_base64(f2['gif_cv'])
                        if html:
                            st.markdown(html, unsafe_allow_html=True)
                    else:
                        st.warning(t("image_unavailable"))

                st.markdown("---")

                # Row 2: 2D.gif
                st.markdown("### 2. Champ de Concentration 2D (GIF)")
                c1, c2 = st.columns(2)
                with c1:
                    if f1 and os.path.exists(f1['gif_2d']):
                        html = load_media_as_base64(f1['gif_2d'])
                        if html:
                            st.markdown(html, unsafe_allow_html=True)
                    else:
                        st.warning(t("image_unavailable"))
                with c2:
                    if f2 and os.path.exists(f2['gif_2d']):
                        html = load_media_as_base64(f2['gif_2d'])
                        if html:
                            st.markdown(html, unsafe_allow_html=True)
                    else:
                        st.warning(t("image_unavailable"))

                st.markdown("---")

                # Row 3: CV.png
                st.markdown("### 3. Voltammogramme (PNG)")
                c1, c2 = st.columns(2)
                with c1:
                    if f1 and os.path.exists(f1['png_cv']):
                        st.image(f1['png_cv'], use_container_width=True)
                        st.caption(f"Ipa={f1['metrics']['Ipa']:.2f} µA, Ipc={f1['metrics']['Ipc']:.2f} µA, ΔEp={f1['metrics']['delta_Ep']} mV")
                    else:
                        st.warning(t("image_unavailable"))
                with c2:
                    if f2 and os.path.exists(f2['png_cv']):
                        st.image(f2['png_cv'], use_container_width=True)
                        st.caption(f"Ipa={f2['metrics']['Ipa']:.2f} µA, Ipc={f2['metrics']['Ipc']:.2f} µA, ΔEp={f2['metrics']['delta_Ep']} mV")
                    else:
                        st.warning(t("image_unavailable"))

        else:
            st.info(t("gif_coming_soon"))

    # Tab 3: Analysis
    with tabs[3]:
        st.markdown("### Analyse de l'Étude Paramétrique")

        analysis_report_path = os.path.join(DATA_PATH, "cv_analysis/ANALYSE_RAPPORT.md")
        if os.path.exists(analysis_report_path):
            with open(analysis_report_path, 'r', encoding='utf-8') as f:
                st.markdown(f.read())


# ===== ÉTUDE 2 - EIS couple redox sur Au =====
elif selected_page == model_pages[1]:
    st.title(t("title_study_2"))

    tabs_eis_f = st.tabs(t("tabs_eis_ferro"))

    with tabs_eis_f[0]:
        display_smart_markdown(load_file_content("physics/eis_ferro.md"), "physics/eis_ferro.md")

    with tabs_eis_f[1]:
        st.markdown(load_file_content("code/eis_ferro_code.md"))

    with tabs_eis_f[2]:
        df_eis_ferro = load_eis_ferro_mapping()

        if not df_eis_ferro.empty:
            with st.container(border=True):
                c_pop, _ = st.columns([0.3, 0.7])
                with c_pop:
                    with st.popover(t("lbl_avail_sims"), use_container_width=True):
                        st.dataframe(
                            df_eis_ferro[["run", "n_elec", "k0_m_s", "D_m2_s", "conc_mol_m3",
                                          "Q0_uF_cm2", "Rct_measured", "Cdl_eff"]],
                            use_container_width=True, hide_index=True
                        )

                files1 = render_eis_ferro_cascading_filters(df_eis_ferro, "eisf", 1)
                st.divider()
                files2 = render_eis_ferro_cascading_filters(df_eis_ferro, "eisf", 2)

                _, btn1, btn2, _ = st.columns([1, 1, 1, 1])
                with btn1:
                    if st.button(t("btn_launch"), type="primary", key="btn_eisf_results"):
                        st.session_state.run_eisf_results = True
                        st.session_state.files_eisf_results = (files1, files2)
                with btn2:
                    if st.button(t("btn_reset"), type="secondary", key="rst_eisf_results"):
                        st.session_state.run_eisf_results = False
                        st.rerun()

            if st.session_state.get("run_eisf_results", False):
                f1, f2 = st.session_state.files_eisf_results

                st.markdown("### 1. Diagrammes de Nyquist")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and os.path.exists(f["nyquist_png"]):
                            st.markdown(f"**{sim_label}** — Run {f['run']} ({f['label']})")
                            st.image(f["nyquist_png"], use_container_width=True)
                        else:
                            st.warning(t("image_unavailable"))

                st.markdown("---")

                st.markdown("### 2. Diagrammes de Bode")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and os.path.exists(f["bode_png"]):
                            st.image(f["bode_png"], use_container_width=True)
                        else:
                            st.warning(t("image_unavailable"))

                st.markdown("---")

                st.markdown(f"### 3. {t('eis_ferro_metrics_title')}")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and f.get("metrics"):
                            m = f["metrics"]
                            st.markdown(f"**{sim_label}** — Run {f['run']}")
                            mc1, mc2, mc3 = st.columns(3)
                            mc1.metric(t("lbl_Rs"), f"{m['Rs_measured']:.1f}" if isinstance(m['Rs_measured'], (int, float)) else str(m['Rs_measured']))
                            mc2.metric(t("lbl_Rct"), f"{m['Rct_measured']:.1f}" if isinstance(m['Rct_measured'], (int, float)) else str(m['Rct_measured']))
                            mc3.metric(t("lbl_Rct_calc"), f"{m['Rct_calc']:.1f}" if isinstance(m['Rct_calc'], (int, float)) else str(m['Rct_calc']))
                            mc4, mc5, mc6 = st.columns(3)
                            mc4.metric(t("lbl_Cdl_eff"), f"{m['Cdl_eff']:.2e}" if isinstance(m['Cdl_eff'], (int, float)) else str(m['Cdl_eff']))
                            mc5.metric(t("lbl_sigma"), f"{m['sigma_fit']:.1f}" if isinstance(m['sigma_fit'], (int, float)) else str(m['sigma_fit']))
                            mc6.metric(t("lbl_phase_max"), f"{m['phase_max_deg']:.1f}°" if isinstance(m['phase_max_deg'], (int, float)) else str(m['phase_max_deg']))
        else:
            st.info(t("placeholder_coming_soon"))

    with tabs_eis_f[3]:
        st.markdown("### Analyse de l'étude 2 — EIS couple redox sur Au")

        st.markdown("""
L'étude paramétrique de 48 simulations EIS met en évidence les tendances suivantes :

**Effet de n (électrons)** : n=1 → n=3 divise Rct par 9 (facteur n²) et σ par 9.
Le nombre d'électrons est le paramètre le plus influent sur toutes les métriques.

**Effet de k⁰** : augmenter k⁰ de 10⁻⁵ à 10⁻³ m/s réduit Rct de 2 ordres de grandeur.
Pour k⁰ élevé, le semicercle disparaît et seule la droite de Warburg est visible.

**Effet de D** : D affecte uniquement σ (Warburg), pas Rct. D × 10 → σ / √10.

**Effet de c** : la concentration divise à la fois Rct et σ proportionnellement.

**Effet de Q₀** : Q₀ n'affecte ni Rct ni σ, mais modifie la fréquence caractéristique
du semicercle (ω_max) et la capacité effective mesurée.
""")


# ===== PAGES ANNEXES =====
elif selected_page in annex_pages:
    idx = annex_pages.index(selected_page)
    annex_files = [
        "conclusion/cv_conclusion.md",
        "lexique/cv_lexique.md",
        "equations/cv_equations.md",
        "histoire/cv_histoire.md",
        "biblio/cv_biblio.md"
    ]

    try:
        st.markdown(load_file_content(annex_files[idx]))
    except Exception as e:
        st.error(f"Erreur de chargement: {e}")

# --- Ancre de fin de page ---
st.markdown('<div id="bottom"></div>', unsafe_allow_html=True)
