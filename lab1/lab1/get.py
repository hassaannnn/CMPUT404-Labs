import requests as r

print(r.__version__)
x = r.get('http://google.com')
print(x)