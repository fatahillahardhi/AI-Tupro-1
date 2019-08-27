Soal
---

Lakukan analisis, desain, dan implementasi algoritma **_Simulated Annealing (SA)_** ke dalam suatu program komputer untuk menemukan *nilai minimum* dari fungsi:

f(x_1,x_2 )= -|sin(x1)cos(x2)exp(|1-√(x1^2+x2^2)/π|)|

dengan batasan -10 ≤ x1 ≤ 10 dan -10 ≤ x2 ≤10.

Jawaban
---

Dalam project saya, untuk hasil terbaik dari X1, X2, E saya simbolkan dengan X1 Best, X2 Best dan E Best. Program akan menghitung hasil dari X1 Best, X2 Best, E Best yang diberikan secara acak, berdasarkan rincian masalah program akan melakukan perulangan proses hingga 500 kali dan pengurangan iterasi dengan ΔT = 0,1 agar hasil dari perulangan tersebut lebih optimal karena banyaknya proses yang dicari, dan setiap hasil akan diambil yang paling minimum. Untuk penentuan parameter nilai X1 Best, X2 Best, E Best di ambil secara acak tetapi dengan batasan -10 ≤ x1 ≤ 10 dan -10 ≤ x2 ≤ 10. Dan nanti X1 Best, X2 Best, E Best akan masuk kedalam pencarian simulated annealing.
