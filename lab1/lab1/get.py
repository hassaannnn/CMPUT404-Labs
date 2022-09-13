import requests as r

print(r.__version__)
#Getting google

x = r.get('http://google.com')
myownscript = r.get("https://raw.githubusercontent.com/hassaannnn/CMPUT401-Labs/master/lab1/lab1/get.py").content
print(myownscript)