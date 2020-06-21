#Encryptor and Decryptor using ord and chr
import time

def Cipher():
    option = '' #To choose either to encrypt, decrypt or quit
    def encrypt():
        enc_msg = ''
        msg = input('Enter message to encryt:\n')
        for i in msg:
            enc_ord_i = ord(i) + 1000
            enc_msg += chr(enc_ord_i)
        print('Enc >> ',enc_msg)

    def decrypt():
        dec_msg = ''
        msg = input('Enter message to decryt:\n')
        for i in msg:
            dec_ord_i = ord(i) - 1000
            dec_msg += chr(dec_ord_i)
        print('Dec >> ',dec_msg)

            
    while option == '':
        option = input('Enter 1 to enctryt, 2 to decrypt, other key to quit: ')
        if option == '1':
            encrypt()
            option = ''
        elif option == '2':
            decrypt()
            option = ''
        elif option != '1' or '2':
            print('Quitting ...')
            time.sleep(2)
            break
Cipher()


            
