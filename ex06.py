from sys import argv 

script, filename = argv

def sort_and_print(file_name):
    info = open(filename)
    new_sort_dic = {}
    for line in info:
        line = line.rstrip()
        entries = line.split(":")
        key = entries[0]
        value = entries[1]
        new_sort_dic[key] = value
    for k, v in sorted(new_sort_dic.items()):
        print "Restaurant %s is rated at %s" % (k, v)

sort_and_print(filename)