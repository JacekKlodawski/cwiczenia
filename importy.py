import urllib.request

stronka = urllib.request.urlopen('https://pl.wikipedia.org/')

tekst = stronka.read()

print(tekst.find('go'.encode('utf-8')))
print(tekst.count('go'.encode('utf-8')))