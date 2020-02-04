# put your code here.
def word_count(filename):

    filename = open(filename)
    word_dict = {}

    for line in filename:
        line = line.rstrip()
        line = line.split(" ")
        
        for word in line:

            word_dict[word] = word_dict.get(word, 0) + 1

    for word, number in word_dict.items():
        print(f'{word} {number}')

# word_count("test.txt")


word_count("test.txt")