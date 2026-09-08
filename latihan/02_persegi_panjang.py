#Program Menghitung Luas dan Keliling Persegi Panjang

Panjang = float(input("Masukkan panjang persegi panjang: "))
Lebar = float(input("Masukkan lebar persegi panjang: "))

luas = Panjang * Lebar
keliling = 2 * (Panjang + Lebar)    

print("\n===== HASIL PERHITUNGAN =====")
print(f"panjang Persegi: {Panjang:.2f} m")
print(f"Lebar Persegi Panjang: {Lebar:.2f} m")
print(f"Luas Persegi Panjang: {luas:.2f} m²")              
print(f"Keliling Persegi Panjang: {keliling:.2f} m")  
