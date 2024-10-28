# Hata yakalama
# veri1 = input("Karekökünü hesaplamak istediğiniz sayı: ")
# karekok = int(veri1) ** 0.5
#
# print(veri1, "sayısının karekökü: ",karekok)
# veri2 = input("Karesini hesaplamak istediğiniz sayı: ")
# kare= int(veri2)**2
#
# print(veri2,"sayısının karesi: ",kare)
#
#
# sayi1 = input("Toplama işlemi için ilk sayıyı girin: ")
# sayi2 = input("Toplama işlemi için ikinci sayıyı girin: ")
# print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

# ilk_sayi = input("ilk sayı: ")
# ikinci_sayi = input("ikinci sayı: ")
# ilk_sayi = int(ilk_sayi)
# ikinci_sayi = int(ikinci_sayi)
# print(ilk_sayi, "/", ikinci_sayi, "=", ilk_sayi / ikinci_sayi)
#valueError ve ZeroDivisionError hataları üretebilir

#try.. except..
# sayi1=input("ilk sayı: ")
# sayi2=input("ikinici sayı: ")
# try:
#     num1=int(sayi1)
#     num2=int(sayi2)
#     print(num1,"/",num2,"=",num1/num2)
# # except ValueError:
# #     print("Lütfen sadece sayı giriniz: ")
# # except ZeroDivisionError:
# #     print("bir sayıyı 0 a bölemezsiniz")
# except (ValueError, ZeroDivisionError):
#     print("Bir hata oluştu.")

# while True:
#     ilk_sayi=input("ilk sayı (çıkmak için q ya basın): ")
#     if ilk_sayi=="q":
#         break
#     ikinci_sayi=input("ikinci sayı: ")
#     try:
#         sayi1=int(ilk_sayi)
#         sayi2=int(ikinci_sayi)
#         print(sayi1,"/",sayi2,"=",sayi1/sayi2)
#     except(ValueError,ZeroDivisionError):
#         print("bir hata oluştu.")
#         print("Lütfen tekrar deneyin")

# try... except... as...
# ilk_sayi = input("ilk sayı: ")
# ikinci_sayi = input("ikinci sayı: ")
# try:
#     sayi1 = int(ilk_sayi)
#     sayi2 = int(ikinci_sayi)
#     print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
# except (ValueError,ZeroDivisionError) as hata:
#     print("sadece sayı girin")
#     print("orijinal hata mesajı: ",hata)

#try... except... else...

# try:
#     bolunen = int(input("bölünecek sayı: "))
#     bolen = int(input("bölen sayı: "))
# except ValueError:
#     print("Lütfen Sadece sayı girin!")
# else:
#     try:
#         print(bolunen/bolen)
#     except ZeroDivisionError:
#         print("bir sayıyı 0 a bölemezsiniz!")

#try... except... finally...
# try:
#     ...bir takım işler...
# except birHata:
#     ...hata alınınca yapılacak işlemler...
# finally:
#     ...hata olsa da olmasa da yapılması gerekenler...

#raise
# bolunen = int(input("bölünecek sayı: "))
# if bolunen ==23:
#     raise Exception("Bu programda 23 sayısını görmek istemiyorum!")
# bolen = int(input("bölen sayı: "))
# print(bolunen/bolen)

# tr_karakter = "şçğüıİ"
# parola =input("parolanız: ")
# for i in parola:
#     if i in tr_karakter:
#         raise TypeError("Türkçe karakter kullanma!")
#     else:
#         pass
# print("Parola kabul edildi!")

#Assert
# giris = input("Merhaba! Adın ne?")
# if len(giris)==0:
#     raise AssertionError("isim bölümü boş bırakılamaz")
# print("Hoşgeldiniz.")

# giris = input("Merhaba! Adın ne?")
# assert len(giris) !=0 ,"isim bölümü boş bırakılamaz"
# print("Hoşgeldiniz.")

#Bütün Hataları yakalamak
# try:
#     birtakım kodlar
# except ValueError:
#     print("Yanlış değer")
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası")
# except:
#     print("Beklenmeyen bir hata oluştu!")

import sys
_2x_metni ="""
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı.
"""
_3x_metni="Programa hoşgeldiniz."
try:
    if sys.version_info.major<3:
        print(_2x_metni)
    else:
        print(_3x_metni)
except AttributeError:
    print(_2x_metni)









