import re
def cleaner(path):
    file = open(path)
    line2 = ""
    for line in file.readlines():
        m = re.split("\s+",line)
        line1 = ""
        for word in m:
            line1 = line1 + word + ","
        line2 = line2 + line1[:len(line1)-2] + "\n"
    file.close()
    file = open(path,"w")
    file.write(line2)
    file.close()

cleaner("data.txt")
