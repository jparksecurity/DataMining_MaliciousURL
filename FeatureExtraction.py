import re

if __name__ == "__main__":
    websites_list = []

    with open("websites.txt", 'r') as f:
        for line in f:
            websites_list.append(line.rstrip('\n').split("//")[1])

    print(websites_list)

    hostname = []
    primaryDomain = []
    pathTokens = []
    lastPathToken = []
    topLevelDomain = []
    bagOfWords = []
    lengthOfURL = []
    numberOfDots = []

    for line in websites_list:
        hostname.append(line.split("/")[0])
        primaryDomain.append(hostname[-1].split(".", 1)[-1])#check -1
        if len(line.split("/", 1)) > 1:
            pathTokens.append(line.split("/", 1)[1])
        else:
            pathTokens.append("")
        if len(line.split("/")) > 1:
            lastPathToken.append(line.split("/")[-1])
        else:
            lastPathToken.append("")
        topLevelDomain.append(hostname[-1].split(".")[-1])
        if len(pathTokens[-1]) > 0:
            words = pathTokens[-1]
            words = words.replace('/', ',')
            words = words.replace('?', ',')
            words = words.replace('.', ',')
            words = words.replace('=', ',')
            words = words.replace('-', ',')
            words = words.replace('_', ',')
            bagOfWords.append(words.split(','))
        else:
            bagOfWords.append("")
        lengthOfURL.append(len(line))
        numberOfDots.append(line.count('.'))

    print(hostname)
    print(primaryDomain)
    print(pathTokens)
    print(lastPathToken)
    print(topLevelDomain)
    print(bagOfWords)
    print(lengthOfURL)
    print(numberOfDots)
