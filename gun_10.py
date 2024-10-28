# for i in dir(""):
#     print(i.ljust(20))
# for i in dir(""):
#     print(i.rjust(20)) #karakter dizilerini sağa ve solahizalama görevi görür

# kardiz="tel no"
# print(kardiz.ljust(10,"."))

# for i in "elma","armut","patlıcan":
#     print(i.ljust(10,"."))

# for i in "elma","armut","patlıcan":
#     print(i.rjust(10,"."))

#zfill() karakter dizilerinin sol tarafına istediğimiz sayıda 0 ekleyebiliriz
a="12"
print(a.zfill(3))
for i in range(11):
    print(str(i).zfill(2))

#partition(), rpartition() karakter dizilerini belli bir ölçüte göre 3 e bölüyoruz
a="istanbul"
print(a.partition("an"))
print(a.partition("h"))
b="istihza"
print(b.partition("i"))
print(b.rpartition("i"))

#encode() karakter dizilerini kodlamak için kullanılır
print("çilek".encode("cp1254"))

#expandtabs() bir karakter dizisi içindeki boşlukları genişletebiliriz
s="elma\tbir\tmeyvedir"
print(s.expandtabs(10))