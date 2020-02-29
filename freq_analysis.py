def main():
  ciphertext = input("Enter ciphertext: ")
  ciphertext = ciphertext.replace(" ", '')
  letters = 'abcdefghijklmnopqrstuvwxyz'
  freq_analysis(ciphertext)

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