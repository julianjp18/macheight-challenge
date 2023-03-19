import sys

def calculatePairs():
    try:
        data = input('')
        lastNumbers = {}
        splitted = data.split(' ')
        if len(splitted) != 2:
            sys.exit()
        exactValue = int(splitted[1])
        numbers = splitted[0].split(',')
        for index, number in enumerate(numbers):
            currentValue = int(exactValue) - int(number)
            if currentValue in lastNumbers:
                format = "%s,%s" % (numbers[lastNumbers.get(int(exactValue) - int(number))], numbers[index])
                print(f'{format}')
            else:
                lastNumbers[int(number)] = index
    catch:
        sys.exit()

calculatePairs()