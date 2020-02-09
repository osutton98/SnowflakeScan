import tokenize
def fileReader():
    global file
    file = open(r"example.txt")
    tokens = tokenize.generate_tokens(file.readlines())
    result = [x[1] for x in tokens]
    print(result)

fileReader()

