# פונקציה שמקבלת משפט אחד ומדפיסה כל מילה בנפרד

def sentence_split():
    # asking for input
    sentence = input("Enter your sentence here: \n")
    # splitting the sentence
    split_words = sentence.split()
    print(split_words)


if __name__ == '__main__':
    sentence_split()
