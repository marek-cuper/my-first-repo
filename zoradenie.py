#!/usr/bin/python

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

print(list_cisiel1)
for i in range(len(list_cisiel1)):
	porovnavane_cislo = list_cisiel1[i]
	for u in range(len(list_cisiel1)):
		print(list)
		if porovnavane_cislo < list_cisiel1[u]:
			if porovnavane_cislo == list_cisiel1[len(list_cisiel1)-1]:
				list.append(porovnavane_cislo)
			#	list_cisiel1.remove(porovnavane_cislo)
		elif porovnavane_cislo > list_cisiel1[u]:
			if list_cisiel1[u] == list_cisiel1[len(list_cisiel1)-1]:
				list.append(list_cisiel1[u])
			#	list_cisiel1.remove(list_cisiel1[u])
			else:
				porovnavane_cislo = list_cisiel1[u]
print(list)


