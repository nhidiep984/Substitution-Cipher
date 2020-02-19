from random import shuffle

class Cipher:
    string = 'abcdefghijklmnopqrstuvwxyz '
    plaintext = list(string)

    def key_gen(self):
        to_shuffle = list(self.string)
        shuffle(to_shuffle)
        self.key = to_shuffle

    def encrypt(self, text):
        ciphertext = []
        self.ciphertext = ciphertext
        for letter in text:
            index_plaintext = self.plaintext.index(letter)
            encrypted_letters = self.key[index_plaintext]
            ciphertext.append(encrypted_letters)
        self.letter = letter
        print("Ciphertext:", ''.join(self.ciphertext))

    def decrypt(self, key):
        output = []
        print("Here is your key to decrypt:", ''.join(self.key))
        if input("Enter key:") == ''.join(self.key):
            for letter in key:
                index_output = self.key.index(letter)
                decrypted_letters = self.plaintext[index_output]
                output.append(decrypted_letters)
            print("Message decrypted: ", ''.join(output))
        else:
            print("Access denied!")

    def freq_analysis(self):
        ciphertext = self.ciphertext
        key_dict = dict.fromkeys(self.key, 0)
        for letter in ciphertext:
            if letter not in key_dict:
                key_dict[letter] = 0
            else:
                key_dict[letter] += 1
        for letter in key_dict:
            key_dict[letter] = key_dict[letter] / len(ciphertext)
        for k, v in key_dict.items():
            print(k, ':', v)


s = Cipher()
s.key_gen()
s.encrypt(input("Enter a string to encrypt: "))
s.decrypt(input("Enter message to decrypt: "))
s.freq_analysis()