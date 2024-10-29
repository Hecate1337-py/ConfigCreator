# Access Token Tools

Tools ini digunakan untuk mendapatkan **short-lived** dan **long-lived access token** dari **Facebook Graph API**. Dua file utama yang disediakan adalah `short.py` untuk mendapatkan short-lived access token dan `long.py` untuk menukarkan short-lived access token menjadi long-lived access token.

## Persyaratan

Sebelum menggunakan alat ini, pastikan Anda telah melakukan hal berikut:

- Memiliki **Facebook App ID** dan **App Secret** dari [Facebook Developer Console](https://developers.facebook.com/).
- Menginstal library `requests` dan `configparser` di lingkungan Python Anda.

Anda dapat menginstal dependensi dengan perintah berikut:

```
pip install requests configparser
```

# Cara Penggunaan
1. short.py - Mendapatkan Short-Lived Access Token
Gunakan file short.py untuk mendapatkan short-lived access token dari Facebook Graph API Explorer.

## Langkah-langkah:

- Masuk ke Facebook Graph API Explorer.

- Dapatkan User Access Token.

- Salin token yang dihasilkan dan gunakan pada short.py jika diperlukan.

2. long.py - Mendapatkan Long-Lived Access Token
File ini digunakan untuk menukar short-lived access token menjadi long-lived access token.

## Langkah-langkah:

- Jalankan script long.py.

- Masukkan Short-Lived Access Token, App ID, dan App Secret yang diminta.

- Setelah proses selesai, Long-Lived Access Token akan dihasilkan dan secara otomatis ditulis ke dalam file config.ini.

# Contoh Isi config.ini

Setelah proses berhasil, file config.ini akan terlihat seperti berikut :
```
[PAGE_01]
page_name = YourPageName1
page_id = YourPageID1
access_token = YourPageAccessToken1

[PAGE_02]
page_name = YourPageName2
page_id = YourPageID2
access_token = YourPageAccessToken2

[PAGE_03]
page_name = YourPageName3
page_id = YourPageID3
access_token = YourPageAccessToken3

[PAGE_04]
page_name = YourPageName4
page_id = YourPageID4
access_token = YourPageAccessToken4

[DETAILS]
video_path = vid
hashtags = #viral #epic #reels #fyp #respect

[REPLY_TEMPLATES]
default_reply = Thanks for watching, dont forget to like, comment, follow, and share <3.
```

# Catatan

- Short-lived access token hanya berlaku selama beberapa jam.
- Long-lived access token berlaku selama 60 hari.

# Error Handling

Jika terjadi kesalahan saat mengambil atau menukarkan token, pesan error akan dicetak ke konsol. Pastikan bahwa:

- Short-Lived Access Token valid.
- App ID dan App Secret yang Anda gunakan benar.
