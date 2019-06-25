masalar=dict()
for i in range(10):
    masalar[1]=0


def hesapEkle():
    masaNo=int(input("Masa No: "))
    gecerli=masalar[masaNo]
    eklenecek=float(input("Eklenecek Ücret: "))
    toplam=gecerli+eklenecek
    masalar[masaNo]=toplam


def hesapSil():
    masaNo=int(input("Masa No: "))
    gecerli=masalar[masaNo]
    eksilecek=float(input("Eksilecek Ücret: "))
    toplam=gecerli-ekeksilecek
    masalar[masaNo]=toplam

def main():
    while True:
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [4] Çıkış
    
        """)

        secim=input("İşleminiz : ")

        if secim == "1":
            for i in range(10):
                print("Masa [] için hesap: []".format(i,masalar[i]))
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim=="2":
            hesapEkle()
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim=="3":
            hesapSil()
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim=="4":
            print("Çıkılıyorr..")
            quit()
             
main()