dict= {}

def toDict(*strings):
    for i in range(len(strings)):
        dict[i] = strings[i]
    return dict

print(toDict('Hello', 'ABC'))