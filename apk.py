import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri", 
    page_icon = ":star:"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("LogoGeometri-removebg-preview.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang"])
    st.caption("Dibuat dengan :star: oleh **Ramdhan**")

match pilihan: 
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas Persegi adalah {luas:.2} dan Kelilingnya adalah {keliling:.2f} ")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi panjang adalah {luas:.2f} dan Kelilingnya adalah {keliling:.2f} ")
            st.snow()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jarijari = st.number_input("Masukkan Jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari            
            keliling = 2 * 3.14 * jarijari
            st.success(f"Luas Lingkaran adalah {luas:.2f} dan Kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` segitiga")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        if st.button("Hitung", type="primary"):
            luas = 1/2 * alas * tinggi
            st.success(f"Luas Segitiga adalah {luas:.2f}")
            st.snow()

    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `luas` dan `keliling` jajar genjang")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisimiring = st.number_input("Masukkan Sisi Miring")
        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisimiring)
            st.success(f"Luas Jajar genjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.snow()

    case _ :
        st.error("Terjadi kesalahan")