import core_model


def FileToFile(pathA: str, pathB: str):
    with open(pathA, 'r') as outFile:
        data = outFile.read().split('/n')
        data = list(filter(None, data))
    with open(pathB, 'a') as inFile:
        for i in data:
            dump = f'{i}\n'
            inFile.write(dump)
