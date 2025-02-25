




a= int(input("masukkan usia: "))

if a==0:
  print("belum lahir")
elif a<4:
  print("lu balita")
elif a >= 5 and a <= 10:
  print("lu anak anak")
elif a >10 and a <= 15:
  print("lu pra remaja")
elif a >15 and a <= 20:
  print("lu remaja")
elif a > 20 and a <= 40:
  print("lu dewasa")
elif a > 40 and a <= 60:
  print("lu udah mau tua")
elif a > 60 and a <= 90:
  print("lu lanjut usia")
else :
  print("mati aja")