import urllib.request


def down_page_data(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            url_data = resp.read()
        with open("url_data_1.txt", "wb+") as out_data:
            out_data.write(url_data)
        return "file downloaded correctly"
    except:
        return "file downloaded incorrectly"
