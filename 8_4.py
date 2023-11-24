import math
a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
c=int(input("Nhap c: "))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Dien tich tam giac la: ",S)
