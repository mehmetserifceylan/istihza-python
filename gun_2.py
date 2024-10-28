# Kaçış dizileri (escape sequence)
print('Ahmet, "Bugün sinemaya gidiyorum," dedi.')
print('Yarın Adana\'ya gidiyorum')
print("Python programlama dilinin adı \"piton\" yılanından gelmez")
print("Python \
      Java \
      C#")
print("Hello \nWorld")
title = "Türkiye'de Özgür Yazılımın Geçmişi"
print(title, "\n", "-" * len(title), sep="")
print("C:\\nisan\\masraflar.txt")
print("C:/nisan/masraflar.txt")

print("abc\tdef")  # bir tab boşluk koyar
print(*"123456789", sep="\t")
print("\a" * 20)  # bip sesi çıkarır

print("Merhaba\rZalim Dünya!")  # kaçış dizisinden sonra gelen stringi satır başı yapıyor
print("Merhaba\rDünya")

print('istihza\b\b\bsna')

print('\u0130')  # UNICODE
print('\U00000131')
import unicodedata

print(unicodedata.name('a'))
print("\N{LATIN SMALL LETTER A}")

print('\x41')  # 16 lık sistemdeki karşılığını verir
print("\x4E")

print(r"Kurulum dizini: C:\aylar\nisan\toplam masraf")  # r ile bütün kaçış dizilerinden kurtuluyoruz

f = open("deneme.txt", "w")
print("deneme\fdeneme", file=f)
f.close()

# Kullanıcıdan Bilgi Almak input()
isim = input("Isminiz nedir? : ")
print("Merhaba", isim, end="!\n")

v1 = input("Toplama işlemi için ilk sayıyı girin: ")
v2 = input("Toplama işlemi için ikinci sayıyı girin: ")

v1 = int(v1)  # v1 karakter dizisini int e çeviriyoruz tip dönüşümü
v2 = int(v2)

print(v1, "+", v2, "=", v1 + v2)

sayi = 23
kardiz = str(sayi) # str tip dönüşümü
print(kardiz)
print(type(kardiz))

a = 10
print(a)
print(type(a))
print(float(a))

c = 12+0j
print(type(c))