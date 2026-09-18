
print("Sistem Pencatatan Hasil Panen")

hasil_panen = 100
harga_per_kg = 5000

total = hasil_panen * harga_per_kg

diskon = 0.10
potongan = total * diskon
total_setelah_diskon = total - potongan

print("Total hasil panen:", hasil_panen, "kg")
print("Harga per kg: Rp", harga_per_kg)
print("Total harga: Rp", total)
print("Diskon:", diskon * 100, "%")
print("Potongan harga: Rp", potongan)
print("Total setelah diskon: Rp", total_setelah_diskon)
