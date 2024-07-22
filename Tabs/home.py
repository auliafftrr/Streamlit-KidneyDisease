import streamlit as st
from PIL import Image

def app():
    # Judul halaman aplikasi
    st.title ("Prediksi Penyakit Ginjal")

    # Menambahkan gambar medis
    image = Image.open("D:/Kidney/ginjalku.jpg")
    st.image(image, caption='Ilustrasi Medis', use_column_width=True)

    # CSS untuk styling
    st.markdown("""
        <style>
        body {
            background-color: #4E342E;
            color: #FFFFFF;
        }
        .main {
            background-color: #58D6E63;
            padding: 20px;
            border-radius: 10px;
            color: #FFFFFF;
        }
        .stImage > img {
            border-radius: 10px;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #D7CCC8;
        }
        .stMarkdown p {
            font-size: 16px;
            line-height: 1.6;
            color: #FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True)

    # Deskripsi tambahan
    st.write("""
    <div class="main">
        <p>Selamat datang di aplikasi Prediksi Penyakit Ginjal.</p>
        <p>Aplikasi ini bertujuan untuk membantu memprediksi kemungkinan seseorang terkena penyakit ginjal berdasarkan informasi medis yang diberikan.</p>
        <p>Penyakit ginjal adalah kondisi di mana ginjal tidak dapat berfungsi dengan baik, yang dapat disebabkan oleh berbagai faktor seperti diabetes, hipertensi, dan infeksi.</p>
        <p>Silakan navigasikan ke halaman 'Prediction' untuk mulai menggunakan aplikasi.</p>
    </div>
    """, unsafe_allow_html=True)

