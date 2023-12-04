
ret_list = []

with open('english-words.10', encoding="iso8859-1") as word_file:
    for line in word_file:
        word = line.strip().replace("'", "")
        if len(word) == 4:
            ret_list.append(word)

print(set(ret_list))