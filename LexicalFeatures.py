def getHostName(URL):
    if not containsIPAddress:
        if containsPortNumber:
            return URL.split(":")[0]
        else:
            return URL.split("/")[0]
    else:
        return None

def getPrimaryDomain():
    # TODO:
    return

def getPathTokens():
    return

def getLastPathTokens():
    return

def getTopLevelDomain():
    return

def getBagOfWords():
    return

def getLengthOfDomain():
    return

def getLengthOfURL():
    return

def getNumberOfDots():
    return

def getLetterFrequencies():
    return

def isSuspiciousURL():
    return

def containsIPAddress():
    return

def containsSubdomain():
    return

def getLengthOfFileName():
    return

def containsSuspiciousFile():
    return

def containsPortNumber():
    return
