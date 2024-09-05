rate=0.02
loan=float(input("ระบุจำนวนเงินที่ต้องการกู้:"))
month=float(input("ระบุจำนวนเดือนที่ต้องการชำระเงิน:"))
inte= loan*rate
pay= (loan/month)+inte

print(f"ดอกเบี้ยที่ต้องชำระต่อเดือน  {loan*rate}")
print(f"ต้องผ่อนเดือนละ  {(loan/month)+inte}")
print(f"ยอดเงินที่ต้องจ่ายทั้งหมด  {pay*month}")

