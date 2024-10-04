sletters='abcdefghijklmnopqrstuvwxyz'
cletters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(Plaintext,key):
    ciphertext=''
    
    for char in Plaintext:
        if(char in sletters):
            newindex=(sletters.index(char)+key%26)
            ciphertext+=sletters[newindex]
        elif(char in cletters):
            newindex=(cletters.index(char)+key%26)
            ciphertext+=cletters[newindex]   
        else:
            ciphertext+=char
  
    return ciphertext 

def decrypt(Plaintext,key):
    decryptedtext=''
    for char in Plaintext:
        if(char in sletters):
            newindex=(sletters.index(char)-key%26)
            decryptedtext+=sletters[newindex]
        elif(char in cletters):
            newindex=(cletters.index(char)-key%26)
            decryptedtext+=cletters[newindex]   
        else:
            decryptedtext+=char
  
    return decryptedtext

print()
print('***Ceaser Cipher Program***');
print()


print('Do You Want To Encrypt or Decrypt?')

user_input=input('e/d').lower()
print()

if(user_input=='e'):
    print('Encryption Mode Selected')
    print()
    key=int(input('Enter the key (1 through 26):'))
    text=input('Enter The Text to encrypt: ')
    print(encrypt(text,key))
elif user_input=='d':
    print('Decryption Mode Selected')
    print()
    key=int(input('Enter the key '))
    text=input('Enter The Text to Decrypt: ') 
    print(decrypt(text,key));  
