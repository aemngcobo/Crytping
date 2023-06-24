#Create an encryption and decryption communication code

mylist= ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")


def pwd_encrypt(UserText):
    store=""
    for x in UserText:
            initial_pos=mylist.index(x)
            encrypt_pos=initial_pos+7
            new_char=mylist[encrypt_pos]
            store=store+new_char
    print(store)


def pwd_decrypt(UserText2):
    store2=""
    for y in UserText2:
            initial_pos=mylist.index(y)
            encrypt_pos=initial_pos-7
            new_char=mylist[encrypt_pos]
            store2=store2+new_char
    print(store2)
    

UserAction=input("Do you want to encrypt or decrypt message?:")
User=input("Enter message:")

if UserAction=="encrypt":
    pwd_encrypt(User)
else:
    pwd_decrypt(User)
        