def repeated_word(words):
    words.lower()
    words = words.split(" ")
    counter = 0

    count = {}
    for word in words:
        if word in count:
            print(word)
        # else:
        #     counter = counter + 1
        #     count[word] = counter


if __name__ == "__main__":
    words = "Once upon a time, there was a brave princess who..."
    print(repeated_word(words))
