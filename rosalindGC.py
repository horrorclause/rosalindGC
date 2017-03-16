import re


def gcCount():

    info=input('file location:')
    data = open(info, 'r')
    text = data.read()
    text = text.replace('\n','')

    taxonRegex= re.compile(r'(Rosalind[_]\d+)')
    taxonInfo = taxonRegex.findall(text)
    gcRegex = re.compile(r'Rosalind[_]\d+(\w+)')
    gcInfo = gcRegex.findall(text)

    #print(taxonInfo)
    #print(gcInfo)

    taxonCount = 0
    percentDict = {}

    for block in gcInfo:
        G = 0
        C = 0
        for letter in block:
            if letter == "C":
                C +=1
            elif letter =="G":
                G +=1

        percent= ((C+G)/len(block))*100
        percentDict[taxonInfo[taxonCount]] = percent
        taxonCount+=1
    '''
    for k,v in percentDict.items():
        print(k,v)


    print('*_*_*_*_*__*_*_*_*_*_*_*_*')'''

    maxKey = max(percentDict, key=percentDict.get)

    print(maxKey, "%.6f" % percentDict[maxKey]+'%')


gcCount()