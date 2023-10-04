'''
Алиса владеет интересной информацией, которую хочет заполучить Боб. Алиса умна, поэтому она хранит свою информацию в зашифрованном файле. У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt. Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.
'''

from simplecrypt import decrypt

passwords_list = []  
with open("passwords.txt") as passwords:
    for password in passwords:
        password = password.rstrip()  
        passwords_list.append(password)  #
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read() 


def decrypt_inf(passw, txt):  
    for p in passw:
        try:  
            return decrypt(p, txt).decode("utf-8")
        except: 
            continue


print(decrypt_inf(passwords_list, encrypted))
