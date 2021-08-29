def circlePhrase(phrase):
    if isCircle(list(phrase)):
        print(phrase)
    else:
        print('not circle')

def isCircle(phrase):
    if len(phrase) <= 1:
        return True
    else:
        if phrase[0] == phrase[-1]:
            return isCircle(phrase[1:-1])
        else:
            return False


phrase = 'ddddddddddddddddddddddddddddddddddddddda'
circlePhrase(phrase)