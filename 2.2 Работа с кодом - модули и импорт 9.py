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