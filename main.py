import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# dataset dari URL
url_day = 'https://raw.githubusercontent.com/sagitasantia/dataset_bike/main/day.csv'
df_harian = pd.read_csv(url_day)

#  Menghapus nilai NaN dan duplikat
df_harian_clean = df_harian.dropna().drop_duplicates()

with st.sidebar:
    st.title("Dashboard Penyewaan Sepeda")
    st.write("Rentang Waktu")
    tanggal_awal = st.date_input("Mulai", value=pd.to_datetime('2011-01-01'))
    tanggal_akhir = st.date_input("Akhir", value=pd.to_datetime('2012-12-31'))
    st.write(f"Data dari {tanggal_awal} hingga {tanggal_akhir}")

df_harian_clean['dteday'] = pd.to_datetime(df_harian_clean['dteday'])
df_filtered = df_harian_clean[(df_harian_clean['dteday'] >= pd.to_datetime(tanggal_awal)) & 
                              (df_harian_clean['dteday'] <= pd.to_datetime(tanggal_akhir))]

st.header("Analisis Penyewaan Sepeda")

# Analisis Penyewaan Sepeda Berdasarkan Hari Kerja vs Hari Libur
st.subheader("Perbandingan Penyewaan Sepeda Berdasarkan Hari Kerja vs Hari Libur")

# Analisis Hari Kerja vs Hari Libur
st.write("""
    Analisis ini bertujuan untuk melihat perbandingan jumlah penyewaan sepeda pada hari kerja dan hari libur.
    Hal ini penting untuk mengetahui apakah pengguna lebih banyak menyewa sepeda di hari kerja atau di hari libur.
    """)
# Plot Perbandingan Penyewaan Sepeda (Hari Kerja vs Hari Libur)
fig, ax = plt.subplots()
sns.barplot(x='holiday', y='cnt', data=df_filtered, ci=None, ax=ax)
ax.set_title("Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
ax.set_xlabel("Hari Libur (0: Hari Kerja, 1: Hari Libur)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# Analisis Penyewaan Berdasarkan Kondisi Cuaca
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")

# Analisis Pengaruh Cuaca
st.write("""
    Dalam analisis ini, kita melihat pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda.
    Cuaca yang berbeda dapat mempengaruhi keputusan seseorang untuk menyewa sepeda.
    """)
# Plot Pengaruh Kondisi Cuaca
fig, ax = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=df_filtered, ax=ax)
ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
ax.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Kabut, 3: Hujan)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# Menampilkan data summary 
st.subheader("Ringkasan Data Penyewaan Sepeda")
st.write(df_filtered.describe())

