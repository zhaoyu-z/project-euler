# Source: https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-problem-61-cyclical-figurate-numbers/302173
# Convert from JavaScript

def cyclicalFigurateNums(n):
    def getChains(chain, n, numberTypes, numsExcludingLastNeededType):
        if len(chain) == n:
            return [chain]
        
        nextNumbers = getNextNumbersInChain(chain[-1], numsExcludingLastNeededType)
        
        chains = []
        for nextNumber in nextNumbers:
            if nextNumber not in chain:
                nextChain = chain + [nextNumber]
                chains += getChains(nextChain, n, numberTypes, numsExcludingLastNeededType)
        return chains
    
    def getNextNumbersInChain(num, numsExcludingLastNeededType):
        results = []
        beginning = num % 100
        for number in numsExcludingLastNeededType:
            if number // 100 == beginning:
                results.append(number)
        return results
    
    def fillNumberTypes(n, numberTypes, numsExcludingLastNeededType):
        lastTypeCheck, lastTypeArr = numberTypes[n - 1][1:]
        for i in range(1000, 10000):
            for j in range(n - 1):
                typeCheck, typeArr = numberTypes[j][1:]
                if typeCheck(i):
                    typeArr.append(i)
                    numsExcludingLastNeededType.add(i)
            if lastTypeCheck(i):
                lastTypeArr.append(i)
    
    def isCyclicalChain(chain, n, numberTypes):
        numberTypesInChain = getNumberTypesInChain(chain, numberTypes)
        if not isChainAllowed(numberTypesInChain, n):
            return False
        isChainCyclic = chain[0] // 100 == chain[-1] % 100
        return isChainCyclic
    
    def getNumberTypesInChain(chain, numberTypes):
        numbersInChain = {typeName: [] for typeName, _, _ in numberTypes}
        for i in range(n):
            for typeName, typeCheck, typeNumbers in numberTypes:
                if chain[i] in typeNumbers:
                    numbersInChain[typeName].append(chain[i])
        return numbersInChain
    
    def isChainAllowed(numberTypesInChain, n):
        for i in range(n):
            typeName, _, _ = numberTypes[i]
            isNumberWithTypeInChain = len(numberTypesInChain[typeName]) > 0
            if not isNumberWithTypeInChain:
                return False
            for j in range(i + 1, n):
                otherTypeName, _, _ = numberTypes[j]
                if isNumberRepeatedAsOnlyNumberInTwoTypes(numberTypesInChain[typeName], numberTypesInChain[otherTypeName]):
                    return False
        return True
    
    def isNumberRepeatedAsOnlyNumberInTwoTypes(typeNumbers, otherTypeNumbers):
        return len(typeNumbers) == 1 and len(otherTypeNumbers) == 1 and typeNumbers[0] == otherTypeNumbers[0]
    
    def isTriangle(num):
        return ((8 * num + 1) ** 0.5 - 1) % 2 == 0
    
    def isSquare(num):
        return num ** 0.5 == int(num ** 0.5)
    
    def isPentagonal(num):
        return ((24 * num + 1) ** 0.5 + 1) % 6 == 0
    
    def isHexagonal(num):
        return ((8 * num + 1) ** 0.5 + 1) % 4 == 0

    def isHeptagonal(num):
        return ((40 * num + 9) ** 0.5 + 3) % 10 == 0

    def isOctagonal(num):
        return ((3 * num + 1) ** 0.5 + 1) % 3 == 0

    numberTypes = [
        ['triangle', isTriangle, []],
        ['square', isSquare, []],
        ['pentagonal', isPentagonal, []],
        ['hexagonal', isHexagonal, []],
        ['heptagonal', isHeptagonal, []],
        ['octagonal', isOctagonal, []]
    ]

    numsExcludingLastNeededType = set()
    fillNumberTypes(n, numberTypes, numsExcludingLastNeededType)

    nNumberChains = []
    lastType = numberTypes[n - 1][2]
    for startOfChain in lastType:
        nNumberChains.extend(
            getChains([startOfChain], n, numberTypes, numsExcludingLastNeededType)
        )

    cyclicalChains = [chain for chain in nNumberChains if isCyclicalChain(chain, n, numberTypes)]

    sum = 0
    for chain in cyclicalChains:
        for num in chain:
            sum += num

    return sum

print(cyclicalFigurateNums(6))