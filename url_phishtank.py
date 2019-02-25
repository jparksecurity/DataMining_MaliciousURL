def getURLs():
    key = "580de27a01d6c4b0ac4ae454495bc6e1df4671260b45fc91c5e6ba77dcd0c14d"
    link = "http://data.phishtank.com/data/{}/online-valid.json"

    import requests
    resp = requests.get(link.format(key))
    resp.close()

    if resp.status_code != 200 or resp.json() == []:
        raise Exception("Failed to retrieve data")

    urls = []
    for json in resp.json():
        urls.append(json['url'])
    return urls
