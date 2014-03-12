import os
word_list = ['green', 'sustainable', 'environment']

desired_words = {'green', 'sustainable', 'environment'}

input_words = {'green', 'red', 'blue'}

def calculate_score(university):
    pass

def get_sources(university):
    pass

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def _naive_score(university):

    score = 0
    files = []
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            files.append(file)
            #data = set([line.strip() for line in open("data/"+file, 'r')])
            data = read_words("data/"+file)
            d = []
            for word in data:
                for d_word in desired_words:
                    if d_word in word:
                        d.append(word)
            score += len(d)/(1.0*len(data))
    return score
