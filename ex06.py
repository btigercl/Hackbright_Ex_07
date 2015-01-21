from sys import argv 

script, filename = argv

def s_d(file_name):
    info = open(file_name)
    for line in info:
        line = line.rstrip()
        new_sort_dic = dict[(line)]
    return new_sort_dic 
print s_d(filename)