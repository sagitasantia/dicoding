# BIKESHARING PROJECT AKHIR DICODING

Proyek ini adalah bagian dari tugas akhir dalam kursus "Belajar Analisis Data dengan Python" di Dicoding. Di sini, saya menganalisis dataset penyewaaan sepeda dan membuat dashboard interaktif berbasis Streamlit. Tahapan yang saya lakukan meliputi pembersihan data, eksplorasi data untuk menemukan pola, serta visualisasi menggunakan grafik interaktif. silahkan akses dashboardnya disini https://penyewaansepeda.streamlit.app/ 

# 1. File Struktur
```plaintext
.
├── dashboard
│   ├── dashboard.py
│   └── df_jam_analisis.csv
│   └── background.jpg
├── data
│   ├── Readme.txt
│   ├── df_hari.csv
│   └── df_jam.csv
├── screenshots
│   ├── Screenshots 1.png
│   ├── Screenshots 2.png
│   ├── Screenshots 3.png
│   ├── Screenshots 4.png
│   └── Screenshots 5.png
├── README.md
├── notebook.ipynb
└── requirements.txt
```
# 2. Langkah-langkah mengerjakan project
## 1. Data Wrangling:
- Mengumpulkan Data: Mengumpulkan data dari sumber yang tersedia, termasuk data hari dan jam.
- Menilai Data: Menilai kualitas data dengan melihat tipe data, missing values, dan duplikat.
- Membersihkan Data: Menghapus atau mengganti nilai yang hilang, duplikat, serta kolom yang tidak relevan.

## 2. Exploratory Data Analysis (EDA) :
- Menentukan Pertanyaan Bisnis : Menyusun pertanyaan bisnis yang ingin dijawab, seperti tren penggunaan berdasarkan waktu dan pengaruh cuaca.
- Eksplorasi Data: Menganalisis data untuk melihat pola, tren, atau informasi penting yang bisa membantu memahami data dengan lebih baik.

## 3. Visualisasi Data:
- Membuat Visualisasi Data: Menampilkan grafik untuk melihat tren musiman, dampak cuaca terhadap penggunaan, serta perbandingan penggunaan antara pengguna kasual dan terdaftar.

## 4. Dashboard
- Mengatur DataFrame yang Akan Digunakan: Menyiapkan data dari DataFrame yang sebelumnya telah dianalisis di Google Colab, termasuk hasil pembersihan dan eksplorasi data, untuk kemudian diintegrasikan ke dalam dashboard.
- Membuat Komponen Filter di Dashboard: Menambahkan filter seperti musim, cuaca, dan suhu untuk memudahkan eksplorasi data.
- Melengkapi Dashboard dengan Visualisasi Data: Melengkapi dashboard dengan grafik-grafik untuk menjawab pertanyaan bisnis.
- Tahapan 1 hingga 3 dilakukan dalam analisis data, sedangkan tahapan 4 dilakukan untuk membuat dashboard menggunakan Streamlit.

# 3. Langkah Menjalankan project
## Notebook.ipynb
### 1. Download file projectnya
### 2. Kemudian buka google colaboratory di website/chroem
### 3. Buat notebook baru di Google Colab.
### 4. upload dan pilih file dengan format .ipynb yang telah didownload tadi
### 5. Hubungkan ke runtime yang sudah di-hosting dengan mengklik "Connect".
### 6. Jalankan kode di notebook dengan menekan tombol "Run" pada setiap cell kode.

## Dashboard/dashboard.py
## Dashboard.py/main.py
### 1. Download file projectnya
### 2. install streamlit di terminal dengan mengetikkan "pip install streamlit"
- Buat file `requirements.txt` yang berisi library yang dibutuhkan seperti pandas, numpy, matplotlib, dan seaborn.
- Install library tersebut dengan mengetikkan `pip install -r requirements.txt` di terminal.
### 3. Pastikan file CSV (dataset) disimpan dalam folder yang sama dengan file dashboard.py atau main.py.
### 4. Buka Visual Studio Code (VSCode), aktifkan virtual environment dengan mengetikkan perintah berikut di terminal:
```
.\venv\Scripts\activate
```
- Jika sudah masuk ke virtual environment, jalankan Streamlit dengan perintah:
```
streamlit run main.py
```
- Jika menggunakan `dashboard.py`, ubah perintahnya menjadi:
```
streamlit run dashboard.py
```
# 4. Screenshots
![image](https://github.com/user-attachments/assets/8bab2c0e-8436-474b-ae72-9c729c7be31b)

![image](https://github.com/user-attachments/assets/cfe868ee-a220-4c5c-9787-3290e6cec4c9)

![image](https://github.com/user-attachments/assets/eddaa5ef-f820-4576-a4bb-6966d371733c)

![image](https://github.com/user-attachments/assets/e857fa4b-2962-486e-a285-03591d792afe)

![image](https://github.com/user-attachments/assets/59d4fb6b-51fd-43bf-adce-5f6efef192f4)






