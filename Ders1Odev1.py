"""
string => Metinsel veri tipidir.
float => Ondalıklı sayı türünde veri tipidir.
integer => Tam sayı türünde veri tipidir.
boolean => Karar mekanizmalarında kullanılarn True ve False değerini alan veri tipidir.
complex => Kompleks sayıları belirten veri tipidir.
list => Birden veya birden fazla elemanı içinde barındırıp gruplayan veri tipidir.(elemanlar birbirini tekrar edebilir.)
set => list ile aynı işlevi sahiptir fakat aralarındaki tek fark set aynı elemanı birden fazla kez barındıramaz.
tuple => Kısaca özetlemek gerekirse değiştirilemez listelerdir.




Kodlama.io sitesinde yer alan bütün metinsel ifadeler string veri tipine sahiptir.
Sitede yer alan tüm tam sayılar integer veri tipine örnektir.
Sitede yer alan "giriş yap" kısmı boolean veri tipine örnek olabilir.

"""

email = "batuhankelami@gmail.com"
sifre = "123456"
usermail = input("Lütfen mail adresini girin:")
usersifre = input("Lütfen şifrenizi girin:")

if email == usermail and sifre == usersifre:
    print("Giriş baraşılı!")
else:
    print("Giriş başarısız!")