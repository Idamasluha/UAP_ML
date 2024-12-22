# UAP_ML
## Author
202110370311372-Ida masluha

# Klasifikasi ASL Alphabet

## Deskripsi Proyek
Proyek ini bertujuan untuk membangun model kecerdasan buatan berbasis Convolutional Neural Network (CNN) 
untuk mengenali huruf-huruf dalam Bahasa Isyarat Amerika (American Sign Language/ASL).
Model yang digunakan dalam proyek ini adalah dua arsitektur CNN, yaitu VGG19 dan ResNet.

## Informasi Dataset
- LINK DATASET : https://www.kaggle.com/datasets/grassknoted/asl-alphabet?resource=download

Dataset yang digunakan adalah ASL Alphabet Dataset, yang berisi 87.000 gambar tangan yang merepresentasikan 29 kelas. 
Kelas-kelas tersebut mencakup 26 huruf alfabet (A-Z) dan beberapa simbol tambahan. 
Setiap kelas memiliki ribuan gambar, sehingga dataset ini saya pilih untuk membangun model klasifikasi berbasis deep learning.

## Langkah-Langkah Klasifikasi ASL
- a. Pembagian Data: 
Dataset dibagi menjadi dua bagian, yaitu 80% untuk data train, 10% data test dan 10% untuk data val.

- b. Eksplorasi Data: 
Dilakukan analisis terhadap dataset untuk melihat distribusi data di setiap kelas.

- c. Preprocessing Data: 
Gambar diproses lebih lanjut untuk meningkatkan performa model.

- d. Klasifikasi: 
Gambar diklasifikasikan menggunakan dua model CNN, yaitu VGG19 dan ResNet, untuk membandingkan performa keduanya kemudian untuk modelnya disave. 

## Evaluasi MODEL 
- 1. MODEL VGG19
  ![Screenshot 2024-12-22 200138](https://github.com/user-attachments/assets/d34308ed-b5de-4b0e-ae77-ac0bbfe5635b)
  ![Screenshot 2024-12-22 200149](https://github.com/user-attachments/assets/78095c08-5677-49b2-ac14-58b483c84a9a)

- 2. MODEL RESNET
     ![Screenshot 2024-12-22 200527](https://github.com/user-attachments/assets/fffa61c3-af3a-48de-98fb-6ffb92b1abcc)
     ![Screenshot 2024-12-22 200536](https://github.com/user-attachments/assets/162fc05a-7f56-4fea-977f-d6af67659c18)

## Deployment Web
Setelah model selesai dibuat dan disimpan, langkah selanjutnya adalah melakukan deployment menggunakan Streamlit untuk membuat aplikasi berbasis web. 
Aplikasi ini dirancang untuk memprediksi huruf yang ditampilkan dalam gambar yang diunggah pengguna, sekaligus memberikan probabilitas dari setiap prediksi. 
Model yang digunakan untuk membangun aplikasi adalah CNN dengan arsitektur VGG19, 
karena model ini menunjukkan performa terbaik setelah dilakukan evaluasi terhadap kedua model.
