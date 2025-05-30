# 🎓 Proyek Akhir: Menyelesaikan Permasalahan Dropout di Jaya Jaya Institut (Edutech)

## 🧠 Business Understanding

**Jaya Jaya Institut** merupakan institusi pendidikan tinggi yang berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berprestasi. Namun, institusi ini menghadapi tantangan serius berupa **tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout)**.

### 🎯 Tujuan Proyek

1. Mengidentifikasi **faktor-faktor utama** yang mempengaruhi keputusan mahasiswa untuk dropout.
2. Mendeteksi **mahasiswa berisiko tinggi** untuk dropout secara dini.
3. Mengembangkan **strategi intervensi** untuk menekan angka dropout.

---

## 📌 Cakupan Proyek

1. **Analisis Data Eksploratif (EDA)**
   Menganalisis data mahasiswa dan mencari pola yang berkaitan dengan status kelulusan.

2. **Pengembangan Business Dashboard**
   Membuat visualisasi interaktif untuk memantau performa mahasiswa dan potensi dropout.

3. **Pengembangan Model Machine Learning**
   Membangun model prediktif untuk mengklasifikasikan mahasiswa berdasarkan risiko dropout.

---

## 📁 Dataset & Fitur

Dataset berisi data demografis, akademik, sosio-ekonomi, dan makroekonomi mahasiswa. Berikut ringkasan kategorinya:

### 🧍‍♂️ Informasi Demografis & Sosial-Ekonomi

* `Marital_status`, `Nacionality`, `Gender`, `Age_at_enrollment`
* `International`, `Displaced`, `Educational_special_needs`
* `Mothers_qualification`, `Fathers_qualification`
* `Mothers_occupation`, `Fathers_occupation`

### 🎓 Informasi Akademik Awal

* `Application_mode`, `Application_order`, `Course`
* `Daytime_evening_attendance`, `Previous_qualification`
* `Previous_qualification_grade`, `Admission_grade`

### 💰 Informasi Finansial

* `Debtor`, `Tuition_fees_up_to_date`, `Scholarship_holder`

### 📚 Performa Akademik (Semester 1 & 2)

* `Curricular_units_*_credited`, `enrolled`, `evaluations`, `approved`, `grade`, `without_evaluations`

### 🌍 Kondisi Ekonomi Makro

* `Unemployment_rate`, `Inflation_rate`, `GDP`

### 🎯 Target / Label

* `Status`:

  * `Dropout` = keluar
  * `Graduate` = lulus
  * `Enrolled` = masih aktif

---

## ⚙️ Setup Environment

Proyek ini dibangun menggunakan **Python**, dengan library utama seperti:

* `pandas`, `numpy`, `matplotlib`, `seaborn`
* `scikit-learn`, `joblib`, `streamlit`

---

## 📊 Business Dashboard

Dashboard ini menyajikan visualisasi utama terkait dropout, seperti:

* **Distribusi Status Mahasiswa**
* **Tingkat Dropout dan Kelulusan Keseluruhan**
* **Dropout Berdasarkan Nilai Masuk**
* **Rata-Rata SKS Diambil vs. SKS Lulus (Semester 1)**
* **Dropout berdasarkan Status Pembayaran Uang Kuliah**

> 📌 Catatan: Saat ini, dashboard divisualisasikan dalam bentuk analisis dan output statis (PDF). Untuk implementasi nyata, dapat digunakan tools seperti **Tableau**, **Power BI**, atau **Streamlit**.

---

## 🤖 Sistem Machine Learning

### 🔄 Alur Model

1. **Load Data** dari file CSV
2. **EDA & Data Understanding**
3. **Preprocessing**: imputasi, scaling, encoding
4. **Split Data**: training vs testing
5. **Modeling**: Logistic Regression, Random Forest, Gradient Boosting
6. **Evaluation**: fokus pada *Recall* untuk kelas `Dropout`
7. **Saving Best Model**: menggunakan `joblib`

### 🏆 Model Terbaik

* **Random Forest** terpilih karena memiliki **Recall tertinggi** pada kelas `Dropout`.

> 📌 Catatan: Model ini dapat di-deploy sebagai API atau aplikasi web.

---

## 🌐 Demo Model

🔗 **Akses Model Dropout Prediction di Streamlit:**
👉 [Klik untuk buka aplikasi](https://student-dropout-predict-xe4nkisdrrzqsuxwr3meaa.streamlit.app/)

---

## ✅ Kesimpulan

Proyek ini berhasil:

* Mengidentifikasi faktor utama penyebab dropout
* Mengembangkan prototipe prediksi mahasiswa berisiko
* Membangun dashboard interaktif untuk manajemen kampus

**Random Forest** menjadi model unggulan dengan:

* 🎯 Recall (Dropout): `0.8204`
* 📊 Akurasi Uji: `0.7864`

---

## ✅ Rekomendasi Action Items

1. **Program Pendampingan Intensif**
   Fokus pada mahasiswa baru dengan nilai masuk rendah & performa awal buruk.

2. **Skema Bantuan Keuangan & Kebijakan Fleksibel**
   Tawarkan opsi UKT yang lebih adaptif bagi mahasiswa berpotensi.

3. **Sistem Monitoring Akademik Proaktif**
   Kembangkan sistem peringatan dini berbasis dashboard dan model prediksi.

4. **Studi Kualitatif (Survei & Wawancara)**
   Gali alasan dropout dari sisi mahasiswa langsung untuk strategi yang lebih tepat sasaran.

