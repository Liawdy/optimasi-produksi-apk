import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import linprog

st.set_page_config(page_title="Aplikasi Matematika Industri", layout="wide")

st.title("📊 Aplikasi Matematika Industri")

tab1, tab2, tab3, tab4 = st.tabs(["Optimasi Produksi", "Model Persediaan", "Model Antrian", "Turunan Parsial"])

# ====================================
# TAB 1: Optimasi Produksi (Linear Programming)
# ====================================
with tab1:
    st.header("1️⃣ Optimasi Produksi (Linear Programming)")
    st.write("Tujuan: Menentukan kombinasi produk yang memaksimalkan keuntungan dengan keterbatasan sumber daya.")
    st.latex(r"Z = 40X + 60Y")

    st.markdown("### Masukkan Koefisien Fungsi Objektif")
    c1 = st.number_input("Keuntungan per unit produk X", value=40)
    c2 = st.number_input("Keuntungan per unit produk Y", value=60)

    # Titik pojok tetap dari studi kasus
    titik1 = (0, 0)
    titik2 = (0, 33.33)
    titik3 = (50, 0)

    # Hitung nilai Z untuk tiap titik pojok
    z1 = c1 * titik1[0] + c2 * titik1[1]
    z2 = c1 * titik2[0] + c2 * titik2[1]
    z3 = c1 * titik3[0] + c2 * titik3[1]

    st.write("### 🔎 Hasil Perhitungan:")
    st.write(f"Z{titik1} = {z1:,.0f}")
    st.write(f"Z{titik2} = {z2:,.0f}")
    st.write(f"Z{titik3} = {z3:,.0f}")

    # Solusi optimal
    z_opt = max(z1, z2, z3)
    if z_opt == z2:
        solusi = f"{titik2}"
    elif z_opt == z3:
        solusi = f"{titik3}"
    else:
        solusi = f"{titik1}"

    st.success(f"💡 Solusi optimal: {solusi} dengan keuntungan maksimum sebesar Rp {z_opt:,.0f}")

    # Visualisasi
    st.markdown("### 📊 Visualisasi Titik Pojok dan Fungsi Objektif")
    fig, ax = plt.subplots()
    ax.plot([titik1[0], titik2[0], titik3[0]], [titik1[1], titik2[1], titik3[1]], 'bo', label="Titik Pojok")
    ax.text(*titik1, f' {titik1}', fontsize=9)
    ax.text(*titik2, f' {titik2}', fontsize=9)
    ax.text(*titik3, f' {titik3}', fontsize=9)

    # Garis fungsi objektif dari titik2 ke titik3 (visualisasi)
    ax.plot([titik2[0], titik3[0]], [titik2[1], titik3[1]], 'r--', label='Garis Fungsi Objektif')
    ax.set_xlim(-5, 60)
    ax.set_ylim(-5, 40)
    ax.set_xlabel("X (Produk Blender)")
    ax.set_ylabel("Y (Produk Pemanggang Roti)")
    ax.set_title("Visualisasi Titik Pojok & Fungsi Objektif")
    ax.legend()
    st.pyplot(fig)

# ====================================
# TAB 2: Model Persediaan (EOQ)
# ====================================
with tab2:
    st.header("2️⃣ Model Persediaan EOQ (Economic Order Quantity)")
    D = st.number_input("Permintaan Tahunan (D)", value=1000)
    S = st.number_input("Biaya Pemesanan per Pesanan (S)", value=50000)
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (H)", value=10000)

    if D > 0 and S > 0 and H > 0:
        EOQ = np.sqrt((2 * D * S) / H)
        st.success(f"Jumlah Pemesanan Ekonomis (EOQ): {EOQ:.2f} unit")

# ====================================
# TAB 3: Model Antrian (M/M/1)
# ====================================
with tab3:
    st.header("3️⃣ Model Antrian (M/M/1)")
    λ = st.number_input("Tingkat Kedatangan (λ)", value=2.0)
    μ = st.number_input("Tingkat Pelayanan (μ)", value=5.0)

    if λ > 0 and μ > λ:
        ρ = λ / μ
        L = ρ / (1 - ρ)
        Lq = ρ**2 / (1 - ρ)
        W = 1 / (μ - λ)
        Wq = λ / (μ * (μ - λ))

        st.write(f"ρ (Utilisasi): {ρ:.2f}")
        st.write(f"L (Jumlah rata-rata dalam sistem): {L:.2f}")
        st.write(f"Lq (Jumlah rata-rata dalam antrian): {Lq:.2f}")
        st.write(f"W (Waktu rata-rata dalam sistem): {W:.2f} satuan waktu")
        st.write(f"Wq (Waktu rata-rata dalam antrian): {Wq:.2f} satuan waktu")
    elif λ >= μ:
        st.error("Tingkat pelayanan harus lebih besar dari tingkat kedatangan untuk menghindari antrian tak hingga.")

# ====================================
# TAB 4: Turunan Parsial
# ====================================
with tab4:
    st.header("4️⃣ Turunan Parsial")
    x, y = sp.symbols('x y')
    fungsi_input = st.text_input("Masukkan fungsi f(x, y):", value="x**2*y + 3*x*y**2")

    try:
        fungsi = sp.sympify(fungsi_input)
        fx = sp.diff(fungsi, x)
        fy = sp.diff(fungsi, y)

        st.latex(r"f(x, y) = " + sp.latex(fungsi))
        st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(fx))
        st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(fy))
    except:
        st.error("Fungsi tidak valid. Gunakan format Python, misal: x**2 * y + 3*x*y**2")
