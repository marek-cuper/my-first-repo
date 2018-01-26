#!/usr/bin/python

vstup = [8,5,6,7,4,12,10,3,9,18]
list = []
print(vstup)

porovnavatel = vstup[0]
for u in range(len(vstup)):
	if porovnavatel < vstup[u]:
		if porovnavatel == vstup[-1]:
			list.append(porovnavatel)
	elif porovnavatel > vstup[u]:
		if vstup[u] == vstup[-1]:
			list.append(porovnavatel)

		else:
			porovnavatel = vstup[u]

if len(list) == 0:
	list.append(porovnavatel)

print(list)




