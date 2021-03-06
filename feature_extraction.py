if __name__ == "__main__":
    featuresOfURLs = []

    import url_phishtank
    for url in url_phishtank.getURLs()[:5]:
        from lexical_features import URLLexical
        u = URLLexical(url)
        featuresOfURL = {}
        featuresOfURL["Hostname"] = u.getHostname()
        featuresOfURL["PrimaryDomain"] = u.getPrimaryDomain()
        featuresOfURL["LengthOfDomain"] = u.getLengthOfDomain()
        featuresOfURL["LengthOfURL"] = u.getLengthOfURL()
        featuresOfURL["NumberOfDots"] = u.getNumberOfDots()
        featuresOfURL["HostnameTokens"] = u.getHostnameTokens()
        featuresOfURL["PrimaryDomainTokens"] = u.getPrimaryDomainTokens()
        featuresOfURL["PathTokens"] = u.getPathTokens()
        featuresOfURL["LastPathTokens"] = u.getLastPathTokens()
        featuresOfURL["TopLevelDomain"] = u.getTopLevelDomain()
        featuresOfURL["LetterFrequencies"] = u.getLetterFrequencies()
        featuresOfURL["NumberOfUniqueCharacters"] = u.getNumberOfUniqueCharacters()
        featuresOfURL["Subdomain"] = u.containsSubdomain()
        featuresOfURL["IPAddress"] = u.containsIPAddress()
        featuresOfURL["PortNumber"] = u.containsPortNumber()

        featuresOfURLs.append(featuresOfURL)

    print(featuresOfURLs)




    # print(websites_list)
    #
    # hostname = []
    # primaryDomain = []
    # pathTokens = []
    # lastPathToken = []
    # topLevelDomain = []
    # bagOfWords = []
    # lengthOfURL = []
    # numberOfDots = []
    #
    # for line in websites_list:
    #
    #     hostname.append(line.split("/")[0])
    #     primaryDomain.append(hostname[-1].split(".", 1)[-1])#check -1
    #     if len(line.split("/", 1)) > 1:
    #         pathTokens.append(line.split("/", 1)[1])
    #     else:
    #         pathTokens.append("")
    #     if len(line.split("/")) > 1:
    #         lastPathToken.append(line.split("/")[-1])
    #     else:
    #         lastPathToken.append("")
    #     topLevelDomain.append(hostname[-1].split(".")[-1])
    #     if len(pathTokens[-1]) > 0:
    #         words = pathTokens[-1]
    #         words = words.replace('/', ',')
    #         words = words.replace('?', ',')
    #         words = words.replace('.', ',')
    #         words = words.replace('=', ',')
    #         words = words.replace('-', ',')
    #         words = words.replace('_', ',')
    #         bagOfWords.append(words.split(','))
    #     else:
    #         bagOfWords.append("")
    #     lengthOfURL.append(len(line))
    #     numberOfDots.append(line.count('.'))
    #
    # print(hostname)
    # print(primaryDomain)
    # print(pathTokens)
    # print(lastPathToken)
    # print(topLevelDomain)
    # print(bagOfWords)
    # print(lengthOfURL)
    # print(numberOfDots)
