xe=int(input("Nhap loai xe: "))
so_km=int(input("Nhap so km: "))
time_cho=int(input("Nhap thoi gian cho: "))
if xe==4 and time_cho>5 and so_km<21 :
       print("Tien cho: ",(time_cho-5)*800)
       print("Tien di chuyen: ",so_km*12100+11000*0.8)
       print("Tien cuoc: ",(time_cho-5)*800 + so_km*12100+11000*0.8)
else:
        print("Tien cho: ",(time_cho-5)*800,"vnd")
        print("Tien di chuyen: ",20*12100+(so_km-20)*10000+11000*0.8,"vnd")
        print("Tien cuoc: ",(time_cho-5)*800 +20*12100+(so_km-20)*10000+11000*0.8,"vnd")
if xe==7 and time_cho>5 and so_km<31 :
        print("Tien cho: ",(time_cho-5)*800)
        print("Tien di chuyen: ",so_km*14100+13000*0.8)
        print("Tien cuoc: ",(time_cho-5)*800 + so_km*12100+11000*0.8)
else:
        print("Tien cho: ",(time_cho-5)*800,"vnd")
        print("Tien di chuyen: ",30*14100+(so_km-30)*12000+13000*0.8,"vnd")
        print("Tien cuoc: ",(time_cho-5)*800 +30*12100+(so_km-30)*12000+13000*0.8 ,"vnd")
