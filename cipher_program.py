from string import ascii_lowercase
import random

def main():
  key_gen()
  message = input("Enter message to encrypt: ").lower()
  ciphertext = encryption(message)
  print(f"Ciphertext: {ciphertext}")
  print(f"Key: {key}")
  ciphertext = input("Enter ciphertext to decrypt: ")
  decrypted_message = decryption(ciphertext)
  print(f"Decrypted message: {decrypted_message}")

def key_gen():
  global key
  letters = 'abcdefghijklmnopqrstuvwxyz'
  key = list(letters)
  random.shuffle(key)
  key = ''.join(key)

def encryption(message):
  translation = str.maketrans(ascii_lowercase, key)
  return message.translate(translation)

def decryption(ciphertext):
  translation = str.maketrans(key, ascii_lowercase)
  return ciphertext.translate(translation)

if __name__ == '__main__':
  main()