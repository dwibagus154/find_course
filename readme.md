# Strategi Algoritma IF2211
> Tugas Kecil 2


## Table of contents
* [Brief Description](#brief-description)
* [Instalasi Python](#instalasi-python)
* [Clone Repository](#clone-repository)
* [How To Use](#how-to-use)
* [Author](#author)


## Brief Description
Pada tugas kali ini, , mahasiswa diminta membuat aplikasi sederhana yang dapat menyusun rencana pengambilan kuliah, dengan memanfaatkan algoritma Decrease and Conquer. Penyusunan Rencana Kuliah diimplementasikan dengan menggunakan pendekatan Topological Sorting. 
Pada persoalan Topological Sort, penyelesaian dilakukan dengan menggunakan varian decrease by a variable size dimana ukuran instant persoalan direduksi bervariasi pada setiap iterasi algoritma. Penulis memberikan nama program topological sort ini dengan nama Find Course App. Adapun algoritma topological sort yang diimplementasikan melalui tahap-tahap sebagai berikut
- baca masukan file input txt dan menaruhnya dalam array 2 dimensi
- mencari pelajaran yang tidak memiliki prasyarat
- mereduksi pelajaran tersebut di semua anggota array 2 dimensi 
- lakukan berulang kali hingga array 2 dimensi kosong 
- kasus khusus ketika tidak bisa diselesaikan dan array masih tersisa ketika telah 8 iterasi. 


## Instalasi Python
1. Download Python pada https://www.python.org/downloads/windows/
2. Lakukan instalasi pada Python
3. instalasi pyinstaller, pip install pyinstaller (opsional)


## Clone Repository
1. Buka terminal cmder atau gitbash 
2. Pilih directiory tempat anda ingin menyimpan code 
3. ketikkan git clone https://github.com/dwibagus154/find_course.git 
4. ketikkaan cd find_course
5. buka folder ini di text editor kesayangan anda (cara cepat code .)


## How to Use
1. Setelah buka folder find_course (pastikan folder yang anda buka memiliki 4 folder didalamnya yaitu bin, doc, src, dan test. Atau hanya 3 folder jika di clone dari github. Karena folder bin tidak memiliki file)
2. masuk ke folder src
3. lalu buka file 13519057.py
4. jalankan program 
5. untuk memvariasikannya, ganti angka 1 pada file_tucil = open("./test/test1.txt", "r") (line 17) dengan angka 1-8
6. Lihat outputnya pada CLI.

7. CARA LAIN (TIDAK DISARANKAN)
8. Buka direktori src di cmd 
9. ketik pyinstaller tucil.py
10. cari file exe di folder dist, lalu ketikkan 2 kali 

## Author
* 13519057-Kadek Dwi Bagus Ananta Udayana-Teknik Informatika-ITB
