def count_words(str):
    arr = str.split()
    return len(arr)

def count_chars(str):
    return len(str)

def find_most_common_word(str):
    arr = str.split()
    dict = {}
    for word in arr:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    highest = 0
    frequent = ""
    for word in dict:
        if highest < dict[word]:
            highest = dict[word]
            frequent = word
    
    return frequent

def main():
    print(count_words("  "))
    print(count_chars("this is a test"))
    print(find_most_common_word("this is a test a test test"))

if __name__ == "__main__":
    main()