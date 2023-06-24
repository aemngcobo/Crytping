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

UserText=input("Please enter message:")
pwd_encrypt(UserText)
        