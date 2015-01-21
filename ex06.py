from sys import argv 

script, filename = argv

info = open(filename)

new_sort_dic = {}

for line in info:
    line = line.rstrip()
    entries = line.split(":")
    key = entries[0]
    value = entries[1]
    new_sort_dic[key] = value

print sorted(new_sort_dic.items())
