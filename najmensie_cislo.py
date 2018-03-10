#!/usr/bin/python


def smallest(vstup):
	if vstup == []:
		print "Nic si nezadal, vole"
		return

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

	return vysledok

v = [4,8,5,6,3]
print(smallest(v))

