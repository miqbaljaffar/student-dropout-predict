import streamlit as st
import pandas as pd
import joblib
import numpy as np # Berguna untuk beberapa konversi tipe data jika diperlukan

# --- KONFIGURASI AWAL & PEMUATAN MODEL ---

# Judul Aplikasi
st.set_page_config(page_title="Prediksi Dropout Mahasiswa",
                   page_icon="🎓",
                   layout="wide")

st.title("🎓 Prediksi Potensi Dropout Mahasiswa")
st.write("""
Aplikasi ini membantu Jaya Jaya Institut untuk memprediksi apakah seorang mahasiswa
berpotensi melakukan dropout, lulus, atau masih terdaftar berdasarkan data mereka.
Masukkan data mahasiswa di bawah ini untuk mendapatkan prediksi.
""")

# Fungsi untuk memuat model pipeline (preprocessor + classifier)
@st.cache_resource # Menggunakan cache resource agar model tidak di-load ulang setiap interaksi
def load_model(model_path="best_dropout_prediction_model_random_forest.pkl"): # GANTI NAMA FILE JIKA PERLU
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Error: File model '{model_path}' tidak ditemukan. Pastikan file model ada di direktori yang sama dengan app.py.")
        return None
    except Exception as e:
        st.error(f"Error saat memuat model: {e}")
        return None

model_pipeline = load_model()

# --- MAPPING UNTUK FITUR KATEGORIKAL (CONTOH) ---
# Anda HARUS menyesuaikan ini berdasarkan dataset Anda dan bagaimana Anda melatih model
# Kunci adalah nilai yang akan dikirim ke model (biasanya numerik jika model dilatih demikian)
# Nilai adalah apa yang ditampilkan ke pengguna

# Contoh (sesuaikan dengan dataset Anda!)
marital_status_options = {
    1: "Lajang (Single)", 2: "Menikah (Married)", 3: "Duda/Janda (Widower)",
    4: "Bercerai (Divorced)", 5: "Common-Law Union (Facto Union)", 6: "Berpisah secara Hukum (Legally Separated)"
}
attendance_options = {1: "Siang Hari (Daytime)", 0: "Malam Hari (Evening)"} # Asumsi 1=Siang, 0=Malam, sesuaikan!
yes_no_options = {1: "Ya", 0: "Tidak"}
gender_options = {1: "Laki-laki (Male)", 0: "Perempuan (Female)"} # Asumsi 1=Laki-laki, 0=Perempuan

# Target mapping (sesuaikan dengan yang Anda gunakan di Colab)
status_mapping = {
    1: "Berpotensi Dropout", # Sesuai dengan Target = 1 di Colab
    0: "Cenderung Lulus (Graduate)",   # Sesuai dengan Target = 0 di Colab
    2: "Cenderung Masih Terdaftar/Aktif (Enrolled)" # Sesuai dengan Target = 2 di Colab
}


