import sys
doc = open(sys.argv[1],"r")
dict1 = dict() #name:[University,Department]
for i in doc:
    a = i.split(":")
    dict1[a[0]] = a[1].split(",")
names = sys.argv[2].split(",")
for i in names:
    if i in dict1.keys():
        print("Name: {}, University: {},{}".format(i,dict1[i][0],dict1[i][1]),end = "")
    else:
        print("No record of '{}' was found!".format(i))
