<p align="center">
<h1>THOR</h1>
</p>

Thor adalah ransomware.
Thor menggunakan **RSA-2048** dengan **AES-128** untuk mengenkripsi file.
<br/>
<br/>**HANYA** untuk tujuan edukasi.

---
### Cara Tetap Aman Saat Bermain dengan Kode Ini
1. **JANGAN** uncomment baris-baris dalam `payload/agent/lib/file_finder.py`.

2. Secara default, kode ini hanya akan mengenkripsi file dalam folder di desktop Anda yang bernama `Target_Folder`.

3. **Peringatan:** Jangan jalankan kode ini di komputer pribadi Anda, gunakan mesin virtual (VM) sebagai gantinya. Dan jika Anda menjalankannya, biarkan berjalan hingga selesai.

---
### Untuk Perlindungan Diri
1. Untuk perlindungan Anda sendiri, ransomware ini hanya akan mengenkripsi file dalam folder bernama `Target_Folder` di desktop Anda.

2. Anda dapat membuatnya mengenkripsi semua file dengan membuka komentar beberapa baris dalam `payload/agent/lib/file_finder.py`

---
### Persyaratan
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---
### Penggunaan pada Mesin Virtual (VM)
1. Buka komentar pada bagian yang dikomentari di `payload/agent/lib/file_finder.py`.

2. Buat pasangan kunci publik server dengan menjalankan `python thor.py`.

3. Ubah direktori ke direktori payload.

4. Jalankan `encryptor_generator.py`.

5. Infeksi VM Anda dengan file exe yang dihasilkan.

6. Dapatkan kunci pribadi RSA yang terenkripsi yang dihasilkan oleh file exe dari VM Anda.

7. Ubah direktori kembali ke direktori payload.

8. Jalankan `decryptor_generator.py` dan berikan kunci RSA tersebut.

9. Kirim file decryptor.exe ke VM.

10. Biarkan decryptor berjalan dan mendekripsi file dalam VM Anda.

---
### Tidak untuk Dibagikan
Setiap kali Anda membuat ransomware, Anda harus membuat decryptor untuk ransomware tersebut. Anda tidak bisa membuat satu decryptor dan menggunakannya dengan ransomware yang dibuat berbeda.

### Contoh Penggunaan

1.  Install persyaratan
    ```
    pip install -r requirements.txt
    ```
2.  Buat pasangan kunci publik server
    ```
    python thor.py
    ```
3.  Ubah direktori ke folder payload dan buat ransomware
    ```
    python encryptor_generator.py -b mybtcadress -a 120 -k ../server/keys/public.pem -n virus_danger
    ```
4.  Ubah direktori ke folder payload dan buat decryptor
    ```
    python decryptor_generator.py -sk ../server/keys/private.key -vk encrypted_private.ekey -n decryptor
    ```

---
### Peringatan
> Saya tidak akan bertanggung jawab atas tindakan Anda.

> **JANGAN** pakai kode ini jika Anda tidak memiliki pengendalian diri.

---
### Connect with me

  You can reach me through My Gmail, LinkedIn, or Instagram account
  
 <a
 href="mailto:yogaardikaaa123@gmail.com?subject=Hi%20Yoga,%20I'd%20like%20to%20hire%20you">
  <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="27" alt="gmail logo" />
</a>
<a href="https://www.linkedin.com/in/agooy/">
  <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="27" alt="linkedin logo" />
</a>
<a href="https://instagram.com/yogardkaa">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="27" alt="instagram logo" />
</a>

---
<div align="center">

![MadeWithLove](https://forthebadge.com/images/badges/made-with-love__.svg)
![forthebadge](https://forthebadge.com/images/badges/made-in-python.svg)
</div>