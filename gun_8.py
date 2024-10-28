# # Karakter Dizileri
# nesne = "karakter dizisi"
# print(nesne)
# for c in nesne:
#     print(c)
#
# print(*nesne, sep="\n")
# nesne = "123456789"
# for n in nesne:
#     print(int(n) * 2)
#
# print(int(nesne[1])*2)
# print(nesne[len(nesne)-1]) #son eleman
# #print(nesne[len(nesne)])
# print(nesne[-1]) #son eleman -2 sondan 1 önce
#
# for i in range(9): #range(len(nesne))
#     print(nesne[i])
# for i in range(len(nesne)):
#     print(nesne[i])
#
# isim=input("isminiz: ")
# for i in range(len(isim)):
#     print("isminizin {}. harfi: {}".format(i+1,isim[i]))
#
# #karakter dizilerini dilimlemek

# site="www.istihza.com"
# print(site[4:11]) #[ilk_oge : son_oge+1]
# print(site[:11])
# print(site[11:])
#
# site1 = "www.google.com"
# site2 = "www.istihza.com"
# site3 = "www.yahoo.com"
# site4 = "www.gnu.org"
#
# for isim in site1, site2, site3, site4:
#     print("Site: ",isim[4:-4])
#
# kardiz="Sana Gül Bahçesi Vadetmedim"
# print(kardiz[::-1])
# print(kardiz[7:4:-1])
#
# for i in reversed(kardiz):
#     print(i,end="")
# print()
# print(*reversed(kardiz),sep="")

#Karakter dizilerini alfabe sırasına göre dizmek
# print(sorted("kitap"))
# print(*sorted("kitap"),sep="")
# for i in sorted("kitap"):
#     print(i,end="")
# print()

# kardiz="istihza"
# print(id(kardiz))
# kardiz ="İ"+kardiz[1:]
# print(id(kardiz)) #immutable(değiştirilemeyen)

# sesli_harfler = "aeıioöuü"
# sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
#
# sesliler=""
# sessizler=""
# kelime="istanbul"
# for i in kelime:
#     if i in sesli_harfler:
#         sesliler+=i
#     else:
#         sessizler+=i
#
# print("sesli harfler: ",sesliler)
# print("sessiz harfler: ",sessizler)

# print(dir(str))
# print(dir(int))
# print(dir("")) #str ile aynı
# sayac =0
# for i in dir(""):
#     if "_" not in i[0]:
#         sayac+=1
#         print(sayac, " : ", i)
# print("Toplam {} adet metot ile ilgileniyoruz.".format(sayac))

#enumerate
# print(*enumerate("istihza"))
# for i in enumerate("istihza"):
#     print(i)
#
# for sira, metot in enumerate(dir("")):
#     print(sira, metot)
#
# for sira, harf in enumerate("serif",3):#3 den başlayarak verir
#     print(sira, harf)
#
# #print(help())
# help(dir)

kardiz="elma"
print(kardiz.replace("e","E"))
kardiz="memleket"
print(kardiz.replace("e","",1))

kardiz="İstanbul Büyükşehir Belediyesi"
print(kardiz.split())
for i in kardiz.split():
    print(i)

kardiz=input("kısaltmasını öğrenmek istediğiniz kurum adını girin: ")
for i in kardiz.split():
    print(i[0],end="")

kardiz="Ankara Büyükşehir Belediyesi"
print(kardiz.split(" ",1))
print(kardiz.rsplit(" ",1))


