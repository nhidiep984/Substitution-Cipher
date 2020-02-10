from random import shuffle

string = 'abcdefghijklmnopqrstuvwxyz'
plaintext = list(string)


class Cipher:

    def key_gen(self):
        to_shuffle = list(plaintext)
        shuffle(to_shuffle)
        self.key = to_shuffle

    def encrypt(self, text):
        output = ''
        for letter in text:
            index_plaintext = plaintext.index(letter)
            encrypted_letters = self.key[index_plaintext]
            output = output + encrypted_letters
        print("Ciphertext:", repr(output))

    def decrypt(self, key):
        output2 = ''
        print("Here is your key to decrypt:", ''.join(self.key))
        if input("Enter key:") == ''.join(self.key):
            for letter in key:
                index_output = self.key.index(letter)
                decrypted_letteres = plaintext[index_output]
                output2 = output2 + decrypted_letteres
            print("Message decrypted: ", repr(output2))
        else:
            print("Access denied!")


s = Cipher()
s.key_gen()
s.encrypt(input("Enter a string to encrypt: "))
s.decrypt(input("Enter message to decrypt: "))