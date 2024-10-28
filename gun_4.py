# _*_ coding: utf-8 _*_
# kullanici = input("Kullanıcı Adınız: ")
# if bool(kullanici) == True:
#     print("Teşekkürler! ")
#genelde buraya kadar olan kısmı kullanılır.
# else:
#     print("Kullanıcı adı alanı boş bırakılmamalı! ")

# kullanici_adi = input("Kullanıcı Adınız: ")
# parola=input("Parola: ")
#
# if kullanici_adi == "aliveli" and parola == "123456789":
#     print("Programa Hoşgeldiniz")
# else:
#     print("Yanlış kullanıcı adı veya parola!")

# x = int(input("Notunuz: "))
#
# if x >100 or x<0:
#     print("Böyle bir not yok")
# elif 90 <= x <= 100:
#     print("A Aldınız.")
# elif 80 <= x <= 89:
#     print("B Aldınız.")
# elif x>=70  <=79:
#     print("C Aldınız")
# elif x>=60 and x<=69:
#     print("D Aldınız.")
# elif x>=0 and x<=59:
#     print("F aldınız.")
#
# #yukarıda 3 şekilde de yazabiliriz
#
# parola = input("Parola: ")
# if not parola:
#     print("Parola boş bırakılamaz")

# giris = len(input("Adın ne: "))
#
# if giris < 4:
# #if (giris := len(input("Adın ne?"))) <4:  #Walrus operatörü
#     print("Adın Kısaymış.")
# elif giris < 6:
#     print("Adın biraz uzunmuş")
# else:
#     print("Çok uzun bir adın var.")

# giris = """
# (1) Topla
# (2) Çıkar
# (3) Çarp
# (4) Böl
# (5) Karesini Hesapla
# (6) Karekök Hesapla
# """
#
# print(giris)
#
# soru = input("Yapmak isteiğiniz işlemin numarasını giriniz: ")
# if soru == "1":
#     sayi1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
#     sayi2= int(input("Toplama işlemi için ikinci sayıyı girin:"))
#     print(sayi1, "+", sayi2, "=" , sayi1 + sayi2)
# elif soru == "2":
#     sayi3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
#     sayi4= int(input("Çıkarma işlemi için ikinci sayıyı girin:"))
#     print(sayi3, "-", sayi4, "=" , sayi3 - sayi4)
# elif soru == "3":
#     sayi5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
#     sayi6= int(input("Çarpma işlemi için ikinci sayıyı girin:"))
#     print(sayi5, "x", sayi6, "=" , sayi5 * sayi6)
# elif soru == "4":
#     sayi7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
#     sayi8= int(input("Bölme işlemi için ikinci sayıyı girin:"))
#     print(sayi7, "/", sayi8, "=" , sayi7 / sayi8)
# elif soru == "5":
#     sayi9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
#     print(sayi9, "sayısının karesi=" , sayi9 ** 2)
# elif soru == "6":
#     sayi10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
#     print(sayi10, "sayısının karekökü=", sayi10 ** 0.5)
# else:
#     print("Yanlış Giriş:")
#     print("Aşağıdaki seçeneklerden birini giriniz:",giris)

import sys
print(sys.version_info)
print(sys.version)

_2x_metni = u"""
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı.
"""
_3x_metni = "Programa Hoşgeldiniz."
# if sys.version_info.major<3:
if sys.version_info < (3, 0):
    print(_2x_metni)
else:
    print(_3x_metni)




