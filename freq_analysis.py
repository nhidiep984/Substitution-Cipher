import re

def main():
  ciphertext = input("Enter ciphertext: ")
  ciphertext = extract(ciphertext)
  freq_analysis(ciphertext)

def extract(ciphertext):
    ciphertext = ciphertext.replace(" ", '').lower()
    ciphertext_only_alpha = ""
    for char in ciphertext:
      if char.isalpha():
        ciphertext_only_alpha += char
    return ciphertext_only_alpha

def freq_analysis(ciphertext):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  letters_dict = dict.fromkeys(letters, 0)
  for letter_index in ciphertext:
    if letter_index not in letters_dict:
      letters_dict[letter_index] = 0
    else:
      letters_dict[letter_index] += 1
  for letter_index in letters_dict:
    letters_dict[letter_index] = letters_dict[letter_index] / len(ciphertext)
  for k,v in letters_dict.items():
    print(k, ":", v)

if __name__ == '__main__':
  main()