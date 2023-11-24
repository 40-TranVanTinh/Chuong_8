#Phương trình bậc nhất: ax+b=0
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
x=-b/a
if (x>0):
    print("Ta có PT:",a,"x","+",b,"=0")
    print("x=",x)
else:
    print("PT vô nghiệm")
