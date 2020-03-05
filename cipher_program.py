from string import ascii_lowercase
import random

def main():
  key = key_gen()
  message = input("Enter message to encrypt: ").lower()
  ciphertext = encryption(message, key)
  print(f"Ciphertext: {ciphertext}")
  print(f"Key: {key}")
  ciphertext = input("Enter ciphertext to decrypt: ")
  decrypted_message = decryption(ciphertext, key)
  print(f"Decrypted message: {decrypted_message}")

def key_gen():
  letters = 'abcdefghijklmnopqrstuvwxyz'
  key = list(letters)
  random.shuffle(key)
  return ''.join(key)


def encryption(message, key):
  translation = str.maketrans(ascii_lowercase, key)
  return message.translate(translation)

def decryption(ciphertext, key):
  translation = str.maketrans(key, ascii_lowercase)
  return ciphertext.translate(translation)

if __name__ == '__main__':
  main()