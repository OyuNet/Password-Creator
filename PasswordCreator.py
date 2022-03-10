import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

num = "1234567890"
symbol = "[]{}#()*;._-"

global answer
global length

answer = lower_case + upper_case + num + symbol

MainSelection = input("""(1 = Tekli Parola Oluşturma)
(2 = Çoklu Parola Oluşturma)
Hangi işlemi istiyorsunuz: """)

length = int(input("Şifreniz kaç haneli olsun: "))

def bulkpassword():
    password = "".join(random.sample(answer, length))
    sifreler = open('C:/Users/OyuNet/Desktop/Şifreleyici/Pyhton Kodlarım/Sifreler.txt', 'a')
    sifreler.write(" "+password)
    sifreler.close

if MainSelection == str(1):
    password = "".join(random.sample(answer, length))
    print("Parolanız: ", password)

elif MainSelection == str(2):
    amount = int(input("Kaç tane şifre oluşturmak istiyorsunuz: "))
    while(True):
        if (amount > 0):
            bulkpassword()
            amount = amount - 1
        else:
            break

else:
    print("Yanlış sayı girdiniz.")    

