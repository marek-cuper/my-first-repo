#!/usr/bin/python
pocet_cisiel = ""
vstup = ""
list = []
list_cisiel1 = []
list_cisiel2 = []
list_cisiel_v_poradi = []
print("Zadavaj cisla ktore chces zoradit, ak uz nechces zadavat, napis koniec")

while vstup != "koniec":
	vstup = raw_input("")
	try:
        	cislo = int(vstup)
        	list_cisiel1.append(cislo)

	except ValueError:
		if vstup != "koniec":
			print("Oops! Toto nie je cislo, skuste znova alebo ukoncite pomocou prikazu koniec")

if vstup == "koniec":
	pocet_cisel = len(list_cisiel1)
	list_cisiel1 = list_cisiel2
	for i in range(pocet_cisiel):
		porovnavane_cislo = list_cisiel2[i]
		for u in range((pocet_cisiel)-1):
			if porovnavane_cislo >= list_cisiel2[u]:
			elif u == ((pocet_cisel) -1):
				list.append(porovnavane_cislo)
				break
			else:
				 porovnavane_cislo = list_cisiel2[u]
	print(list)

