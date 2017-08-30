text = input("Text: ")
text_dict = {}
words = text.split()
for word in words:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1
for text in text_dict:
    print("{} : {}".format(text, text_dict[text]))
