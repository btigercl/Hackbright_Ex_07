from sys import argv 

script, filename = argv

def counting_words(filename):
    data = open(filename)
    counting = {}
    for line in data:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            if word not in counting:
                counting[word] = 1
            else: 
                counting[word] = counting[word] + 1 
    print counting


counting_words(filename)


