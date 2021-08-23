from sys import argv

script, filename = argv
print("We're going to read %r." % filename)
readWhatFile = open(filename)
print(readWhatFile.read())