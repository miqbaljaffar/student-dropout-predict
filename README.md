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

## Persiapan
### 📁 Dataset & Fitur

Dataset yang digunakan adalah `data.csv`. File ini berisi berbagai atribut mengenai siswa/students, seperti :

| **Nama Kolom**                                        | **Definisi**                                                                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Marital\_status**                                   | Status pernikahan mahasiswa (misalnya: 1 = Lajang, 2 = Menikah, dll).                                                          |
| **Application\_mode**                                 | Cara atau jalur mahasiswa mendaftar (misalnya: online, jalur prestasi, reguler, dll — direpresentasikan sebagai kode numerik). |
| **Application\_order**                                | Urutan pilihan program studi saat pendaftaran (misalnya: pilihan ke-1, ke-2, dst.).                                            |
| **Course**                                            | ID program studi atau jurusan yang diambil mahasiswa.                                                                          |
| **Daytime\_evening\_attendance**                      | Jenis kehadiran kuliah (1 = kelas pagi, 0 = kelas malam).                                                                      |
| **Previous\_qualification**                           | Kualifikasi pendidikan terakhir sebelum masuk (misalnya: SMA, diploma, dll — dalam bentuk kode).                               |
| **Previous\_qualification\_grade**                    | Nilai akhir dari kualifikasi sebelumnya (misalnya nilai ijazah SMA).                                                           |
| **Nacionality**                                       | Kewarganegaraan mahasiswa (kode numerik).                                                                                      |
| **Mothers\_qualification**                            | Kualifikasi pendidikan ibu mahasiswa (kode numerik).                                                                           |
| **Fathers\_qualification**                            | Kualifikasi pendidikan ayah mahasiswa (kode numerik).                                                                          |
| **Mothers\_occupation**                               | Pekerjaan ibu mahasiswa (kode numerik).                                                                                        |
| **Fathers\_occupation**                               | Pekerjaan ayah mahasiswa (kode numerik).                                                                                       |
| **Admission\_grade**                                  | Nilai akhir saat penerimaan mahasiswa.                                                                                         |
| **Displaced**                                         | Apakah mahasiswa berasal dari wilayah konflik/pengungsi (1 = ya, 0 = tidak).                                                   |
| **Educational\_special\_needs**                       | Apakah mahasiswa memiliki kebutuhan khusus dalam pendidikan (1 = ya, 0 = tidak).                                               |
| **Debtor**                                            | Apakah mahasiswa memiliki tunggakan pembayaran (1 = ya, 0 = tidak).                                                            |
| **Tuition\_fees\_up\_to\_date**                       | Apakah pembayaran SPP/biaya kuliah mahasiswa sudah diperbarui (1 = ya, 0 = tidak).                                             |
| **Gender**                                            | Jenis kelamin mahasiswa (1 = perempuan, 0 = laki-laki, atau sebaliknya tergantung dokumentasi).                                |
| **Scholarship\_holder**                               | Apakah mahasiswa menerima beasiswa (1 = ya, 0 = tidak).                                                                        |
| **Age\_at\_enrollment**                               | Usia mahasiswa saat pertama kali mendaftar.                                                                                    |
| **International**                                     | Apakah mahasiswa berasal dari luar negeri (1 = ya, 0 = tidak).                                                                 |
| **Curricular\_units\_1st\_sem\_credited**             | Jumlah mata kuliah semester 1 yang diakui kreditnya (misalnya karena transfer dari institusi lain).                            |
| **Curricular\_units\_1st\_sem\_enrolled**             | Jumlah mata kuliah semester 1 yang diambil.                                                                                    |
| **Curricular\_units\_1st\_sem\_evaluations**          | Jumlah mata kuliah semester 1 yang diikuti ujian/penilaiannya.                                                                 |
| **Curricular\_units\_1st\_sem\_approved**             | Jumlah mata kuliah semester 1 yang lulus.                                                                                      |
| **Curricular\_units\_1st\_sem\_grade**                | Rata-rata nilai dari semua mata kuliah semester 1.                                                                             |
| **Curricular\_units\_1st\_sem\_without\_evaluations** | Jumlah mata kuliah semester 1 yang tidak dinilai (mungkin tidak ikut ujian).                                                   |
| **Curricular\_units\_2nd\_sem\_credited**             | Jumlah mata kuliah semester 2 yang diakui kreditnya.                                                                           |
| **Curricular\_units\_2nd\_sem\_enrolled**             | Jumlah mata kuliah semester 2 yang diambil.                                                                                    |
| **Curricular\_units\_2nd\_sem\_evaluations**          | Jumlah mata kuliah semester 2 yang diikuti ujian/penilaiannya.                                                                 |
| **Curricular\_units\_2nd\_sem\_approved**             | Jumlah mata kuliah semester 2 yang lulus.                                                                                      |
| **Curricular\_units\_2nd\_sem\_grade**                | Rata-rata nilai dari semua mata kuliah semester 2.                                                                             |
| **Curricular\_units\_2nd\_sem\_without\_evaluations** | Jumlah mata kuliah semester 2 yang tidak dinilai.                                                                              |
| **Unemployment\_rate**                                | Tingkat pengangguran pada saat itu (dalam persentase, bisa jadi dari data eksternal).                                          |
| **Inflation\_rate**                                   | Tingkat inflasi saat itu (persentase, bisa jadi dari data eksternal).                                                          |
| **GDP**                                               | Produk Domestik Bruto (dalam satuan tertentu, biasanya log GDP atau GDP per kapita).                                           |
| **Status**                                            | Status akhir mahasiswa: **Graduate** (lulus), **Enrolled** (masih aktif), atau **Dropout** (putus studi).                      |

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

* **URL Metabase (Lokal):** http://localhost:3000/public/dashboard/81e22187-2c74-41da-b4e7-40e54e09b542
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

