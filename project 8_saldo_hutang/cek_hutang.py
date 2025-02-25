



saldo_awal= 5_000
hutang=50_000


print('   Saldomu: ',saldo_awal)
print('   Hutangmu: ',hutang)
deposit= int(input("   deposit berapa: "))
totalan= saldo_awal+deposit
print("")
print('   total saldomu sekarang: ',totalan)


if totalan >= hutang:
  print('   bayar utang woi')
else:
  print('   kumpulin duitnya buat bayar utang')