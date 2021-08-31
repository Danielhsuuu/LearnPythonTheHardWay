tabby_cat = "\tI'm tabbed in"
persian_cat = "\tI'm split \non a line"
backlash_cat = 'I am \\ a \\ cat'

#use ' instead of " because you don't have to hold shift that way.
fat_cat = '''
I'll do a list:
\t- Cat food
\t- Fishies
\t- Catnip \n\t- Grass
'''

print("a tabby cat: %r" % tabby_cat)
print("a persian car: %s" % persian_cat)
print("a backlash cat: %r" % backlash_cat)
print(fat_cat)

#while True:
#    for i in ["/","-","|","\\","|"]:
#       print("%r\r" % i)