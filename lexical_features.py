import re

class URLLexical(object):
    def __init__(self, url):
        from urllib.parse import urlparse
        self.url = urlparse(url)
        import tldextract
        self.correctedHostname = tldextract.extract(self.url.hostname)

    def getHostname(self):
        return self.url.hostname

    def getPrimaryDomain(self):
        return self.correctedHostname.registered_domain

    def getLengthOfDomain(self):
        return len(self.url.hostname)

    def getLengthOfURL(self):
        return len(self.url.geturl())

    def getNumberOfDots(self):
        return self.url.geturl().count('.')

    def getHostnameTokens(self):
        return self.url.hostname.split('.')

    def getPrimaryDomainTokens(self):
        return self.correctedHostname.registered_domain.split('.')

    def getPathTokens(self):#need to work
        if self.url.path:
            tokens = re.split('[\W_]+', self.url.path)
            if not tokens[0]:
                tokens = tokens[1:]
            if not tokens[-1]:
                tokens = tokens[:-1]
            if tokens:
                return tokens
        else:
            None

    def getLastPathTokens(self):
        return self.getPathTokens()[-1] if self.getPathTokens() is not None else None

    def getTopLevelDomain(self):
        return self.correctedHostname[2]

    def getLetterFrequencies(self):
        import collections
        return collections.Counter(re.sub('[\W_]+', '', self.url.hostname.rsplit('.', 1)[0]))

    def getNumberOfUniqueCharacters(self):
        return len(list(self.getLetterFrequencies()))

    def containsSubdomain(self):
        return True if self.correctedHostname.subdomain else False

    def containsIPAddress(self):
        import socket
        if not self.correctedHostname.subdomain and not self.correctedHostname.suffix:
            host = self.correctedHostname.domain
            if socket.gethostbyname(host) == host:
                return True
        else:
            return False

    def containsPortNumber(self):
        return False if self.url.port is None else True
