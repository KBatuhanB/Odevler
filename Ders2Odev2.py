ogrenciler = ["Batuhan Bölükbaşı","İrfan Günaygün","Yiğit Uçaroğlu"]



def ogrenciEkleme():
    isim = input("Örenci İsmi: ")
    soyisim = input("Öğrenci Soyismi: ")
    ogrenciler.append(isim+ " " +soyisim)
    for ogrenci in ogrenciler:
        print(ogrenci)
    
ogrenciEkleme()


def ogrenciCikarma():
    isim = input("Örenci İsmi: ")
    soyisim = input("Öğrenci Soyismi: ")
    TamAD = isim + " " +soyisim
    ogrenciler.remove(TamAD)
    for ogrenci in ogrenciler:
        print(ogrenci)

ogrenciCikarma()


def ogrenciListe():
    for ogrenci in ogrenciler:
        print(ogrenci)

ogrenciListe()



def ekleme():
    sayi = int(input("Kaç kişi ekliyeceksiniz? "))
    i = 0
    while i < sayi :
        isim = input("Örenci İsmi: ")
        soyisim = input("Öğrenci Soyismi: ")
        ogrenciler.append(isim+ " " +soyisim)
        i += 1
    else:
        for ogrenci in ogrenciler:
            print(ogrenci)

ekleme()


def ekleme ():
    i = 0
    ogrenci = input("Numarasını istediğiniz öğrencinin adı ve soyadı: ")
    while i < len(ogrenciler):
        if ogrenciler[i] == ogrenci:
            print(i)
            break
        else:
            i += 1


ekleme()
    



def silme():
    x = int(input("Kaç kişi çıkarmak istediğinizi yazın: "))
    i = 0
    while i < x :
         isim = input("Örenci İsmi: ")
         soyisim = input("Öğrenci Soyismi: ")
         TamAD = isim + " " +soyisim
         ogrenciler.remove(TamAD)
         i += 1
    else:
         for ogrenci in ogrenciler:
            print(ogrenci)
         

silme()



