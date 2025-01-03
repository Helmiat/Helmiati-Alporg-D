# Program pengecekan rentang angka berdasarkan NIM
nim_awal = 2
nim_akhir = 0

# Masukkan angka
angka = int(input(f"Masukkan angka antara { 2 } dan { 0 }: "))

# Mengecek apakah angka dalam rentang NIM
if nim_akhir <= angka <= nim_awal:
    print(f"Angka {angka} berada dalam rentang { 2 } dan { 0 }.")
    
    # Operasi logika
    or_true = nim_akhir | True
    or_false = nim_akhir | False
    and_true = nim_akhir & True
    and_false = nim_akhir & False
    xor_true = nim_akhir ^ True
    xor_false = nim_akhir ^ False

    # Output hasil
    print(f"Jika nilai akhir di OR-kan dengan True maka: {or_true}")
    print(f"Jika nilai akhir di OR-kan dengan False maka: {or_false}")
    print(f"Jika nilai akhir di AND-kan dengan True maka: {and_true}")
    print(f"Jika nilai akhir di AND-kan dengan False maka: {and_false}")
    print(f"Jika nilai akhir di XOR-kan dengan True maka: {xor_true}")
    print(f"jika nilai akhir  di XOR-false dengan false maka: {xor_false}")
else: 
   print(f"angka {angka} tidak berada dalam rentang {nim_awal }dan {nim_akhir}.")
