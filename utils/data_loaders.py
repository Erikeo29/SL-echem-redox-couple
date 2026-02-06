"""Fonctions de chargement des données — Couple redox ferro/ferricyanure."""
import os
import pandas as pd
import streamlit as st

from config import DATA_PATH, DOC_PATH
from utils.translations import get_language


@st.cache_data(ttl=600)
def load_cv_mapping():
    """Charge le mapping CV et retourne (mapping_dict, DataFrame)."""
    try:
        csv_path = os.path.join(DATA_PATH, 'cv_parametric_study/cv_mapping.csv')
        df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        mapping = {}
        for _, row in df.iterrows():
            key = (str(row['k0']), float(row['alpha']), float(row['scan_rate']))
            mapping[key] = {
                'gif_cv': os.path.join(DATA_PATH, "cv_parametric_study/gif", row['file_gif_cv']),
                'gif_2d': os.path.join(DATA_PATH, "cv_parametric_study/gif_2d", row['file_gif_2d']),
                'png_cv': os.path.join(DATA_PATH, "cv_parametric_study/png", row['file_png_cv']),
                'png_conc': os.path.join(DATA_PATH, "cv_parametric_study/png", row['file_png_conc']),
                'metrics': {
                    'Ipa': row['Ipa'], 'Ipc': row['Ipc'],
                    'ratio': row['ratio'], 'delta_Ep': row['delta_Ep']
                }
            }
        return mapping, df
    except Exception:
        return {}, pd.DataFrame()


@st.cache_data(ttl=600)
def load_eis_ferro_mapping():
    """Charge le CSV de l'étude EIS ferro/ferri sur Au."""
    try:
        csv_path = os.path.join(DATA_PATH, 'eis_ferro_study/parametric_summary.csv')
        df = pd.read_csv(csv_path, sep=',', encoding='utf-8')
        return df
    except Exception:
        return pd.DataFrame()


def load_file_content(relative_path: str) -> str:
    """Charge un fichier depuis docs/<lang>/relative_path."""
    lang = get_language()
    full_path = os.path.join(DOC_PATH, lang, relative_path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return f"Document not found: {relative_path}"
