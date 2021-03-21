alphabet='abcdefghijklmnopqrstuvwxyz'
key=5

def encryption(x):
        encrypt=''
        for i in x:
                p=alphabet.find(i)
                np=(p+key)% 26
                encrypt+=alphabet[np]
        return encrypt

def decryption(y):
        decrypt=''
        for i in y:
                p=alphabet.find(i)
                np=(p-key)%26
                decrypt+=alphabet[np]
        return decrypt

def main():
        print("What do you Want to do :")
        print("1.Encrypt the code")
        print("2.Decrypt the code")
        choice=int(input("What is your choice:"))
        if choice==1:
                msg=input("Enter the word:")
                print("The encrypted code:",encryption(msg))
        elif choice==2:
                msg=input("Enter Encrypted code:")
                print("The decrypted code:",decryption(msg))   


main()