# --- FUNGSI UNTUK MENGUMPULKAN INPUT ---
def get_user_input():
    st.sidebar.header("Masukkan Data Mahasiswa:")
    input_features = {}

    # Buat kolom untuk layout yang lebih baik
    col1, col2, col3 = st.sidebar.columns(3)

    # Contoh input fields - Anda HARUS melengkapi semua fitur yang digunakan model.
    # Perhatikan nama kunci di input_features harus SAMA PERSIS dengan nama kolom di X_train
    # sebelum preprocessing.

    with col1:
        input_features['Marital_status'] = st.selectbox("Status Pernikahan",
                                                        options=list(marital_status_options.keys()),
                                                        format_func=lambda x: marital_status_options[x])
        input_features['Application_mode'] = st.number_input("Mode Aplikasi (Kode)", min_value=0, step=1, value=1) # Contoh: biarkan pengguna input kode jika tidak ada mapping
        input_features['Application_order'] = st.number_input("Urutan Aplikasi", min_value=0, step=1, value=1)
        input_features['Course'] = st.number_input("Program Studi (Kode)", min_value=0, step=1, value=171) # Contoh value dari dataset
        input_features['Daytime_evening_attendance'] = st.selectbox("Waktu Perkuliahan",
                                                                     options=list(attendance_options.keys()),
                                                                     format_func=lambda x: attendance_options[x],
                                                                     key="attendance")
        input_features['Previous_qualification'] = st.number_input("Kualifikasi Sebelumnya (Kode)", min_value=0, step=1, value=1)
        input_features['Previous_qualification_grade'] = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, step=0.1, value=120.0)
        input_features['Nacionality'] = st.number_input("Kewarganegaraan (Kode)", min_value=0, step=1, value=1) # Sebaiknya mapping jika ada
        input_features['Mothers_qualification'] = st.number_input("Kualifikasi Ibu (Kode)", min_value=0, step=1, value=19)
        input_features['Fathers_qualification'] = st.number_input("Kualifikasi Ayah (Kode)", min_value=0, step=1, value=12)

    with col2:
        input_features['Mothers_occupation'] = st.number_input("Pekerjaan Ibu (Kode)", min_value=0, step=1, value=5) # Sebaiknya mapping
        input_features['Fathers_occupation'] = st.number_input("Pekerjaan Ayah (Kode)", min_value=0, step=1, value=9) # Sebaiknya mapping
        input_features['Admission_grade'] = st.number_input("Nilai Penerimaan", min_value=0.0, max_value=200.0, step=0.1, value=125.0)
        input_features['Displaced'] = st.selectbox("Mahasiswa Pindahan (Displaced)",
                                                   options=list(yes_no_options.keys()),
                                                   format_func=lambda x: yes_no_options[x],
                                                   key="displaced")
        input_features['Educational_special_needs'] = st.selectbox("Kebutuhan Pendidikan Khusus",
                                                                    options=list(yes_no_options.keys()),
                                                                    format_func=lambda x: yes_no_options[x],
                                                                    key="special_needs")
        input_features['Debtor'] = st.selectbox("Memiliki Hutang Biaya Kuliah",
                                                 options=list(yes_no_options.keys()),
                                                 format_func=lambda x: yes_no_options[x],
                                                 key="debtor")
        input_features['Tuition_fees_up_to_date'] = st.selectbox("Biaya Kuliah Lunas",
                                                                  options=list(yes_no_options.keys()),
                                                                  format_func=lambda x: yes_no_options[x],
                                                                  key="tuition_paid")
        input_features['Gender'] = st.selectbox("Jenis Kelamin",
                                                options=list(gender_options.keys()),
                                                format_func=lambda x: gender_options[x],
                                                key="gender")
        input_features['Scholarship_holder'] = st.selectbox("Penerima Beasiswa",
                                                             options=list(yes_no_options.keys()),
                                                             format_func=lambda x: yes_no_options[x],
                                                             key="scholarship")
        input_features['Age_at_enrollment'] = st.number_input("Usia Saat Pendaftaran", min_value=17, max_value=70, step=1, value=20)

    with col3:
        input_features['International'] = st.selectbox("Mahasiswa Internasional",
                                                       options=list(yes_no_options.keys()),
                                                       format_func=lambda x: yes_no_options[x],
                                                       key="international")
        # Curricular units (contoh beberapa, lengkapi semua yang digunakan model)
        input_features['Curricular_units_1st_sem_credited'] = st.number_input("SKS Diakui Sem 1", min_value=0, step=1, value=0)
        input_features['Curricular_units_1st_sem_enrolled'] = st.number_input("SKS Diambil Sem 1", min_value=0, step=1, value=6)
        input_features['Curricular_units_1st_sem_evaluations'] = st.number_input("Jumlah Evaluasi Sem 1", min_value=0, step=1, value=6)
        input_features['Curricular_units_1st_sem_approved'] = st.number_input("SKS Lulus Sem 1", min_value=0, step=1, value=6)
        input_features['Curricular_units_1st_sem_grade'] = st.number_input("Rata-rata Nilai Sem 1", min_value=0.0, max_value=20.0, step=0.1, value=14.0) # Asumsi skala nilai 0-20
        input_features['Curricular_units_1st_sem_without_evaluations'] = st.number_input("SKS Tanpa Evaluasi Sem 1", min_value=0, step=1, value=0)

        input_features['Curricular_units_2nd_sem_credited'] = st.number_input("SKS Diakui Sem 2", min_value=0, step=1, value=0)
        input_features['Curricular_units_2nd_sem_enrolled'] = st.number_input("SKS Diambil Sem 2", min_value=0, step=1, value=6)
        input_features['Curricular_units_2nd_sem_evaluations'] = st.number_input("Jumlah Evaluasi Sem 2", min_value=0, step=1, value=6)
        input_features['Curricular_units_2nd_sem_approved'] = st.number_input("SKS Lulus Sem 2", min_value=0, step=1, value=6)
        input_features['Curricular_units_2nd_sem_grade'] = st.number_input("Rata-rata Nilai Sem 2", min_value=0.0, max_value=20.0, step=0.1, value=13.5)
        input_features['Curricular_units_2nd_sem_without_evaluations'] = st.number_input("SKS Tanpa Evaluasi Sem 2", min_value=0, step=1, value=0)

        input_features['Unemployment_rate'] = st.number_input("Tingkat Pengangguran (Wilayah)", min_value=0.0, step=0.1, value=10.0)
        input_features['Inflation_rate'] = st.number_input("Tingkat Inflasi (Wilayah)", step=0.1, value=1.0)
        input_features['GDP'] = st.number_input("GDP (Wilayah)", step=0.01, value=1.5)

    # Kumpulkan semua input dalam DataFrame
    # Pastikan urutan kolomnya (jika penting untuk model tertentu sebelum ColumnTransformer) atau cukup nama kolomnya
    # ColumnTransformer akan memilih kolom berdasarkan nama, jadi urutan di DataFrame ini tidak krusial,
    # TAPI nama kolom harus SAMA PERSIS dengan yang digunakan saat training.
    input_df = pd.DataFrame([input_features])
    return input_df

