import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

st.set_page_config(page_title="Optimasi Produksi", layout="centered")

st.title("Aplikasi Optimasi Produksi")

# ✅ Tambahkan definisi tab1
tab1, = st.tabs(["Optimasi Produksi"])

# ================================================
# Optimasi Produksi (Linear Programming)
# ================================================

with tab1:
    st.header("1️⃣ Optimasi Produksi (Linear Programming)")
    st.markdown("""
    ### 🔧 Studi Kasus
    PT Prima Citra Indonesia yang merupakan sebuah perusahaan yang memproduksi **Sepatu (X)** dan **Tas (Y)**. 
    Untuk mengetahui berapa banyak penjualan dan keuntungan pada hasil produksi, pemiliknya menggunakan perhitungan 
    matematika dengan rumus:
    """)

    st.latex(r"Z = c₁X + c₂Y")
    st.markdown("### 📘 Keterangan Notasi Model Optimasi Produksi:")
    st.markdown(r"""
    - $Z$  = Total biaya atau total keuntungan  
    - $c₁$ = Biaya atau keuntungan per unit X  
    - $c₂$ = Biaya atau keuntungan per unit Y  
    - $X$  = Jumlah unit produk (misal: Sepatu)  
    - $Y$  = Jumlah unit produk (misal: Tas)
    """)

    # Input Harga dan Keuntungan
    st.markdown("### Harga Jual dan Keuntungan per Unit")
    col1, col2= st.columns(2)
    with col1:
        x = st.number_input("Jumlah Produksi Sepatu (X)", value=0)
        laba_sepatu = st.number_input("Keuntungan per Sepatu (c₁)", value=0)
        harga_sepatu = st.number_input("Harga Jual sepatu", value=0)
    with col2:
        y = st.number_input("Jumlah Produksi Tas (Y)", value=0)
        laba_tas = st.number_input("Keuntungan per Tas (c₂)", value=0)
        harga_tas = st.number_input("Harga Jual Tas", value=0)

    # Hitung Fungsi Tujuan
    if all([laba_sepatu, laba_tas, x, y]):
        Z = laba_sepatu * x + laba_tas * y

        st.subheader("🧮 Perhitungan Berdasarkan Input")
        st.latex(rf"""
        \begin{{align*}}
        Z &= c_1 \cdot X + c_2 \cdot Y \\
          &= {laba_sepatu} \cdot {x} + {laba_tas} \cdot {y} \\
          &= {Z:,.0f}
        \end{{align*}}
        """)

        # Hitung biaya produksi
        biaya_sepatu = harga_sepatu - laba_sepatu
        biaya_tas = harga_tas - laba_tas

        # Format rupiah
        def format_rupiah(nilai):
            return f"Rp {nilai:,.0f}".replace(",", ".")

        # Hasil Fungsi Tujuan
        z1 = laba_sepatu * x + laba_tas * y
        z2 = laba_sepatu * x
        z3 = laba_tas * y

        st.markdown("### 🔎 Hasil Fungsi Tujuan Z:")
        st.write(f"Z({x}, {y}) = {format_rupiah(z1)}")
        st.write(f"Z({x}, 0) = {format_rupiah(z2)}")
        st.write(f"Z(0, {y}) = {format_rupiah(z3)}")

        # Ringkasan Penjualan
        st.markdown("### 💰 Ringkasan Total Penjualan")

        total_penjualan_sepatu = harga_sepatu * x
        total_penjualan_tas = harga_tas * y
        total_penjualan = total_penjualan_sepatu + total_penjualan_tas

        st.write(f"🪑 Penjualan sepatu (X): {format_rupiah(total_penjualan_sepatu)}")
        st.write(f"🪑 Penjualan tas (Y): {format_rupiah(total_penjualan_tas)}")
        st.write(f"📊 Total Penjualan: {format_rupiah(total_penjualan)}")

        # Total Keuntungan Bersih
        st.markdown("### 🧾 Total Keuntungan Bersih")

        total_laba_sepatu = laba_sepatu * x
        total_laba_tas = laba_tas * y
        total_keuntungan_bersih = total_laba_sepatu + total_laba_tas

        st.write(f"🔹 Keuntungan Sepatu (X): {format_rupiah(z2)}")
        st.write(f"🔹 Keuntungan Tas (Y): {format_rupiah(z3)}")
        st.write(f"✅ Total Keuntungan Bersih: {format_rupiah(total_keuntungan_bersih)}")

        # Grafik Perbandingan
        st.markdown("### 📊 Diagram Perbandingan Penjualan dan Keuntungan")

        kategori = ['Sepatu (X)', 'Tas (Y)', 'Total']
        penjualan = [total_penjualan_sepatu, total_penjualan_tas, total_penjualan]
        keuntungan = [total_laba_sepatu, total_laba_tas, total_keuntungan_bersih]

        x_pos = np.arange(len(kategori))
        width = 0.35
        fig2, ax2 = plt.subplots()

        bar1 = ax2.bar(x_pos - width/2, keuntungan, width=width, color='skyblue', label='Keuntungan')
        bar2 = ax2.bar(x_pos + width/2, penjualan, width=width, color='lightgreen', label='Penjualan')

        max_val = max(penjualan + keuntungan)
        ax2.set_ylim(0, max_val * 1.3)

        for bars in [bar1, bar2]:
            for bar in bars:
                value = bar.get_height()
                ax2.text(
                    bar.get_x() + bar.get_width() / 2,
                    value + max_val * 0.03,
                    f"{value:,.0f}".replace(",", "."),
                    ha='center', va='bottom',
                    fontsize=10
                )

        ax2.set_ylabel("Rupiah", fontsize=10)
        ax2.set_xlabel("Kategori Produk", fontsize=10)
        ax2.set_title("Perbandingan Penjualan dan Keuntungan", fontsize=12)
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(kategori, fontsize=10)
        ax2.legend(fontsize=10)
        ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'.replace(",", ".")))

        plt.tight_layout()
        st.pyplot(fig2)
