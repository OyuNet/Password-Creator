import random
from questionary import select
import os.path

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

num = "1234567890"
symbol = "[]{}#()*;._-"

answer = lower_case + upper_case + num + symbol

def checkFile():
    if (os.path.exists("./sifreler.txt")):
        print("sifreler.txt found.")
    else:
        open("./sifreler.txt", "x")
        print("./sifreler.txt can't found. Created...")

def bulkpassword():
    password = "".join(random.sample(answer, length))
    sifreler = open('./sifreler.txt', 'a')  # Buraya kendi istediğiniz metin dosyasının konumunu girin.
    sifreler.write(password+'\n')
    sifreler.close

while True:
    MainSelection = select(
    "Hangi işlemi istiyorsunuz?",
    choices = ['Tekli Şifre Oluştur',
                'Çoklu Şifre Oluştur',
                'Ayarlar',
                'Çıkış'],
    ).ask()
    
    if "Tekli Şifre Oluştur" in MainSelection:
        length = int(input("Şifreniz kaç haneli olsun: "))
        password = "".join(random.sample(answer, length))
        print("Parolanız: ", password)

    elif "Çoklu Şifre Oluştur" in MainSelection:
        length = int(input("Şifreniz kaç haneli olsun: "))
        amount = int(input("Kaç tane şifre oluşturmak istiyorsunuz: "))
        checkFile()
        while True:
            if (amount > 0):
                bulkpassword()
                amount = amount - 1
            else:
                print('Şifreler başarıyla oluşturulmuştur.')
                break
    
    elif "Ayarlar" in MainSelection:
        while True:
            SettingsSelection = select(
            "Ayarlara hoş geldiniz. Değiştirmek istediğiniz ayarı seçiniz.",
            choices = ['Dil Tercihi',
                       'Toplu Kayıt Dosyası',
                       'Geri']    
            ).ask()
            if "Dil Tercihi" in SettingsSelection:
                while True:
                    LangSelection = select(
                    "Dilinizi tercih ediniz",
                    choices = ['Türkçe',
                                'İngilizce',
                                'Geri']
                    ).ask()
                    if "Türkçe" in LangSelection:
                        print("Diliniz Türkçe olarak ayarlandı.")
                        break
                    elif "İngilizce" in LangSelection:
                        print("Diliniz İngilizce olarak ayarlandı.")
                        break
                    elif "Geri" in LangSelection:
                        break
                
            elif "Toplu Kayıt Dosyası" in SettingsSelection:
                fileInput = str(input("Yeni dosya adını giriniz: "))
                print("Yeni dosya adınız: " + fileInput + ".txt")
                
            elif "Geri" in SettingsSelection:
                break        
    elif "Çıkış" in MainSelection:
        break            
