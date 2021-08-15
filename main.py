import requests
print(requests.get("https://www.pepper.it/codici-sconto/amazon.it").text.split('href="https://www.pepper.it/offerte/')[1].split('"')[0])