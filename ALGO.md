`LOCAL_RSA_KEY_PAIR` = dihasilkan saat inisialisasi waktu jalannya program

`GLOBAL_RSA_PUBLIC_KEY` = kunci publik server, yang disematkan secara hard-coded ke dalam program

---
### Enkripsi file
1. Buat kunci AES.
2. Enkripsi konten file.
3. Enkripsi kunci AES menggunakan kunci publik dari `LOCAL_RSA_KEY_PAIR`.
4. Tambahkan kunci AES yang telah dienkripsi ke bagian awal file yang telah dienkripsi.

---
### Algo
1. Cari file.
2. Enkripsi setiap file.
3. Enkripsi kunci pribadi dari `LOCAL_RSA_KEY_PAIR` menggunakan `GLOBAL_RSA_PUBLIC_KEY`.
4. Tulis kunci pribadi yang telah dienkripsi dari `LOCAL_RSA_KEY_PAIR` ke sebuah file.
5. Buat README.txt.
---
### Dekripsi file
1. Ambil kunci AES yang telah dienkripsi dari bagian awal file.
2. Dekripsi kunci AES menggunakan kunci pribadi RSA yang telah didekripsi dari pasangan kunci RSA yang dihasilkan secara lokal.
3. Gunakan kunci AES yang telah didekripsi untuk mendekripsi konten file.
4. Simpan konten file yang telah didekripsi ke dalam file baru.
5. Hapus file yang telah dienkripsi.
