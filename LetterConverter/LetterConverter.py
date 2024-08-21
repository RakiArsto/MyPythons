def replace_new_letter(sentence, dict_letter):
    new_sentence = ""
    for letter in sentence:
        if letter in dict_letter:
            new_sentence += dict_letter[letter]
        else:
            new_sentence += letter
    return new_sentence

sentence = input("Paste your text right here: \n")
dict_letter = {"ả": "a", "ã": "a", "ạ": "a", "ă": "a", "ắ": "á",
               "ằ": "à", "ẳ": "a", "ẵ": "a", "ặ": "a", "ấ": "â",
               "ầ": "â", "ẩ": "â", "ẫ": "â", "ậ": "â", "ẻ": "e",
               "ẽ": "e", "ẹ": "e", "ế": "ê", "ề": "ê", "ể": "ê",
               "ễ": "ê", "ệ": "ê", "ỏ": "o", "õ": "o", "ọ": "o",
               "ố": "ô", "ồ": "ô", "ổ": "ô", "ỗ": "ô", "ộ": "ô",
               "ớ": "ó", "ờ": "ò", "ở": "o", "ỡ": "o", "ợ": "o",
               "ủ": "u", "ũ": "u", "ụ": "u", "ứ": "ú", "ừ": "ù",
               "ử": "u", "ữ": "u", "ự": "u", "đ": "d", "Đ": "D",
               "ỉ": "i", "ĩ": "i", "ị": "i", "ỳ": "y", "Ả": "A",
               "Ã": "A", "Ạ": "A", "Ố": "Ô", "Ồ": "Ô", "Ổ": "Ô",
               "Ỗ": "Ô", "Ộ": "Ô", "Ứ": "Ú", "Ừ": "Ù", "Ử": "U",
               "Ữ": "U", "Ự": "U"}

new_sentence = replace_new_letter(sentence, dict_letter)
print(f"This is the new text: \n{new_sentence}")