import tkinter as tk

def replace_new_letter(sentence, dict_letter):
    new_sentence = ""
    for letter in sentence:
        if letter in dict_letter:
            new_sentence += dict_letter[letter]
        else:
            new_sentence += letter
    return new_sentence

def process_text():
    sentence = input_text.get("1.0", "end-1c")
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
    output_text.delete("1.0", "end")
    output_text.insert("1.0", new_sentence)

root = tk.Tk()
root.geometry("600x600")
root.title("Text Converter")

input_label = tk.Label(root, text="Input:")
input_label.pack()

input_text = tk.Text(root, height=16, width=70)
input_text.pack()

process_button = tk.Button(root, 
                           text="Process", 
                           command=process_text,
                           font=("Courier New", 10),
                           width=15,
                           fg="#FFFB55",
                           bg="black",
                           activeforeground="#E1DC00",
                           activebackground="black")
process_button.pack()

output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = tk.Text(root, height=16, width=70)
output_text.pack()

root.mainloop()