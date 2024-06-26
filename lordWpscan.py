import os


os.system("figlet lordWpscan")


print("""
      LordWpscan Programına Hoş Geldiniz...
      1-Genel Tarama
      2-Sitedeki Tüm Yöneticileri Ve Yazarları Göster
      3-Sitede Tüm Eklentileri Göster
      4-Sitede Açık Bulunduran Eklentileri Göster
      5-Sitede Kullanılan Template Tema Bilgisini Göster
      6-Kullanılan Tema Üzerinde AçıKları Göster
      7-Kullanıcı Adını Bulduktan Sonra Şifre Denemesi Yap
      """)
seçim = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")

if seçim == "1":
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url" + site_adı)
elif seçim == 2: 
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url"+ site_adı + "-enumerate u")
elif seçim == 3:
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url"+ site_adı + "-enumerate p")
elif seçim == 4:
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url" + site_adı + "-enumerate vp")
elif seçim == 5:
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url " + site_adı + "-enumerate t")
elif seçim == 6:
    site_adı = input("Hedef Site Adını Giriniz:")
    os.system("wpscan -url" + site_adı + "-enumerate at")
elif seçim == "7":
    site_adı = input("Hedef Site Adını Giriniz:")
    kullanıcı_adı = input("Kullanıcı Adını Giriniz:")
    os.system("wpscan --url " + site_adı + " --wordlist wordlist.txt --username " + kullanıcı_adı)
else:
    print("Geçersiz seçim. Lütfen geçerli bir seçenek giriniz.")