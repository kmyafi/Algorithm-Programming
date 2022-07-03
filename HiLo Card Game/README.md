## Question 5 ##
Kartu remi merupakan kumpulan 52 kartu yang digunakan untuk permainan. Salah satu contoh permainan yang menggunakan kartu remi adalah upper-lower. Peraturan permainan tersebut sebagai berikut:
- Nilai kartu dari terendah hingga tertinggi sebagai berikut:

  <p align="center"><i>
    Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king.
  </i></p>
  
  Perhatikan bahwa terdapat 52 kartu, tetapi hanya 13 nilai. Hal ini berarti dalam satu *deck* kartu remi, terdapat empat kartu untuk setiap nilai.
- Pada awal permainan, pemain akan diberikan 1 kartu tertutup (nilai tidak diketahui) dan 1 kartu terbuka (nilai diketahui) dari *deck*. 
- Pemain harus menebak nilai kartu yang tertutup.
  - "*Upper*" berarti kartu tertutup memiliki nilai lebih besar daripada kartu terbuka.
  - "*Lower*" berarti kartu tertutup memiliki nilai lebih kecil daripada kartu terbuka.
- Apabila pemain menebak dengan benar, mereka mendapatkan 1 poin dan *game* dilanjutkan. Kartu tertutup menjadi kartu terbuka yang baru. Kartu tertutup yang baru diambil dari *deck*.
- Apabila pemain salah menebak, maka *game* dihentikan.
- Apabila kartu tertutup dan kartu terbuka memiliki nilai yang sama, tidak terjadi penambahan poin dan *game* dilanjutkan. Kartu tertutup menjadi kartu terbuka yang baru. Kartu tertutup yang baru diambil dari *deck*.
- Kartu yang telah dimainkan tidak digunakan lagi (tidak kembali ke *deck*).

Buatlah program permainan *upper-lower* di Python dengan ketentuan tambahan berikut:
- Buat fungsi *start()* yang menerima 0 input.
- Munculkan poin yang pemain dapatkan di akhir permainan.
- Apabila pemain salah menebak, berikan pemain pilihan untuk *restart*.
- Apabila dalam permainan pemain menginput selain "*upper*" atau "*lower*", perintahkan pemain untuk menginput ulang.
- Apabila kartu pada *deck* sudah habis, tampilkan pesan selamat dan berikan pemain pilihan untuk *restart*.
- Gunakanlah *input()* dan *module random* untuk membantu program kalian.

Contoh output running program seperti yang dilihat dibawah ini.
```
-------~~-------~~-------
Kartu yang terbuka adalah kartu 2.
Kartu tertutup sudah diambil
upper or lower?: upper
Nilai kartu sama, kita lanjutkan
-------~~-------~~-------
Kartu yang terbuka adalah kartu 2.
Kartu tertutup sudah diambil
upper or lower?: upper
Kartu tertutup adalah kartu jack. Jawaban anda benar.
-------~~-------~~-------
Kartu yang terbuka adalah kartu jack.
Kartu tertutup sudah diambil
upper or lower?: lower
Kartu tertutup adalah kartu ace. Jawaban anda benar.
-------~~-------~~-------
Kartu yang terbuka adalah kartu ace.
Score akhir: 2
Selamat! Deck kartu sudah habis, restart?(y/n):y
-------~~-------~~-------
Kartu yang terbuka adalah kartu jack.
Kartu tertutup sudah diambil
upper or lower ?: ayam
Anda salah input, silahkan ulang.
upper or lower ?: bebek
Anda salah input, silahkan ulang.
upper or lower ?: upper
Kartu tertutup adalah kartu 2. Jawaban anda salah.
Score akhir: 0
Restart?(y/n):n
```
