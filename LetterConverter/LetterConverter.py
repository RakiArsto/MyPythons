def replace_new_letter(sentence, dict_letter):
    new_sentence = ""
    for letter in sentence:
        if letter in dict_letter:
            new_sentence += dict_letter[letter]
        else:
            new_sentence += letter
    return new_sentence

sentence = input("Paste your text right here: \n")

from DictLetter import dict_letter

new_sentence = replace_new_letter(sentence, dict_letter)
print(f"\nThis is the new text: \n{new_sentence}")