# --- TOMBOL PREDIKSI DAN TAMPILAN HASIL ---
if model_pipeline: # Hanya tampilkan jika model berhasil dimuat
    user_data_df = get_user_input()

    st.subheader("Data Mahasiswa yang Dimasukkan:")
    st.dataframe(user_data_df)

    # Tombol untuk Prediksi
    if st.sidebar.button("Prediksi Status Mahasiswa", type="primary"):
        try:
            # Buat prediksi
            prediction = model_pipeline.predict(user_data_df)
            prediction_proba = model_pipeline.predict_proba(user_data_df)

            predicted_status_code = prediction[0]
            predicted_status_label = status_mapping.get(predicted_status_code, "Label Tidak Diketahui")

            st.subheader("Hasil Prediksi:")
            if predicted_status_code == 1: # Dropout
                st.error(f"Status Prediksi: **{predicted_status_label}**")
            elif predicted_status_code == 0: # Graduate
                st.success(f"Status Prediksi: **{predicted_status_label}**")
            else: # Enrolled atau lainnya
                st.info(f"Status Prediksi: **{predicted_status_label}**")

            st.subheader("Probabilitas Prediksi:")
            # Menampilkan probabilitas untuk setiap kelas
            # Pastikan urutan probabilitas sesuai dengan urutan kelas model Anda (misal, model.classes_)
            # Biasanya urutannya adalah 0, 1, 2 jika labelnya demikian
            proba_df = pd.DataFrame({
                "Status": [status_mapping.get(i, f"Kelas {i}") for i in model_pipeline.classes_],
                "Probabilitas": prediction_proba[0]
            })
            st.dataframe(proba_df.set_index("Status"))

            # Memberikan saran berdasarkan prediksi (opsional)
            if predicted_status_code == 1: # Jika diprediksi Dropout
                st.warning("""
                **Rekomendasi:** Mahasiswa ini teridentifikasi memiliki risiko tinggi untuk dropout.
                Sebaiknya segera hubungi mahasiswa yang bersangkutan untuk:
                - Sesi konseling akademik dan non-akademik.
                - Identifikasi permasalahan yang dihadapi.
                - Pemberian dukungan atau bimbingan khusus.
                """)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
            st.error("Pastikan semua input telah diisi dengan benar dan model telah dilatih dengan fitur yang sesuai.")
else:
    st.error("Model tidak dapat dimuat. Aplikasi tidak dapat melakukan prediksi.")

st.markdown("---")
st.markdown("Developed for Jaya Jaya Institut")