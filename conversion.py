def convert(celsiusList):
    farenList = []
    for temp in celsiusList:
        F = ((temp*9)/5)+32
        farenList.append(F)
    return farenList




convert([23,34,56])
