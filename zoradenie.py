#!/usr/bin/python


def smallest(vstup):
	if vstup == []:
		print "Ziaden vstup!"
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


def sort(vstup):
	print(vstup)
	list = []
	if vstup == []:
		print "Ziaden vstup!"
	for i in range(len(vstup)):
		list.append(smallest(vstup))
		vstup.remove(smallest(vstup))
	return list



vstup = [5,4,8,100,68,59,48,48,52,77,33,47,49,28,18,10,0]
print(sort(vstup))

