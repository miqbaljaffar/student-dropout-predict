# 🎓 Proyek Akhir: Menyelesaikan Permasalahan Dropout di Jaya Jaya Institut (Edutech)

* Nama: Mohammad Iqbal Jaffar
* Email: iqbaljaffar1108@gmail.com
* Id Dicoding: miqbalj

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
1.  Pembuatan *virtual environment* Python untuk isolasi dependensi proyek.
2.  Instalasi pustaka `sqlalchemy` (meskipun tidak secara eksplisit digunakan dalam *script* analisis utama, ini dicatat sebagai bagian dari persiapan awal lingkungan yang mungkin diperlukan untuk interaksi database di skenario lain).
3.  import library seperti : 
* `pandas`, `numpy`, `matplotlib`, `seaborn`
* `scikit-learn`, `joblib`, `streamlit`

---

## 📊 Business Dashboard

![dashboard](https://raw.githubusercontent.com/miqbaljaffar/student-dropout-predict/main/miqbalj-dashboard.jpg)

Dashboard ini menyajikan visualisasi utama terkait dropout, seperti:

* **Distribusi Status Mahasiswa**
* **Tingkat Dropout dan Kelulusan Keseluruhan**
* **Dropout Berdasarkan Nilai Masuk**
* **Rata-Rata SKS Diambil vs. SKS Lulus (Semester 1)**
* **Dropout berdasarkan Status Pembayaran Uang Kuliah**


### Ringkasan Temuan dari Business Dashboard

Secara keseluruhan, dashboard ini menyajikan gambaran komprehensif mengenai situasi mahasiswa di **Jaya Jaya Institut**, dengan fokus utama pada **identifikasi faktor-faktor yang berkontribusi terhadap angka dropout**.

Beberapa temuan utama:

* **Jumlah Mahasiswa Aktif:** 4.424 mahasiswa
* **Tingkat Dropout:** 32,12%
* **Tingkat Kelulusan:** 49,93%
* **Status Masih Terdaftar:** 17,9%

#### Temuan Utama:

1. **Nilai Masuk dan Dropout**

   * Mahasiswa dengan **nilai masuk di bawah 100** menunjukkan tingkat dropout tertinggi.
   * Hampir **50% dari 794 mahasiswa** dalam kelompok ini tidak menyelesaikan pendidikan mereka.

2. **Kinerja Akademik Awal**

   * Mahasiswa yang dropout rata-rata:

     * Mengambil lebih sedikit SKS.
     * Lulus lebih sedikit mata kuliah di semester pertama.
   * Ini menunjukkan bahwa performa akademik awal sangat berkorelasi dengan status akhir mahasiswa.

3. **Faktor Finansial**

   * Mahasiswa yang **tidak membayar uang kuliah tepat waktu** memiliki tingkat dropout hingga **80%**.
   * Sebaliknya, mereka yang membayar tepat waktu memiliki kecenderungan dropout yang jauh lebih rendah.

---

### Implikasi

Informasi ini sangat **krusial** bagi manajemen Jaya Jaya Institut untuk:

* Melakukan **intervensi dini**,
* Memberikan **bimbingan dan dukungan khusus**, serta
* Merancang **strategi pencegahan dropout** berbasis data dan risiko yang telah teridentifikasi.

---

## Kredensial Metabase

Dashboard Metabase dijalankan secara lokal. Untuk mengaksesnya, pastikan instance Metabase sudah berjalan di komputer Anda.

* **URL Metabase (Lokal):** http://localhost:3000/public/dashboard/61371a65-1b33-4783-a161-5bfd0e1e7a14
* **Username:** iqbaljaffar1108@gmail.com
* **Password:** metabase1108
 
**Catatan Penting untuk Penilai:**
Karena Metabase dijalankan secara lokal, URL di atas hanya akan berfungsi jika Anda menjalankan instance Metabase ini di mesin Anda sendiri dengan data yang sama. Jika diperlukan cara lain untuk mendemonstrasikan dashboard (misalnya melalui screenshot, video, atau jika saya perlu men-deploy-nya ke environment yang bisa diakses publik), mohon informasikan.

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

