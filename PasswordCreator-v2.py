import random
from questionary import select
import os.path
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

config = dotenv_values(".env")

localLang = config.get("LANG")
path = config.get("BULKPATH")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

num = "1234567890"
symbol = "[]{}#()*;._-"

answer = lower_case + upper_case + num + symbol



def checkFile():
    if (os.path.exists(path)):
        print("Bulk file found.")
    else:
        open(path, "x")
        print(path + " can't found. Created...")

def bulkpassword():
    password = "".join(random.sample(answer, length))
    sifreler = open(path, 'a')  
    sifreler.write(password+'\n')
    sifreler.close
    
def setPath(newPath):
    os.system("dotenv set BULKPATH " + newPath)

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
                fileInput = str(input("Yeni dosya adını giriniz (.txt olmadan): "))
                newpath = "./" + fileInput + ".txt"
                print("Yeni dosya adınız: " + fileInput + ".txt")
                
            elif "Geri" in SettingsSelection:
                break        
    elif "Çıkış" in MainSelection:
        os.system("clear")
        break
