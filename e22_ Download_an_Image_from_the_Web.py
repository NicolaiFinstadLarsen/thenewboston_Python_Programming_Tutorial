import random
import urllib.request


def download_picture(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    
download_picture(str(input()))
