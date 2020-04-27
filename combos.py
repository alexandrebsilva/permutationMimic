#Author: Alexandre Borges
#E-mail: alexandre.bsilva55@gmail.com

#Prints all permutations of letters of a given word

#REFERENCE: https://docs.python.org/2/library/itertools.html
import itertools

def returnAllCombinations(word,size):
    return list(itertools.permutations(word, size))

def convertCombinationInToList(combinationTuple):
    singleValue = []
   
    for letters in combinationTuple:
        singleValue.append(''.join(letters))

    return singleValue

#MAIN FUNCTION
def combos(word):
    #extra feature
    itemsCounter = 0

    count = 1
    while count <= len(word):
        combinationTuple = returnAllCombinations(word,count) 
        combinationItems = convertCombinationInToList(combinationTuple)

        #convert combinations into simple strings        
        for combination in combinationItems:
            print(combination)
            itemsCounter = itemsCounter + 1

        count = count + 1

    #extra feature
    print('Total de combinações possíveis: ', itemsCounter)


#FIRE UP
combos(input('Digite a palavra desejada: '))