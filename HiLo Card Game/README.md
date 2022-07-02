## Question 5 ##
Kartu remi merupakan kumpulan 52 kartu yang digunakan untuk permainan. Salah satu contoh permainan yang menggunakan kartu remi adalah upper-lower. Peraturan permainan tersebut sebagai berikut:
- Nilai kartu dari terendah hingga tertinggi sebagai berikut:
  > *Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king.*
  
  Perhatikan bahwa terdapat 52 kartu, tetapi hanya 13 nilai. Hal ini berarti dalam satu *deck* kartu remi, terdapat empat kartu untuk setiap nilai.
- Pada awal permainan, pemain akan diberikan 1 kartu tertutup (nilai tidak diketahui) dan 1 kartu terbuka (nilai diketahui) dari *deck*. 
- Pemain harus menebak nilai kartu yang tertutup.
  - "*Upper*" berarti kartu tertutup memiliki nilai lebih besar daripada kartu terbuka.
  - "*Lower*" berarti kartu tertutup memiliki nilai lebih kecil daripada kartu terbuka.
- Apabila pemain menebak dengan benar, mereka mendapatkan 1 poin dan *game* dilanjutkan. Kartu tertutup menjadi kartu terbuka yang baru. Kartu tertutup yang baru diambil dari *deck*.
- Apabila pemain salah menebak, maka game dihentikan.
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
![Example Output](https://github.com/kmyafi/Algorithm-Programming/blob/main/HiLo%20Card%20Game/ExampleOutput_No5.jpg)
