# program Kalkulator BMI
print("-"*50)
print("PERHITUNGAN BMI (BODY MASS INDEX)".center(50))
print("-"*50) 

berat_badan = float(input("Masukkan berat badan anda (Kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan anda (Cm) :"))/100

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if bmi < 18.5 :
  kategori = "ANDA KEKURANGAN BERAT BADAN"
elif bmi < 25:
  kategori = "NILAI BMI ANDA NORMAL"
elif bmi < 30:
  kategori = "ANDA KELEBIHAN BERAT BADAN"
else:
  kategori = "ANDA MENGALAMI OBESITAS"

print("-"*50)
print("Hasil Kalkulasi BMI anda adalah".center(50))
print("-"*50)
print(f'\nNilai BMI anda adalah {bmi:.2f} Kg/M^2')
print(f"\n{kategori}")
print(f'\nNilai BMI normal adalah 18.5 Kg/M^2 sampai 25Kg/M^2')
print(f'''Berat badan ideal anda adalah dalam rentang
      {berat_badan_ideal['bawah']:.2f} Kg sampai {berat_badan_ideal['atas']:.2f} Kg''')

print("\nterimakasih sudah menggunakan program ini")