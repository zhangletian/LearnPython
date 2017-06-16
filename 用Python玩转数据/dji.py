import requests

url = 'http://money.cnn.com/data/dow30/'
r = requests.get(url)
print(r.text)
