#declares a string that contains four {} that can each take in strings and display them
formatter = "{} {} {} {}"
#prints 1 2 3 4
print(formatter.format(1, 2, 3, 4))
#prints one two three four
print(formatter.format("one", "two", "three", "four"))
#prints True False False True
print(formatter.format(True, False, False, True))
#prints 16 {}s
print(formatter.format(formatter, formatter, formatter, formatter))
#prints Try your Own text here Maybe a poem Or a song about fear
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))