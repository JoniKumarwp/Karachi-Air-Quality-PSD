---
title: "Streamlit App Deployment Guide"
---

# Panduan Deployment Aplikasi Streamlit

**Joni Kumar Meghwar · 240411100234**

Dokumen ini menjelaskan arsitektur, deployment, dan pembaruan dashboard klasifikasi tutupan lahan Jawa Timur. Aplikasi Streamlit dan dokumentasi proyek berada di layanan berbeda: Streamlit menyajikan dashboard, sedangkan GitHub Pages menyajikan dokumentasi.

## Tautan aplikasi dan repositori

- **Dashboard Streamlit:** [psd-uts-joni.streamlit.app](https://psd-uts-joni.streamlit.app/)
- **Repositori GitHub:** [JoniKumarwp/Karachi-Air-Quality-PSD](https://github.com/JoniKumarwp/Karachi-Air-Quality-PSD)
- **Dokumentasi GitHub Pages:** [Karachi Air Quality PSD](https://jonikumarwp.github.io/Karachi-Air-Quality-PSD/)
- **Kode aplikasi:** [`uts/deploy/app.py`](https://github.com/JoniKumarwp/Karachi-Air-Quality-PSD/blob/main/uts/deploy/app.py)
- **Dependensi aplikasi:** [`uts/deploy/requirements.txt`](https://github.com/JoniKumarwp/Karachi-Air-Quality-PSD/blob/main/uts/deploy/requirements.txt)

## Arsitektur dan berkas dashboard

Notebook dan pipeline Python mengolah data sampel, melatih model, serta menyimpan keluaran analisis. Aplikasi Streamlit membaca berkas hasil tersebut dari `uts/deploy/`, lalu menampilkan metrik evaluasi, tabel, dan peta interaktif. Dengan demikian, dashboard menggunakan keluaran proyek yang disimpan di repositori; ia tidak menjalankan ulang ekstraksi citra satelit setiap kali halaman dibuka.

Berkas hasil utama yang dibaca dashboard meliputi:

- `metrik_evaluasi_knn.csv` dan `confusion_matrix.csv` untuk evaluasi model.
- `ringkasan_model_knn.csv`, `kepentingan_fitur.csv`, dan `kurva_validasi_k.csv` untuk ringkasan serta analisis model.
- `prediksi_data_uji.csv` untuk membandingkan label aktual dan prediksi.
- `map_lulc.html`, `map_lulc_predicted.html`, dan berkas GeoJSON untuk peta sampel dan evaluasi.

Daftar pustaka deployment dikelola di `uts/deploy/requirements.txt`. Pertahankan berkas hasil yang dibutuhkan dashboard saat memperbarui proyek. Jangan memasukkan kredensial Copernicus, token, atau rahasia ke repositori.

## Deploy atau hubungkan aplikasi Streamlit

Aplikasi ini sudah tersedia di [psd-uts-joni.streamlit.app](https://psd-uts-joni.streamlit.app/). Untuk membuat ulang atau menghubungkan deployment di Streamlit Community Cloud:

1. Masuk ke [Streamlit Community Cloud](https://share.streamlit.io/) menggunakan akun GitHub yang memiliki akses ke repositori.
2. Pilih **Create app** lalu pilih **Deploy a public app from GitHub**.
3. Gunakan konfigurasi berikut:

   | Pengaturan | Nilai |
   | --- | --- |
   | Repository | `JoniKumarwp/Karachi-Air-Quality-PSD` |
   | Branch | `main` |
   | Main file path | `uts/deploy/app.py` |
   | App URL | `psd-uts-joni` |

4. Pilih **Deploy**. Streamlit Community Cloud memasang dependensi aplikasi dari `uts/deploy/requirements.txt` dan menjalankan berkas utama.
5. Setelah proses deployment selesai, periksa dashboard dan pastikan tabel, metrik, serta peta tampil. Jika deployment mengalami kegagalan, buka log aplikasi di Streamlit Community Cloud untuk melihat pesan error.

## Menjalankan dashboard secara lokal

Dari direktori utama repository, siapkan environment Python, instal dependensi dashboard, lalu jalankan aplikasi:

```bash
python -m venv .venv
```

Aktifkan environment `.venv`, kemudian:

```bash
python -m pip install -r uts/deploy/requirements.txt
python -m streamlit run uts/deploy/app.py
```

Dashboard memerlukan berkas hasil yang disimpan di `uts/deploy/`. Untuk menjalankan pipeline data atau menghasilkan ulang model, ikuti notebook dan instruksi di direktori `uts/code/`; pengambilan citra Copernicus memerlukan akun dan autentikasi tersendiri.

## Memperbarui dashboard dan dokumentasi

Streamlit Community Cloud terhubung ke repository GitHub. Setelah perubahan aplikasi atau berkas data yang digunakan dashboard diperiksa, commit dan push perubahan ke `main`:

```bash
git add uts/
git commit -m "Update UTS dashboard"
git push origin main
```

Streamlit Community Cloud mendeteksi perubahan branch yang terhubung dan menjalankan ulang aplikasi. Periksa log deployment dan buka URL aplikasi untuk memastikan pembaruan berhasil.

Dokumentasi ini dibangun melalui workflow GitHub Pages [`.github/workflows/deploy.yml`](https://github.com/JoniKumarwp/Karachi-Air-Quality-PSD/blob/main/.github/workflows/deploy.yml). Workflow berjalan otomatis ketika ada push ke `main` atau dapat dijalankan manual melalui tab **Actions**. Workflow membangun situs MyST (`myst build --html`) dan menerbitkan hasilnya ke GitHub Pages; tidak perlu membuat branch `gh-pages` secara manual.

Halaman panduan ini tersedia di:

`https://jonikumarwp.github.io/Karachi-Air-Quality-PSD/deployment-guide/`

## Referensi

- [Dokumentasi deployment Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
- [Repositori proyek](https://github.com/JoniKumarwp/Karachi-Air-Quality-PSD)
- [Aplikasi Streamlit](https://psd-uts-joni.streamlit.app/)
