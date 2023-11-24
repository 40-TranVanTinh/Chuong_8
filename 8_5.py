year=int(input("Nhap nam:"))
if year %4 ==0 or year%400 ==0 and year %100 !=0:
    print(year,"la nam nhuan")
else:
    print(year,"khong phai nam nhuan")