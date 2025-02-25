from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(["Nama", "Usia", "Kota"])
ws.append(["Ali", 25, "Jakarta"])
ws.append(["Budi", 30, "Surabaya"])

wb.save("data.xlsx")
