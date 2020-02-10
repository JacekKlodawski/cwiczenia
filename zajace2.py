tekst = "zajac nr %d jest koloru %s"
zajace = [(1, 'zielony'), (2, 'fioletowy'), (3, 'szary'), (4, 'brązowy')]
for zajac in zajace:
    print(tekst % zajac)
[print(tekst % zajac) for zajac in zajace]

[print (number) for number in range(0, 10)]
