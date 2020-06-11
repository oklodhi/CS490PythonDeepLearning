# open the file, read each line and split based every word. Close the file
f = open("sample.txt")
line = f.read()
words = line.split()
f.close()

# create a word count dictionary and keep track of frequency
wordcount = {}
for w in words:
    if w not in wordcount:
        wordcount[w] = 0
    wordcount[w] += 1

print(wordcount)

# open same file as append and write the word count to the bottom of file
f = open("sample.txt", "a")
f.write("\n\n")
for key, value in wordcount.items():
    f.write('%s: %s\n' % (key, value))
f.close()