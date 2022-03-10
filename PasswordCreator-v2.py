import random
from questionary import select

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

num = "1234567890"
symbol = "[]{}#()*;._-"

answer = lower_case + upper_case + num + symbol

def bulkpassword():
    password = "".join(random.sample(answer, length))
    sifreler = open('C:/Users/OyuNet/Desktop/Şifreleyici/Pyhton Kodlarım/Sifreler.txt', 'a')  # Buraya kendi istediğiniz metin dosyasının konumunu girin.
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
        while True:
            if (amount > 0):
                bulkpassword()
                amount = amount - 1
            else:
                print('Şifreler başarıyla oluşturulmuştur.')
                break
    elif "Çıkış" in MainSelection:
        break            
