# program Kalkulator BMI
print("-"*10)
print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("-"*10) 

berat_badan = float(input("Masukkan berat badan anda (Kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan anda (M) :"))/100

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f'Nilai BMI anda adalah {bmi:.2f} Kg/M^2')
print(f'Nilai BMI normal adalah 18.5 Kg/M^2 sampai 25Kg/M^2')
print(f'''Berat badan ideal anda adalah dalam rentang
      {berat_badan_ideal['bawah']:.2f} Kg sampai {berat_badan_ideal['atas']:.2f} Kg''')

print("terimakasih sudah menggunakan program ini")