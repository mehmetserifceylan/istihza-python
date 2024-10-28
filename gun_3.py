# ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
# nisan = haziran = eylul = kasim = 30
# subat = 28
#
# # Doğalgazın vergiler dahil metreküp fiyatı
# birim_fiyat = 0.79
#
# aylikSarfiyat = input("Aylık doğalgaz sarfiyatını metreküp olarak giriniz: ")
#
# donem = input("Hesaplamak istediğiniz ayı giriniz(küçük harflerle yaz):")
#
# # yukarıdaki input() fonksiyonundan gelen değeri
# # python ın anlayabileceği bir biçime dönüştürüyoruz
# ay = eval(donem)
#
# # kullanıcının günlük doğalgaz sarfiyatı
# gunlukSarfiyat = int(aylikSarfiyat) / ay
#
# # fatura tutarı
# fatura = birim_fiyat * gunlukSarfiyat * ay
#
# print("Günluk sarfiyatınız: \t", gunlukSarfiyat, " metreküp\n",
#       "tahmini fatura tutarı: \t", fatura, " TL", sep="")

# Eval ve exec() Fonksiyonları

# veri=input("İşleminiz: ")
# hesap=eval(veri)
# print(hesap)
# exec() fonkisyonu aynı şekilde çalışır farkı eval değişken tanımına izin
# vermez exec te bu işlemi gerçekleştirebiliriz.

# format metodu
# url = input("URL: ")
# print("Hata! Google Chrome", url, "sitesini bulamadı")
# print("Hata! Google Chrome {} sitesini bulamadı".format(url))
# print("{} ve {} iyi bir ikilidir.".format("Python","Django"))
# print("{} {} yaşında bir {}dur".format("serif","18","futbolcu"))
#
# metin= "{} ve {} iyi bir ikilidir".format("Python","Django")
# print(metin)
# metin2 = "{} ve {} iyi bir ikilidir"
# print(metin2.format("Python","Django"))
# dilekce=""""
#                                                 tarih: {}
#
#
# T.C
# {} ÜNİVERSİTESİ
# {} Fakültesi Dekanlığına
# Fakülteniz {} Bölümü {} numaralı öğrencisiyim.
# Ekte sunduğum belgede belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı
# {}. yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.
#
#       Bilgilerinizi ve gereğini arz ederim.
#
#             İmza
#
# Ad                : {}
# Soyad             : {}
# T.C Kimlik No     : {}
# Adres             : {}
# Tel               : {}
# Ekler             : {}
# """
# tarih = input("tarih: ")
# universite = input("universite: ")
# fakulte = input("fakulte: ")
# bolum =input("bolum: ")
# ogrenci_no = input("ogrenci no: ")
# ogretim_yili = input("ogrenci yili: ")
# yariyil=input("yariyil: ")
# ad =input("ad: ")
# soyad = input("soyad: ")
# tc_kimlik_no = input("tc_kimlik no: ")
# adres =input("adres: ")
# tel = input("tel: ")
# ekler = input("ekler: ")
#
# print(dilekce.format(tarih,universite,fakulte,bolum,ogrenci_no,
#                      ogretim_yili,yariyil,ad,soyad,tc_kimlik_no,adres,
#                      tel,ekler))

# if elif else

# n = 11
# if n > 10:
#     print("Sayı 10 dan büyüktür.")
#
# num1 = int(input("Bir sayı giriniz: "))
# if num1 > 10:
#     print("Girdiğiniz sayı 10 dan büyük.")
# if num1 < 10:
#     print("Girdiğiniz sayı 10 dan küçük.")
# if num1 == 10:
#     print("Girdiğiniz sayı 10 a eşittir.")
#
# parola = input("Parola: ")
# if parola == "123456789":
#     print("Siateme hoşgeldiniz!")
# if parola != "123456789":
#     print("Yanlış Parola girdin.")

# yas = int(input("Yaşınız: "))
# if yas == 18:
#     print("18 iyidir!")
# elif yas < 0:
#     print("Yok canım, daha neler!...")
# elif yas < 18:
#     print("Genç bir kardeşimizsin!")
# elif yas > 18:
#     print("Eh, artık yaş yavaş yavaş kemale eriyor!")

# soru = input("Bir meyve adı söyleyin bana:")
# if soru == "elma":
#     print("evet, elma bir meyvedir...")
# elif soru == "karpuz":
#     print("evet, karpuz bir meyvedir...")
# elif soru == "armut":
#     print("evet, armut bir meyvedir...")
# else:
#     print(soru, "gerçekten bir meyve midir?")
#
# boy = int(input("boyunuz kaç cm?"))
# if boy < 170:
#     print("boyunuz kısa")
# elif boy < 180:
#     print("boyunuz normal")
# else:
#     print("boyunuz uzun")

kullanici_adi = input("Kullanıcı Adınız: ")
parola = input("Parola: ")

toplam_uzunluk=len(kullanici_adi)+len(parola)
mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor"
print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk >40:
    print("Kullanıcı adınız ile parolanızın "
          "toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme Hoşgeldiniz!")

