# Break deyimi
# while True:
#     parola = input("Lütfen bir parola belirleyin: ")
#     if len(parola) < 5:
#         print("parola 5 karakterden az olamaz")
#     else:
#         print("parolanız belirlendi! ")
#         break

# Continue Deyimi
# while True:
#     s=input("Enter a number: ")
#     if s=="iptal":
#         break
#     if len(s)<=3:
#         continue
#     print("en fazla 3 haneli bir sayı girmelisiniz.")

# for i in range(5):
#     print(i)
# else:
#     print("else çalıştı.")

# a=0
# while True:
#     a+=1
#     print(a)
#     if a==3:
#         break
# else:
#     print("else çalıştı.")
# karakter_dizisi="m"
# for harf in karakter_dizisi:
#     if harf == "a":
#         print("a harfi bulundu.")
#         break
# else:
#     print("a harfi bulunmadı")
#1.Örnek
# ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
# ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
# fark=""
# for s in ilk_metin:
#     if not s in ikinci_metin:
#         if not s in fark:
#             fark += s
# print(fark)

#2.Örnek
# d1 = open("isimler1.txt",encoding="utf-8")
# d1_satirlar=d1.readlines()
#
# d2=open("isimler2.txt",encoding="utf-8")
# d2_satirlar=d2.readlines()
#
# for i in d2_satirlar:
#     if not i in d1_satirlar:
#         print(i)
# d1.close()
# d2.close()

#3 örnek metinde verilen harften kaç adet kullanıldığını veren program
# metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
# tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
# isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
# yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
# adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
# Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
# gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
# da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
# edilmesi neredeyse bir gelenek halini almıştır."""
#
# harf = input("Sorgulamak istediğiniz harf: ")
# sayi=''
# for s in metin:
#     if harf==s:
#         sayi+=harf
# print(len(sayi))

#aynı örneği bi de dosyadan okuyarak yapalım
hakkinda = open("hakkinda.txt",encoding="utf-8")
harf = input("sorgulamak istediğiniz harf: ")
sayi =0
for s in hakkinda:
    for k in s:
        if harf==k:
            sayi+=1
print(sayi)
hakkinda.close()