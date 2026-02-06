"""Composants de filtres en cascade — Couple redox ferro/ferricyanure."""
import os
import pandas as pd
import streamlit as st

from config import DATA_PATH
from utils.translations import t


def render_cv_cascading_filters(df_origin: pd.DataFrame, key_prefix: str, sim_num: int) -> dict | None:
    """
    Génère les filtres en cascade pour l'étude CV (3 paramètres).

    Args:
        df_origin: DataFrame source avec toutes les combinaisons
        key_prefix: Préfixe pour les clés des widgets
        sim_num: 1 ou 2 (pour l'index par défaut différent)

    Returns:
        Dict avec chemins des fichiers ou None si non trouvé
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else (1 if len(df) > 1 else 0)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    # 3 paramètres sur une ligne
    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])

    with c1:
        # Filter 1: k0 (scientific notation, sorted by float value)
        k0_opts = sorted(df['k0'].unique(), key=lambda x: float(x))
        idx = min(default_idx, len(k0_opts) - 1)
        val_k0 = st.selectbox(t("lbl_k0"), k0_opts, key=f"{key_prefix}_k{sim_num}", index=idx)
        df = df[df['k0'] == val_k0]

    with c2:
        # Filter 2: alpha (filtered by k0)
        alpha_opts = sorted(df['alpha'].unique())
        val_alpha = st.selectbox(t("lbl_alpha"), alpha_opts, key=f"{key_prefix}_a{sim_num}")
        df = df[df['alpha'] == val_alpha]

    with c3:
        # Filter 3: scan_rate (filtered by alpha)
        sr_opts = sorted(df['scan_rate'].unique())
        val_sr = st.selectbox(t("lbl_scan_rate"), sr_opts, key=f"{key_prefix}_sr{sim_num}")
        df = df[df['scan_rate'] == val_sr]

    if not df.empty:
        row = df.iloc[0]
        return {
            'gif_cv': os.path.join(DATA_PATH, "cv_parametric_study/gif", row['file_gif_cv']),
            'gif_2d': os.path.join(DATA_PATH, "cv_parametric_study/gif_2d", row['file_gif_2d']),
            'png_cv': os.path.join(DATA_PATH, "cv_parametric_study/png", row['file_png_cv']),
            'png_conc': os.path.join(DATA_PATH, "cv_parametric_study/png", row['file_png_conc']),
            'metrics': {
                'Ipa': row['Ipa'], 'Ipc': row['Ipc'],
                'ratio': row['ratio'], 'delta_Ep': row['delta_Ep'],
                'Epa': row.get('Epa', ''), 'Epc': row.get('Epc', '')
            },
            'run': row['run']
        }
    return None


def render_eis_ferro_cascading_filters(df_origin: pd.DataFrame, key_prefix: str, sim_num: int) -> dict | None:
    """
    Filtres en cascade pour l'étude EIS ferro/ferri (5 paramètres).
    n_elec → k0 → D → conc → Q0
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else (1 if len(df) > 1 else 0)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, c4, c5, _ = st.columns([0.3, 1, 1, 1, 1, 1, 0.3])

    with c1:
        n_opts = sorted(df["n_elec"].unique())
        idx = min(default_idx, len(n_opts) - 1)
        val_n = st.selectbox(t("lbl_n_elec"), n_opts, key=f"{key_prefix}_n{sim_num}", index=idx)
        df = df[df["n_elec"] == val_n]

    with c2:
        k0_opts = sorted(df["k0_m_s"].unique())
        idx2 = min(default_idx, len(k0_opts) - 1)
        val_k0 = st.selectbox(t("lbl_k0"), k0_opts, key=f"{key_prefix}_k0{sim_num}", index=idx2)
        df = df[df["k0_m_s"] == val_k0]

    with c3:
        D_opts = sorted(df["D_m2_s"].unique())
        val_D = st.selectbox(t("lbl_D"), D_opts, key=f"{key_prefix}_D{sim_num}")
        df = df[df["D_m2_s"] == val_D]

    with c4:
        c_opts = sorted(df["conc_mol_m3"].unique())
        val_c = st.selectbox(t("lbl_conc"), c_opts, key=f"{key_prefix}_c{sim_num}")
        df = df[df["conc_mol_m3"] == val_c]

    with c5:
        Q_opts = sorted(df["Q0_uF_cm2"].unique())
        val_Q = st.selectbox(t("lbl_Q0"), Q_opts, key=f"{key_prefix}_Q{sim_num}")
        df = df[df["Q0_uF_cm2"] == val_Q]

    if not df.empty:
        row = df.iloc[0]
        run_id = int(row["run"])
        run_dir = os.path.join(DATA_PATH, "eis_ferro_study", f"run_{run_id:03d}")
        return {
            "nyquist_png": os.path.join(run_dir, "Nyquist.png"),
            "bode_png": os.path.join(run_dir, "Bode.png"),
            "run": run_id,
            "label": f"n={int(row['n_elec'])}, k0={row['k0_m_s']:.0e}",
            "metrics": {
                "Rs_measured": row.get("Rs_measured", ""),
                "Rct_measured": row.get("Rct_measured", ""),
                "Rct_calc": row.get("Rct_calc", ""),
                "Cdl_eff": row.get("Cdl_eff", ""),
                "sigma_fit": row.get("sigma_fit", ""),
                "omega_max": row.get("omega_max", ""),
                "phase_max_deg": row.get("phase_max_deg", ""),
            }
        }
    return None
