# kisi=input("Aradığınız kişinin adı ve soyadı: ")
# kisi=kisi.lower() #bütün karakterleri küçük harfe çevirir
# if kisi == "ahmet öz":
#     print("email: aoz@hmail.com")
#     print("tel : 02121231212")
#     print("şehir: istanbul")
# elif kisi == "mehmet söz":
#     print("email: msoz@zmail.com")
#     print("tel : 03121231212")
#     print("şehir: ankara")
# elif kisi == "mahmut göz":
#     print("email: mgoz@jmail.com")
#     print("tel : 02161231212")
#     print("şehir: İstanbul")
# else:
#     print("Aradığınız kişi veritabanında yok!")
#
# iller="ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
# iller=iller.replace("I","ı").replace("İ","i").lower()
# print(iller)
#
# kardiz="kalem"
# kardiz=kardiz.upper()
# print(kardiz)
# kardiz="istihza"
# print(kardiz.isupper())
# print(kardiz.islower())
#
# veri=input("mesajınız: ")
# bol=veri.split()
# for i in bol:
#     if i.isupper():
#         print("Tamamı büyük harflerden oluşan kelimeler kullanmayın!")
# kardiz="istihza"
# print(kardiz.endswith("a")) #sonu a ile bittiğinin kontrölü
# print(kardiz.startswith("i"))#i le başladğının kontrölü

# a="python programlama"
# print(a.capitalize()) #stringin ilk harfini büyük yapar
# kardiz="istanbul büyükşehir belediyesi"
# if kardiz.startswith("i"):
#     kardiz="İ"+kardiz[1:]
# kardiz=kardiz.capitalize()
# print(kardiz)
#
# print(a.title())#stringin bütün kelimelerin ilk harfini büyük yazar
#
# kardiz = "istanbul"
# if kardiz.startswith("i"):
#     kardiz = "İ" + kardiz[1:]
#     kardiz = kardiz.title()
# else:
#     kardiz = kardiz.title()
# print(kardiz)
#
# kardiz="on iki ada"
# for kelime in kardiz.split():
#     if kelime.startswith("i"):
#         kelime="İ"+kelime[1:]
#     kelime=kelime.title()
#     print(kelime,end=" ")

# kardiz="Python"
# print(kardiz.swapcase()) # küçük karakterleri büyük büyükleri küçük yapar
# kardiz = "istanbul"
# for i in kardiz:
#     if i == 'İ':
#         kardiz = kardiz.replace('İ', 'i')
#     elif i == 'i':
#         kardiz = kardiz.replace('i', 'İ')
#     else:
#         kardiz = kardiz.replace(i, i.swapcase())
# print(kardiz)

# kardiz=" istihza "
# print(kardiz)
# print(kardiz.strip()) #verilen string deki istenmeyen kısımları atar varsayılan boşluktur
# kardiz="kazak"
# print(kardiz.strip("k"))
#
# metin="""> mehmet
# > serif
# > ceylan"""
# for i in metin.split():
#     print(i.strip("> "),end=" ")
# print()
# print("kazak".lstrip("k"))#stringin solunda istenmeyen karakteri atar
# print("kazak".rstrip("k"))#stringin sağında istenmeyen karakteri atar

# kardiz="Galatasaray Spor Kulübü"
# bolunmus=kardiz.split()
# print(bolunmus)
# print(" ".join(bolunmus)) #verilen parçalı stringleri birleştirir
#
# sehir="kahramanmaraş"
# print(sehir.count("a")) #verilen karakterin string içinde kaç defa geçtiğini verrir
#
# parola=input("parolanız: ")
# kontrol=True
# for i in parola:
#     if parola.count(i)>1:
#         kontrol=False
# if kontrol:
#     print("parolanız onaylandı!")
# else:
#     print("parolanızda aynı harfi 1 kez kullanabilirsiniz!")
#
# kelime=input("kelime: ")
# for harf in kelime:
#     print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))

# kardiz="python"
# print(kardiz.index("p")) #verilen karakterin stringin hangi indexinde geçtiğini verir
# #print(kardiz.index("j"))
# print("adana".index("a")) #ilk bulduğunu verir
# kardiz="adana"
# print(kardiz.index("a"))
# print(kardiz.index("a",1))
# print(kardiz.index("a",1,3))
# print("-------------")
# kardiz=input("metin girin: ")
# aranacak=input("Aradığınız harf: ")
# for i in range(len(kardiz)):
#     if i == kardiz.index(aranacak,1):
#         print(i)

# kardiz="adana"
# print(kardiz.rindex("a"))
#
# print(kardiz.find("a"))
# print(kardiz.rfind("a"))
# print(kardiz.rfind("z")) #bulamadığında -1 verir

for metot in dir(""):
    print(metot.center(15)) #verilen değeri 15 karakterlik bir alanda ortalayarak yazar
kardiz="python"
print("----------------------")
for i in range(1,20):
    print(kardiz.center(i))

kardiz="elma"
print(kardiz.center(10,"-"))
