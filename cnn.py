import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Judul
st.title("\U0001F4F7 Klasifikasi Alfabet ASL")

# Subjudul
st.subheader("Unggah gambar untuk mendapatkan hasil prediksi")
st.markdown("""
    Di sini, Anda dapat mengunggah gambar alfabet bahasa isyarat ASL, dan sistem kami akan mengklasifikasikannya menjadi salah satu dari kategori berikut:
    
    - A hingga Z \U0001F1E6\U0001F1FF
    - space (spasi)
    - nothing (tidak ada gerakan)
    - del (hapus)
""")

# Input untuk memilih model
model_choice = st.selectbox("Pilih model untuk prediksi:", ["VGG19", "ResNet"])

# Input file gambar
uploaded_files = st.file_uploader("Drag and drop file di sini", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"Jumlah file yang diunggah: {len(uploaded_files)}")

    # Load model berdasarkan pilihan pengguna
    try:
        model_path = {
            "VGG19": "D:\modul6prak\src\CNN(VGG19).h5",
            "ResNet": "D:\modul6prak\src\CNN(RESNET).h5"
        }[model_choice]
        model = tf.keras.models.load_model(model_path)
    except FileNotFoundError:
        st.error(f"Model file tidak ditemukan di lokasi: {model_path}.")
        st.stop()
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat model: {e}")
        st.stop()

    # Daftar kelas sesuai dataset
    class_names = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        'del', 'nothing', 'space'
    ]

    # Fungsi preprocessing
    def preprocess_image(uploaded_image):
        img = Image.open(uploaded_image)
        img = img.convert('RGB')  # Konversi ke RGB jika perlu
        img = img.resize((224, 224))  # Resize ke ukuran input model
        img_array = np.array(img) / 255.0  # Normalisasi
        img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
        return img_array

    # Looping untuk setiap file yang diunggah
    for uploaded_file in uploaded_files:
        st.write(f"*File diunggah:* {uploaded_file.name}")

        # Membaca dan menampilkan gambar
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Gambar: {uploaded_file.name}", use_container_width=True)

        # Preprocessing gambar
        img_array = preprocess_image(uploaded_file)

        # Prediksi
        predictions = model.predict(img_array)
        predicted_class_idx = np.argmax(predictions, axis=1)[0]
        predicted_class = class_names[predicted_class_idx]
        max_prob = predictions[0][predicted_class_idx]

        # Menampilkan hasil prediksi
        confidence_threshold = 0.6  # Threshold minimum untuk prediksi valid
        rejection_threshold = 0.2  # Jika probabilitas terlalu rendah

        if max_prob < rejection_threshold:
            st.error(f"Gambar {uploaded_file.name} tidak valid atau bukan alfabet ASL.")
        elif max_prob >= confidence_threshold:
            st.success(f"Hasil prediksi untuk {uploaded_file.name}: {predicted_class} (Probabilitas: {max_prob:.2f})")
        else:
            st.warning(f"Gambar {uploaded_file.name} tidak dikenali dengan baik. Coba unggah gambar yang lebih jelas.")
else:
    st.info("Silakan unggah file gambar terlebih dahulu untuk melanjutkan.")