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

    # ===============================
    # Input Harga dan Keuntungan
    # ===============================
    st.markdown("### Harga Jual dan Keuntungan per Unit")
    col1, col2= st.columns(2)
    with col1:
        x = st.number_input("Jumlah Produksi Sepatu (X)", value=0)
        laba_Sepatu = st.number_input("Keuntungan per Sepatu (c₁)", value=0)
        harga_sepatu = st.number_input("Harga Jual sepatu", value=0)
    with col2:
        y = st.number_input("Jumlah Produksi Tas (Y)", value=0)
        laba_Tas = st.number_input("Keuntungan per Tas (c₂)", value=0)
        harga_Tas = st.number_input("Harga Jual Tas", value=0)

    if all([laba_Sepatu, laba_Tas, x, y]):
        Z = laba_Sepatu * x + laba_Tas * y
    
        st.subheader("🧮 Perhitungan Berdasarkan Input")
        st.latex(rf"""
        \begin{{align*}}
        Z &= c_1 \cdot X + c_2 \cdot Y \\
          &= {laba_Sepatu} \cdot {x} + {laba_Tas} \cdot {y} \\
          &= {Z:,.0f}
        \end{{align*}}
        """)

    # Hitung biaya produksi dari selisih harga dan keuntungan
    biaya_sepatu = harga_sepatu - laba_sepatu
    biaya_tas = harga_tas - laba_tas
    
    # ===============================
    # Fungsi Format Rupiah
    # ===============================
    def format_rupiah(nilai):
        return f"Rp {nilai:,.0f}".replace(",", ".")

    # ===============================
    # Perhitungan Fungsi Tujuan Z
    # ===============================
    z1 = laba_sepatu * x + laba_tas *y
    z2 = laba_sepatu * x
    z3 = laba_tas * y

    st.markdown("### 🔎 Hasil Fungsi Tujuan Z:")
    st.write(f"Z({x}, {y}) = {format_rupiah(z1)}")
    st.write(f"Z({x}, 0) = {format_rupiah(z2)}")
    st.write(f"Z(0, {y}) = {format_rupiah(z3)}")

    z_opt = max(z1, z2, z3)
    if z_opt == z2:
        solusi = f"(0, {x})"
    elif z_opt == z3:
        solusi = f"({y}, 0)"
    else:
        solusi = "(0, 0)"

    # ===============================
    # Total Penjualan dan Keuntungan
    # ===============================
    st.markdown("### 💰 Ringkasan Total Penjualan")

    total_penjualan_sepatu = harga_sepatu * x
    total_penjualan_tas = harga_tas * y
    total_penjualan = total_penjualan_sepatu + total_penjualan_tas

    st.write(f"🪑 Penjualan sepatu (X): {format_rupiah(total_penjualan_sepatu)}")
    st.write(f"🪑 Penjualan tas (Y): {format_rupiah(total_penjualan_tas)}")
    st.write(f"📊 Total Penjualan: {format_rupiah(total_penjualan)}")

    # ===============================
    # Total Biaya Produksi & Laba Bersih
    # ===============================
    st.markdown("### 🧾 Total Keuntungan Bersih")

    total_biaya_sepatu = biaya_sepatu * x
    total_biaya_tas = biaya_tas * y
    total_biaya_produksi = total_biaya_sepatu + total_biaya_tas

    total_laba_sepatu = laba_sepatu * x
    total_laba_tas = laba_tas * y
    total_keuntungan_bersih = total_laba_sepatu + total_laba_tas

    st.write(f"🔹 Keuntungan Sepatu (X): {format_rupiah(z2)}")
    st.write(f"🔹 Keuntungan Tas (Y): {format_rupiah(z3)}")
    st.write(f"✅ Total Keuntungan Bersih: {format_rupiah(z2 + z3)}")

    # ===============================
    # Grafik Perbandingan (Diagram Batang Vertikal)
    # ===============================
    st.markdown("### 📊 Diagram Perbandingan Penjualan dan Keuntungan")
    
    # Data per kategori
    kategori = ['Sepatu (X)', 'Tas (Y)', 'Total']
    penjualan = [total_penjualan_sepatu, total_penjualan_tas, total_penjualan]
    keuntungan = [total_laba_sepatu, total_laba_tas, total_keuntungan_bersih]
    
    # Grafik
    x_pos = np.arange(len(kategori))
    width = 0.35
    fig2, ax2 = plt.subplots()
    
    # Buat batang grafik
    bar1 = ax2.bar(x_pos - width/2, keuntungan, width=width, color='skyblue', label='Keuntungan')
    bar2 = ax2.bar(x_pos + width/2, penjualan, width=width, color='lightgreen', label='Penjualan')
    
    # Gabungan semua nilai untuk menentukan batas Y
    values = penjualan + keuntungan
    max_val = max(values)
    ax2.set_ylim(0, max_val * 1.3)  # Ruang ekstra di atas grafik
    
    # Label angka tetap (tidak menempel batang)
    for bars in [bar1, bar2]:
        for bar in bars:
            value = bar.get_height()
            text = f"{value:,.0f}".replace(",", ".")
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                value + (max_val * 0.03),  # Jarak 3% dari tinggi maksimal
                text,
                ha='center', va='bottom',
                fontsize=10,
                color='black',
                fontweight='bold'
            )
    
    # Pengaturan axis dan label
    ax2.set_ylabel("Rupiah", fontsize=10)
    ax2.set_xlabel("Kategori Produk", fontsize=10)
    ax2.set_title("Perbandingan Penjualan dan Keuntungan", fontsize=12)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(kategori, fontsize=10)
    ax2.legend(fontsize=10)
    
    # Format angka di sumbu Y
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'.replace(",", ".")))
    
    plt.tight_layout()
    st.pyplot(fig2)
