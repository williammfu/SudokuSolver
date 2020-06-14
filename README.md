# Sudoku Solver

## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.


## Spesifikasi

#### Spesifikasi untuk program yang dibuat :
| No | Spesifikasi Program | Jenis |
| ---- | ---- | ---- |
| 1 | Program dibuat dalam bahasa Python | Wajib |
| 2 | Program menerima input berupa file eksternal yang berisi matriks area permainan (disediakan pada repository) dengan lambang '#' yang menandai area belum diketahui nomornya | Wajib |
| 3 | Program melengkapi area-area yang nomornya belum diketahui, strategi dan heuristik yang digunakan dibebaskan dan menjadi salah satu komponen penilaian. **Pencarian solusi harus dibuat sendiri algoritmanya**. | Wajib |
| 4 | Tuliskan hasil dari sepesifikasi (3) pada command prompt/terminal dan simpan dalam file eksternal. Buatlah agar mudah dibaca | Wajib |
| 5 | Tuliskan semua koordinat dari area bernomor 5, tuliskan pada command prompt/terminal dan simpan pada file eksternal yang sama dengan spesifikasi nomor (4). Koordinat dituliskan setelah area permainan | Wajib |
| 6 | Program dapat membaca inputan dari gambar. **Program hanya perlu dapat membaca gambar spesifik yang ada pada repository**. Library yang digunakan dibebaskan dan tidak ada batasan. | Bonus |
| 7 | Program diletakkan pada directory src, kemudian file pengujian diletakkan pada directory test, dan hasil pengujian berupa screenshot diletakkan pada directory result | Wajib |
| 8 | Program dikejakan secara individu, Anda boleh mencari referensi dari manapun namun tidak diperkenankan bekerja sama | Wajib |

## Prerequisite
Untuk menjalankan program ini, pastikan perangkat anda memiliki 
1. Python (versi 3.6.0 ke atas)
2. OpenCV for Python
3. Pytesseract (untuk OCR)

Apabila perangkat anda memiliki package manager pip, anda dapat menjalankan perintah berikut untuk menginstal prerequisite yang dibutuhkan
```
pip install requirements.txt
```

## Penggunaan Program
Jalankan perintah berikut pada repository ini
```
cd src
python main.py <input file> <output file> <username>
```
**Keterangan**: 
- Nama file input dapat dalam format **txt** atau **jpg**/**png**, sedangkan output hanya dalam **txt** saja
- *(Untuk pengguna Windows)* username merupakan nama perangkat Windows

## Algoritma

### Backtracking
Algoritma ini merupakan perbaikan dari pencarian solusi secara DFS. Pada pohon pencarian solusi, simpul yang tidak mengarah pada solusi dipangkas dan tidak diekspan lagi.

Dalam penyelesaian sudoku, suatu sel sudoku kosong akan diisi dengan nilai yang tidak melanggar constraint kolom/baris/submatriks, kemudian sel kosong selanjutnya akan diisi hingga seluruh sel kosong pada sudoku terisi atau tidak ada nilai yang bisa diisi pada sel kosong (karena sel yang diisi sebelumnya tidak valid, **backtrack**). Algoritma backtracking dapat diimplementasikan dalam bentuk fungsi rekursif yang akan berhenti saat seluruh sel kosong sudoku sudah terisi (basis).  

**Kompleksitas** : O(n<sup>m</sup>)

n = banyaknya kemungkinan jawaban pada tiap sel <br>
m = banyaknya sel kosong pada sudoku

(Aljohani, et al. 2016)

#### Alasan
Algoritma backtracking dimanfaatkan dalam mengisi puzzle sudoku sebab permasalahan ini memiliki kesamaan dengan *Graph Coloring Problem* yang dapat dipecahkan dengan menggunakan algoritma *backtracking*. Sehingga, algoritma ini juga cocok digunakan untuk memecahkan sudoku.

### Heuristik

Heuristik yang dimanfaatkan dalam backtracking ini adalah **heuristik MRV** (Minimum Remaining Value). Heuristik ini diterapkan dengan mengganggap penyelesaian puzzle sudoku sebagai CSP (*Constraint Satisfaction Problem*). 

Dalam penyelesaian puzzle sudoku, sel sudoku kosong dengan banyak kemungkinan nilai yang paling kecil akan diisi terlebih dahulu. Dengan demikian, diharapkan simpul yang menunjuk pada solusi yang tidak valid dapat dipangkas lebih cepat.

## Struktur Repository

- src

Berisi source code program backtracking 

- result

Berisi file txt output program (solusi)

- test

Berisi file image atau txt untuk input program

## Image Processing Library

- OpenCV

OpenCV dimanfaatkan untuk mengurangi *noise* yang ada pada gambar serta membagi gambar menjadi 81 grid kecil.

| Kelebihan | Kekurangan |
| ---- | ---- |
| OpenCV merupakan *library* untuk mengolah gambar yang paling umum dimanfaatkan (terutama dalam bahasa pemrograman Python). *Library* ini memiliki beragam fungsi dan prosedur yang dapat dimanfaatkan untuk mengolah gambar sesuai keinginan developer. | Untuk pemula, OpenCV ini sedikit sulit karena membutuhkan pengalaman lebih dalam mengolah berbagai jenis struktur data yang ada dalam *library* Python dan membutuhkan pengetahuan tentang *library* NumPy untuk mengolah matriks *image*. |

- Pytesseract

Pytesseract dimanfaatkan untuk mengenali digit yang ada pada image sudoku. 

| Kelebihan | Kekurangan |
| ---- | ---- |
| Pengenalan teks dapat dilakukan (dengan *Optical Character Recognition*) tanpa perlu melatih agen pemroses gambar dengan *machine learning* | Instalasi *library* sedikit rumit sebab file binary nya harus diunduh dan diinstal terlebih dahulu. *Library* yang diimport juga harus diikuti dengan konfigurasi tesseract_cmd. |

## Referensi
1. A comprehensive guide to OCR with Tesseract, OpenCV and Python ([link](https://nanonets.com/blog/ocr-with-tesseract/))
2. Schermerhorn, Mike. *A Sudoku Solver* ([link](https://www.cs.rochester.edu/u/brown/242/assts/termprojs/Sudoku09.pdf))
3. Aljohani, Abdulaziz, et al. *N x N Sudoku Solver* ([link](https://www.cs.rit.edu/~ark/fall2016/654/team/02/report.pdf))