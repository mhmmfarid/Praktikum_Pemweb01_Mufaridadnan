import streamlit as st

st.title("Riwayat Kalkulasi")
st.write("Lihat kalkulasi sebelumnya.")

if 'history' in st.session_state and st.session_state.history:
    st.subheader("Daftar Riwayat")
    # Looping riwayat
    for i, calc in enumerate(st.session_state.history, start=1):
        st.write(f"{i}. {calc}")
    #  clear 
    if st.button("Hapus Riwayat"):
        st.session_state.history = []
        st.success("Riwayat dihapus!")
else:
    st.info("Belum ada riwayat. Lakukan kalkulasi di halaman Kalkulator.")