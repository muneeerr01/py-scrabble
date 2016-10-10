class WordDictionary:
    def __init__(self, fn):
        self.words = []
        with open(fn) as f:
            for line in f.readlines():
                self.words.append(line.rstrip().upper())

    def isValid(self, word):
        '''
        isValid(word)
        Uses a binary search to check if the word exists in the
        array.
        '''
        if word == '': return False

        word = word.upper()
        first, last = 0, len(self.words)
        while first != last:
            mid = (first + last) // 2
            if word == self.words[mid]:
                return True
            elif word > self.words[mid]:
                first = mid + 1
            elif word < self.words[mid]:
                last = mid
        return False

# Letter point value system
POINTS = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
          "X": 8, "Z": 10, " ": 0}

def wordScore(word):
    word = word.upper()
    return sum(map(lambda l: POINTS[l], word))