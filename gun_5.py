# Döngüler
# a = 1
# while a < 10:
#     print("döngü çalıştı", a)
#     a += 1

# giris = """
# (1) topla
# (2) çıkar
# (3) çarp
# (4) böl
# (5) karesini hesapla
# (6) karekök hesapla"""
#
# print(giris)
# while True:
#     soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q):")
#     if soru == "q":
#         print("çıkılıyor...")
#         break
#     elif soru == "1":
#         sayi1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
#         sayi2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
#         print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
#     elif soru == "2":
#         sayi3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
#         sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
#         print(sayi3, "-", sayi4, "=", sayi3 - sayi4)
#     elif soru == "3":
#         sayi5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
#         sayi6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
#         print(sayi5, "x", sayi6, "=", sayi5 * sayi6)
#     elif soru == "4":
#         sayi7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
#         sayi8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
#         print(sayi7, "/", sayi8, "=", sayi7 / sayi8)
#     elif soru == "5":
#         sayi9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
#         print(sayi9, "sayısının karesi =", sayi9 ** 2)
#     elif soru == "6":
#         sayi10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
#         print(sayi10, "sayısının karekökü = ", sayi10 ** 0.5)
#     else:
#         print("Yanlış giriş.")
#         print("Aşağıdaki seçeneklerden birini giriniz:", giris)

# while True:
#     soru = input("Nasılsınız, iyi misiniz?")
#     if soru == "q" or soru == "Q":
#         break

# tekrar = 1
# while tekrar <= 5:
#     tekrar += 1
#     input("Nasılsınız, iyimisiniz?")

# a = 0
# while a < 100:
#     a += 1
#     if a % 2 == 0:
#         print(a)

# For Döngüsü
tr_harfler = "şçöğüİı"
# for harf in tr_harfler:
#     print(harf)
# print()
# print(*tr_harfler, sep="\n")
# print()
# a = 0
# while a < len(tr_harfler):
#     print(tr_harfler[a], sep="\n")
#     a += 1

# parola = input("Parolanız: ")
# for karakter in parola:
#     if karakter in tr_harfler:
#         print("Parolada Türkçe karakter kullanılamaz")

# while True:
#     parola = input("Bir parola belirleyin:")
#     if not parola:
#         print("Parola boş geçilemez!")
#     elif len(parola) > 8 or len (parola) < 3:
#         print("Parola 8 karakterden uzun 3 karakterden kısa olamlı")
#     else:
#         print("Yeni parolanız" , parola)
#         break

# izinli_karakterler = "0123456789+-/*= "
# while True:
#     veri = input("İşleminiz: ")
#     if veri == "q":
#         print("çıkılıyor...")
#         break
#     for s in veri:
#         if s not in izinli_karakterler:
#             print("neyin peşindesin?")
#             quit()
#     hesap = eval(veri)
#     print(hesap)

# for i in range(0,10): #range(10) 0 dan 10 a kadar 10 dahil değil
#     print(i)
#
# while True:
#     parola = input("parola: ")
#     if not parola:
#         print("parola boş bırakılamz...:")
#     elif len(parola) in range(3,9):
#         print("yeni parolanız", parola)
#         break
#     else:
#         print("parola 8 karakteden uzun 3 karakterden kısa olmamalı")

# for i in range(3):
#     parola = input("parola belirleyin: ")
#     if not parola:
#         print("parola bölümü boş geçilemez!")
#     elif len(parola) in range(3, 8):
#         print("Yeni parolanız", parola)
#         break
#     elif i == 2:
#         print("parolayı 3 kez yanlış girdiniz.",
#         "Lütfen 30 dakika sonra tekrar deneyin!")
#     else:
#         print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

# for i in range(0,10,2): # range(10,0,-1) 10 9 8 ... 1
#     print(i)
# print(*range(0,10))
# print(*range(10),sep=", ")

# while True:
#     parola = input("parola belirleyin: ")
#     if not parola:
#         pass
#     elif len(parola) in range(3,9):
#         print("yeni parolanız", parola)
#         break
#     else:
#         print("parola 3-8 karakter arasında olmalı")


while True:
    sayi = int(input("Bir sayı girin: "))
    if sayi == 0:
        break
    elif sayi < 0:
        pass
    else:
        print(sayi)