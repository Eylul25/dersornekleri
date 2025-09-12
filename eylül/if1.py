print("not değerlendirme programı")
not1=int(input("ders puanın kaç?"))
print(f"ders puanın {not1}")
if not1>100 or not1<0:
    print("girilen puan 0 ile 100 arası olmalıdır")

else:
        if not1>90 : print("süpersin")
        if not1>50 and not1<90:
            print("gectin")
        if not1<50 : print("kaldın")