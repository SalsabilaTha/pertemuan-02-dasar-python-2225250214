"""
Program Biodata Mahasiswa
"""

TAHUN_SEKARANG = 2026 

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan kelas: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))

umur = TAHUN_SEKARANG - tahun_lahir

print("\n===== KARTU BIODATA =====")
print(f"Nama : {nama}")
print(f"NIM : {nim}")
print(f"Kelas : {kelas}")
print(f"Tahun Lahir : {tahun_lahir}")
print(f"Perkiraan Umur: {umur} tahun")
print("========================")
