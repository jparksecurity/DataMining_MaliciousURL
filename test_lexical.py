from lexical_features import getHostName

def test_getHostName():
    test = "www.whatsmyip.org/random-website-machine"
    assert getHostName(test) == "www.whatsmyip.org"
