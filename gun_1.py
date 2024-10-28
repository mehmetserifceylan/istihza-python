import keyword
import sys

print("Hello World")
var = "mehmet serif ceylan"
print(type(var))  # değişkenin tipini verir
print(len(var))  # değişkenin karakter sayısnı verir
print(len(keyword.kwlist))
yasakli_kelimeler = keyword.kwlist
print(yasakli_kelimeler)
print(len(yasakli_kelimeler))

num = 4
print(num ** 4)  # sayınun üssünü hesaplar
print(num ** 0.5)  # sayınun üssünü hesaplar
print(pow(num, 2))  # sayınun üssünü hesaplar

print(pow(num, 3, 2))  # sayının 3. kuvvetini alıp 2 ile bölümünden kalanı verir

a = b = 10  # aynı satırda iki değişkene birlikte değer vermek
print(a, b)
x = 5
y = 2
print("x:", x, "y:", y)
x, y = y, x  # değişkenlerin değerlerini takas etme alternatifi temp değişkeni
print("x:", x, "y:", y)

# Print Fonksiyonu
print('Python programlama dilinin adı "piton" yılanından gelmez')
print("İstanbul'un 5 günlük hava durumu tahmini")
print("""Game Over!
Insert Coin!""")
print("https://", "www.", "google.", "com")
print("https://", "www.", "google.", "com",
      sep="")  # varsayılan olarak parametreler arasındaki boşluğu değiştirmeye yarar
print("T", "C", sep=".")
print("Adana", "Mersin", sep="-")  # sep' e parametre olarak sayı veremiyoruz
print('a', 'b', sep=None)  # None değeri varsayılan olarak boşluk ekler
print("birinci satır\nikinci satır\nüçüncü satır")
print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")
print("Bugün günlerden salı", end=".")
print("Bugün günlerden salı", end="\n")  # varsayılan olarak end alt satıra geçirir
print("Bugün günlerden salı", end=".\n")
print("bir", "iki", "üç", "on dört",
      sep=" mumdur ", end=" mumdur.\n")  # end değeri de sayı olamamz
print('a', 'b', end=None)

# file Parametresi
dosya = open("deneme.txt", "w")  # deneme.txt adlı bir dosya oluşturuldu
print("Merhaba ben Serif, Mehmet Serif!", file=dosya)  # çıktıyı dosya olarak değiştirdik
# standart çıktı sys.stdout dur
dosya.close()  # dosyaya yazdıktan sonra kapatıyoruz
import os

print(os.getcwd())  # çalışmakta olduğumuz dizini verir
print("Tahir olmak da ayıp değil", "Zühre olmak da",
      sep=" ", end="\n", file=sys.stdout)
f = open("kisisel_bilgiler.txt", "w")
print("Surahi Bardak", file=f)
print("Adana", file=f)
print("Ubuntu", file=f)
f.close()

# flush parametresi
# flush dosyayı kapatmayı beklemeden yazdırdıklarımızı dosyaya kaydeder.
dosya1 = open("deneme1.txt", "w")
print("Hello World", file=dosya1, flush=True)  # default değeri False dur

print("L", "i", "n", "u", "x", sep=".")
print(*"Linux", sep=".")
print(*"Galatasaray")

print(len("Galatasaray"))
# print(len("Galatasaray","İsciSpor")) #Hata verir çünkü tek parametre alır
# len(*"Galatasaray") # Hata verir 11 arguman vermeye calıştı
import sys

print(sys.stdout)
d = open("dosya3.txt", "w")
#sys.stdout = d # yada sys.stdout,f=f,sys.stdout
print("deneme metni", flush=True)
print(sys.stdout, flush=True)  # standart çıktıyı değiştiği için çıktılar dosyaya yazılıyor
print(sys.stdout.name)
print(sys.stdout.mode)
print(sys.stdout.encoding)  # üçü de dosyaya yazar
