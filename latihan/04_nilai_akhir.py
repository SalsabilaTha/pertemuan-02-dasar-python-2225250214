#program Menghitung Nilai Akhir Mahasiswa

nama = input("Masukkan nama: ")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir =(
     (nilai_tugas * 0.20) + 
     (nilai_uts * 0.30) + 
     (nilai_uas * 0.50)
)

print("\n===== HASIL PERHITUNGAN NILAI AKHIR =====")
print(f"Nama Mahasiswa: {nama}")
print(f"Nilai Tugas: {nilai_tugas:.2f}")
print(f"Nilai UTS: {nilai_uts:.2f}")    
print(f"Nilai UAS: {nilai_uas:.2f}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
