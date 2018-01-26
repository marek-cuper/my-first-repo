#!/usr/bin/python


def smallest(vstup):
	vysledok = " "
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

	return(vysledok)


print(smallest([5,4,8,3]))

