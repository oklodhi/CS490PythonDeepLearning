# grab the input as str from console. Input is the weight of each student in lbs separated by white space
inputweight = str(input("Enter weights(lbs) of students as a list, separated by a space: "))

# split and map the str input into a list of ints
inputlist = inputweight.split()
map_object = map(int, inputlist)

# create a list of ints from map object
lbslist = list(map_object)

# create empty list of kg
kglist = []

# iterate through lbs list and convert and append each lbs into kg
for idx in lbslist:
    x = idx * .453592
    kglist.append(x)

# print the result
print("L1: ", lbslist)
print("Output: ", kglist)