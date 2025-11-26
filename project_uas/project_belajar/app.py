import streamlit as st

# style 
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .title {
        color: #4CAF50;
        font-size: 40px;
        text-align: center;
    }
    .subtitle {
        color: #555;
        font-size: 20px;
        text-align: center;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Selamat Datang di Kalkulator Sederhana</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplikasi kalkulator interaktif dengan fitur multi-page</div>', unsafe_allow_html=True)

# Layout 
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>Kalkulator</h3><p>Lakukan operasi matematika dasar seperti tambah, kurang, kali, bagi, dan pangkat.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Riwayat</h3><p>Lihat riwayat kalkulasi Anda yang tersimpan.</p></div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card"><h3>Tentang</h3><p>Pelajari lebih lanjut tentang aplikasi ini.</p></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card"><h3>Navigasi</h3><p>Gunakan sidebar untuk berpindah halaman.</p></div>', unsafe_allow_html=True)

