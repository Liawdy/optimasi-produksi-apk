import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ==============================
# Konfigurasi Halaman
# ==============================
st.set_page_config(page_title="Optimasi Produksi", layout="centered")

st.title("1️⃣ Optimasi Produksi (Linear Programming)")

# ==============================
# Deskripsi Studi Kasus
# ==============================
st.markdown("""
### 🔧 Studi Kasus
PT Prima Citra Indonesia memproduksi **Sepatu (X)** dan **Tas (Y)**. Untuk mengetahui jumlah penjualan dan keuntungan dari produksi, pemilik menggunakan model matematika berikut:
""")

st.latex(r"Z = c_1 X + c_2 Y")

st.markdown("### 📘 Keterangan Notasi:")
st.markdown(r"""
- $Z$  = Total keuntungan  
- $c_1$ = Keuntungan per unit Sepatu (X)  
- $c_2$ = Keuntungan per unit Tas (Y)  
- $X$  = Jumlah unit Sepatu  
- $Y$  = Jumlah unit Tas
""")

# ==============================
# Input Pengguna
# ==============================
st.markdown("### 📥 Masukkan Nilai Produksi")

col1, col2 = st.columns(2)
with col1:
    x = st.number_input("Jumlah Produksi Sepatu (X)", value=0)
    laba_sepatu = st.number_input("Keuntungan per Sepatu (c₁)", value=0)
    harga_sepatu = st.number_input("Harga Jual Sepatu", value=0)
with col2:
    y = st.number_input("Jumlah Produksi Tas (Y)", value=0)
    laba_tas = st.number_input("Keuntungan per Tas (c₂)", value=0)
    harga_tas = st.number_input("Harga Jual Tas", value=0)

# ==============================
# Fungsi Format Rupiah
# ==============================
def format_rupiah(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

# ==============================
# Perhitungan Fungsi Tujuan Z
# ==============================
if all([x, y, laba_sepatu, laba_tas]):
    Z = laba_sepatu * x + laba_tas * y

    st.subheader("🧮 Perhitungan Fungsi Tujuan Z")
    st.latex(rf"""
    \begin{{align*}}
    Z &= c_1 \cdot X + c_2 \cdot Y \\
      &= {laba_sepatu} \cdot {x} + {laba_tas} \cdot {y} \\
      &= {Z:,.0f}
    \end{{align*}}
    """)

    # Biaya Produksi = Harga Jual - Laba
    biaya_sepatu = harga_sepatu - laba_sepatu
    biaya_tas = harga_tas - laba_tas

    # ==============================
    # Perhitungan Penjualan dan Keuntungan
    # ==============================
    total_penjualan_sepatu = harga_sepatu * x
    total_penjualan_tas = harga_tas * y
    total_penjualan = total_penjualan_sepatu + total_penjualan_tas

    total_laba_sepatu = laba_sepatu * x
    total_laba_tas = laba_tas * y
    total_laba = total_laba_sepatu + total_laba_tas

    # ==============================
    # Output Ringkasan
    # ==============================
    st.markdown("### 💰 Total Penjualan")
    st.write(f"Sepatu: {format_rupiah(total_penjualan_sepatu)}")
    st.write(f"Tas: {format_rupiah(total_penjualan_tas)}")
    st.write(f"Total: {format_rupiah(total_penjualan)}")

    st.markdown("### 💵 Total Keuntungan")
    st.write(f"Sepatu: {format_rupiah(total_laba_sepatu)}")
    st.write(f"Tas: {format_rupiah(total_laba_tas)}")
    st.write(f"Total: {format_rupiah(total_laba)}")

    # ==============================
    # Grafik Perbandingan
    # ==============================
    st.markdown("### 📊 Diagram Perbandingan")

    kategori = ['Sepatu (X)', 'Tas (Y)', 'Total']
    penjualan = [total_penjualan_sepatu, total_penjualan_tas, total_penjualan]
    keuntungan = [total_laba_sepatu, total_laba_tas, total_laba]

    x_pos = np.arange(len(kategori))
    width = 0.35

    fig, ax = plt.subplots()

    bar1 = ax.bar(x_pos - width/2, keuntungan, width=width, label='Keuntungan', color='skyblue')
    bar2 = ax.bar(x_pos + width/2, penjualan, width=width, label='Penjualan', color='lightgreen')

    max_val = max(penjualan + keuntungan)
    ax.set_ylim(0, max_val * 1.3)

    for bars in [bar1, bar2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + max_val*0.03,
                    f"{height:,.0f}".replace(",", "."), ha='center', va='bottom', fontsize=10)

    ax.set_ylabel("Rupiah")
    ax.set_title("Perbandingan Penjualan dan Keuntungan")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(kategori)
    ax.legend()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'.replace(",", ".")))

    st.pyplot(fig)
else:
    st.info("Silakan isi semua nilai input terlebih dahulu.")
