from sys import argv 

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
                
    return counting

def printing_by_line(counting):
    for k,v in counting.items():
        print k,v 

def main():
    script, filename = argv
    counted_dict = counting_words(filename)
    pretty_list = printing_by_line(counted_dict)


if __name__ == '__main__':
    main()

