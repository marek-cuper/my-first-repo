#!/usr/bin/python

vstup = [1,8,9,10,6]
vysledok = " "
print(vstup)

porovnavatel = vstup[0]
for u in range(len(vstup)):
	if porovnavatel < vstup[u]:
		if porovnavatel == vstup[-1]:
			vysledok = porovnavatel
	elif porovnavatel > vstup[u]:
		if vstup[u] == vstup[-1]:
			vysledok = vstup[u]

		else:
			porovnavatel = vstup[u]

if vysledok == " ":
	vysledok = porovnavatel

print(vysledok)




